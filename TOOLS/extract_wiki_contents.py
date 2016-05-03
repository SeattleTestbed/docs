"""
Extract wiki contents from a Trac database, and `pickle` parts 
of them for later usage.

Thanks to https://gist.github.com/sgk/1286682 for the code!
"""
import sqlite3
import pickle

SQL = '''
  select
      name, version, time, author, text, comment
    from
      wiki w
'''

conn = sqlite3.connect('trac.db')
result = conn.execute(SQL)
outfile = open("trac_wiki_dump.pickle", "wb")
outlist = []
for line in result:
  outlist.append(line)

pickle.dump(outlist, outfile)
outfile.close()

