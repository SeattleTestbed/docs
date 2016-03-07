import pickle
from subprocess import call
import os

githubID = {'enchl': ' <>', 'imcheng': ' <>', 'sal': ' <>', 'vivekdesai_22': ' <>', 'justinc': 'JustinCappos <>', 'anuhya': ' <>', 'jchilton': ' <>', 'cosminb': ' <>', 'asekine': ' <>', 'sjs25': ' <>', 'jenn': ' <>', 'alpers': ' <>', 'savvas': ' <>', 'peter': ' <>', 'yemuru': ' <>', 'alexjh': ' <>', 'shawiz': ' <>', 'jchen': ' <>', 'richard': ' <>', 'kon': ' <>', 'pheitt': ' <>', 'gessiou': ' <>', 'rishi': ' <>', 'sushant': ' <>', 'aditi': ' <>', 'couvb': ' <>', 'shurui': ' <>', 'jeffra45': ' <>', 'armon': 'armon <>', 'sportzer': ' <>', 'ericms': ' <>', 'linda': ' <>', 'choksi81': 'choksi81 <>', 'mitchellh': ' <>', 'sabiha': ' <>', 'vlad': ' <>', 'tania': ' <>', 'ivan2': ' <>', 'alanloh': ' <>', 'kimbrl': ' <>', 'cmatthew': ' <>', 'hdanny': ' <>', 'jaehong': ' <>', 'us341': 'us341 <>', 'aman': ' <>', 'albert': 'aaaaalbert <>', 'lukasp': ' <>', 'sojc701': ' <>', 'sebass63': ' <>', 'leonwlaw': 'linkleonard <>', 'evan': ' <>', 'butaud': ' <>', 'jsamuel': ' <>', 'anthony': ' <>', 'tc1466': ' <>', 'sebastien': 'awwad <>', 'yanyan': ' <>', 'trac': ' <>', 'nitin': ' <>', 'jflat06': ' <>', 'yskhoo': ' <>', 'MikeMosh': ' <>', 'cemeyer': ' <>', 'pankhuri': ' <>', 'xuefenghuang': ' <>', 'zackrb': ' <>', 'ivan': 'bestchai <>', 'gpress': ' <>', 'monzum': ' <>', 'shoosh': ' <>', 'vjeko': ' <>', 'mkaplan': ' <>'}
wiki_records_list = pickle.load(file("trac_wiki_dump.pickle"))
#how will I know that the UNIX time sort works?
wiki_records_list.sort(key = lambda row: row[2])

for i in wiki_records_list:
  #print str(i) + "\n"
  name = i[0].encode('utf8')
  version = i[1]
  time = i[2]
  #time = i[2]
  author = i[3]
  text = i[4].encode('utf8')
  comment = i[5]
  if not os.path.exists(os.path.dirname(name)):
    try:
      os.makedirs(os.path.dirname(name))
    except OSError:
      if not os.path.isdir(name):
        continue

  f = open(str(name) + str(version) + ".wiki", "w")
  f.write(text)
  f.close()
  
  call(["git","add", str(name) + str(version) + ".wiki"])
  call(["git", "commit", "-m" + str(version) + " " + str(comment), "--date=" + str(time), "--author=" + str(githubID[author])])
  call(["git", "push", "origin","master"])
    # Moin Moin Wiki is a python  and Ivan

  

