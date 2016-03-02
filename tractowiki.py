import pickle
from subprocess import call
import os
#githubID = {'albert': "aaaaalbert", 'justinc': "JustinCappos", ‘sebastien’: “awwad”, ‘leonwlaw’: “linkleonard”, 'choksi81': "choksi81", 'us341':"us341"}
wiki_records_list = pickle.load(file("trac_wiki_dump.pickle"))
#how will I know that the UNIX time sort works?
wiki_records_list.sort(key = lambda row: row[2])

for i in wiki_records_list:
  #print str(i) + "\n"
  name = i[0].encode('utf8')
  version = i[1]
  time = i[2]
  author = i[3]
  text = i[4].encode('utf8')
  comment = i[5]
  if not os.path.exists(os.path.dirname(name)):
    try:
      os.makedirs(os.path.dirname(name))
    except OSError:
      if not os.path.isdir(name):
        continue

  f = open(str(name),"w")
  f.write(text)
  f.close()
  #call(["git","init"])
  #call(["git","add", "."])
  #call(["git", "commit", "-a", "-m", """ + str(version)+str(comment) + """, "--date= ", time, "--author=", githubID[author])
    # Moin Moin Wiki is a python extension

  

