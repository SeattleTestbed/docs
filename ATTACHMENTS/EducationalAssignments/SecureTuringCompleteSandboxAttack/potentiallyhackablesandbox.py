import sys

filedata = open('simple.file','rb').read()


def safecall(programdata):
  BAD_STRINGS = ['import', 'globals', 'class']

  for badstring in BAD_STRINGS:
    if badstring in programdata:
      print 'Error, cannot have "'+badstring+'" in program.'
      sys.exit(1)
    

  newbuiltins = {'None':None, 'False':False, 'True':True, 'range':range, '__builtins__':None, 'safecall':safecall}

  exec programdata in newbuiltins

safecall(filedata)
