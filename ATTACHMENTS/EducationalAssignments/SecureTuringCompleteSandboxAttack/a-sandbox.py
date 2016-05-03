# This sandbox will only execute programs that contain the following characters
allowedchars= "a0123456789=-*/+!<>:() \n\"A"  
# When it finishes, it will print whatever is in the variable a

import sys


programtext = open('a').read()
for char in programtext:
  if char not in allowedchars:
    print "Error, not an 'a' program!"
    sys.exit(1)

programtext = programtext.replace("A0", "while")

a=None
A = {'A':str}
exec(programtext) in A
print A['a']

