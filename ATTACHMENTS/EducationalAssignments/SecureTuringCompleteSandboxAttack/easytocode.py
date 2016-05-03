# Author: Justin Cappos
# Purpose: silly little python secure VM (attempt).   This is meant to be fast 
# for me to code.   

# I'm just going to read this in, replace the globals / locals so they are 
# (almost) blank and strip out anything I can think might be an issue

import sys
filedata = open('silly.input','rb').read()
 
FORBIDDEN_STRINGS = ['import', '.', '_', 'class', '>>', 'exec', 'assert','@','lambda','<<','slice','yield','try','except','global']

for forbidden_string in FORBIDDEN_STRINGS:
  if forbidden_string in filedata:
    print 'Cannot have "'+forbidden_string+'" in program.'
    sys.exit(1)

namespace = {}
namespace['__builtins__'] = {'False':False, 'True':True, 'None':None}

exec filedata in namespace
