"""
Read a previously-`pickle`d partial Trac wiki dump, and make single 
commits out of every edit to a page. Add edit comments as commit 
messages, try to construct meaningful file / directory names, etc.
"""
import pickle
import subprocess
import os

# Map Trac wiki user names to email addresses known 
# on GitHub
githubID = {'enchl': ' <>', 'imcheng': ' <>', 'sal': ' <>', 
'vivekdesai_22': ' <>', 'justinc': '<justincappos@gmail.com>', 
'anuhya': ' <>', 'jchilton': ' <>', 'cosminb': ' <>', 'asekine': ' <>', 
'sjs25': ' <>', 'jenn': ' <>', 'alpers': ' <>', 'savvas': ' <>', 
'peter': ' <>', 'yemuru': ' <>', 'alexjh': ' <>', 'shawiz': ' <>', 
'jchen': ' <>', 'richard': '<weissr@evergreen.edu>', 'kon': ' <>', 
'pheitt': ' <>', 'priyam': '<pn613@nyu.edu>',
'gessiou': ' <>', 'rishi': ' <>', 'sushant': ' <>', 'aditi': ' <>', 
'couvb': ' <>', 'shurui': ' <>', 'jeffra45': ' <>', 'armon': 'armon <>', 
'sportzer': ' <>', 'ericms': ' <>', 'linda': ' <>', 
'choksi81': 'choksi81 <chintan.choksi22@gmail.com>', 
'mitchellh': ' <>', 'sabiha': ' <>', 'vlad': '<vladimir.v.diaz@gmail.com>', 
'tania': ' <>', 
'ivan2': ' <>', 'alanloh': ' <>', 'kimbrl': ' <>', 'cmatthew': ' <>', 
'hdanny': ' <>', 'jaehong': ' <>', 
'us341': 'us341 <us341@nyu.edu>', 'aman': ' <>', 
'albert': '<albert.rafetseder+github@univie.ac.at>', 
'lukasp': '<luk.puehringer@gmail.com>', 'sojc701': ' <>', 
'sebass63': ' <>', 'leonwlaw': '<llaw02@students.poly.edu>', 'evan': ' <>', 
'butaud': ' <>', 'jsamuel': ' <>', 'anthony': ' <>', 'tc1466': ' <>', 
'sebastien': '<sebastien.awwad@nyu.edu>', 
'yanyan': ' <yanyanzhuang83@gmail.com>', 
'trac': ' <>', 
'nitin': ' <>', 'jflat06': ' <>', 'yskhoo': ' <>', 'MikeMosh': ' <>', 
'cemeyer': ' <>', 'pankhuri': ' <>', 'xuefenghuang': '<xh560@nyu.edu>', 
'zackrb': ' <>', 'ivan': '<bestchai@cs.ubc.ca>', 'gpress': ' <>', 
'monzum': ' <monzum@gmail.com>', 'shoosh': ' <>', 'vjeko': ' <>', 
'mkaplan': ' <>'}

# Read in pickle
wiki_records_list = pickle.load(file("trac_wiki_dump.pickle"))

# Sort wiki edits by timestamp
wiki_records_list.sort(key = lambda row: row[2])

# For every page, create an appropriately-named file with the page 
# contents, and add a timestamped git commit for the page author.
for pagename, version, time, author, text, comment in wiki_records_list:
  pagename = pagename.encode('utf8')
  text = text.encode('utf8')

  # Create a subdir for the page if required, e.g. Archive/AnOldPage.
  # (Caveat Windows users, we assume that `os.path.sep` is identical to "/".)
  # Pages that have no subdir raise the `OSError` below.
  pagedir = os.path.dirname(pagename)
  if not os.path.exists(pagedir):
    try:
      os.makedirs(pagedir)
    except OSError:
      pass
  # Use the "wiki" file extension so that we get some level of markup 
  # rendering on GitHub
  filename = pagename + ".wiki"

  # Write out the file contents
  f = open(filename, "w")
  f.write(text)
  f.close()
 
  # Add the file to the staging area 
  subprocess.call(["git", "add", filename])

  # Construct the commit message, adding a detailed comment if available
  message = "Revision " + str(version) + " of " + pagename
  if comment:
    message += "\n\n" + comment

  commit_command = ["git", "commit", filename, "-m", message, "--date=" + 
      str(time), "--author=" + author + " " + githubID[author]]

  # Debug: show the commit command before execution
  print commit_command
  subprocess.call(commit_command)

