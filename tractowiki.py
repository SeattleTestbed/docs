"""
FIXME: add docstring
"""
import pickle
import subprocess
import os

githubID = {'enchl': ' <>', 'imcheng': ' <>', 'sal': ' <>', 
'vivekdesai_22': ' <>', 'justinc': '<justincappos@gmail.com>', 
'anuhya': ' <>', 'jchilton': ' <>', 'cosminb': ' <>', 'asekine': ' <>', 
'sjs25': ' <>', 'jenn': ' <>', 'alpers': ' <>', 'savvas': ' <>', 
'peter': ' <>', 'yemuru': ' <>', 'alexjh': ' <>', 'shawiz': ' <>', 
'jchen': ' <>', 'richard': ' <>', 'kon': ' <>', 'pheitt': ' <>', 
'gessiou': ' <>', 'rishi': ' <>', 'sushant': ' <>', 'aditi': ' <>', 
'couvb': ' <>', 'shurui': ' <>', 'jeffra45': ' <>', 'armon': 'armon <>', 
'sportzer': ' <>', 'ericms': ' <>', 'linda': ' <>', 
'choksi81': 'choksi81 <chintan.choksi22@gmail.com>', 
'mitchellh': ' <>', 'sabiha': ' <>', 'vlad': ' <>', 'tania': ' <>', 
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
'cemeyer': ' <>', 'pankhuri': ' <>', 'xuefenghuang': ' <>', 
'zackrb': ' <>', 'ivan': '<bestchai@cs.ubc.ca>', 'gpress': ' <>', 
'monzum': ' <monzum@gmail.com>', 'shoosh': ' <>', 'vjeko': ' <>', 
'mkaplan': ' <>'}

wiki_records_list = pickle.load(file("trac_wiki_dump.pickle"))
#how will I know that the UNIX time sort works?
wiki_records_list.sort(key = lambda row: row[2])

for pagename, version, time, author, text, comment in wiki_records_list:
  pagename = pagename.encode('utf8')
  text = text.encode('utf8')

  # Create a subdir for the page if required, e.g. Archive/AnOldPage.
  # (Caveat Windows users, we assume that `os.path.sep` is identical to "/".)
  if not os.path.exists(os.path.dirname(pagename)):
    try:
      os.makedirs(os.path.dirname(pagename))
    except OSError:
      if not os.path.isdir(pagename):
        continue

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

# Finally, push all of the commits
#subprocess.call(["git", "push", "origin","master"])

