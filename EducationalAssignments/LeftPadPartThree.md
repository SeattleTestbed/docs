
# Fixing your security layer

In this assignment you will analyze the bugs in your security layer from [Part One](https://github.com/SeattleTestbed/docs/blob/master/EducationalAssignments/LeftPadPartOne.md) and fix them.  You may want to use test cases from [Part Two](https://github.com/SeattleTestbed/docs/blob/master/EducationalAssignments/LeftPadPartTwo.md) to help identify these bugs.  Finally, you will write a report discussing the different classes of bugs that your code had, and why.




## Overview
----
In this assignment you are fixing your reference monitor.  You have been sent a bunch of test programs that try to compromise your reference monitor.  Your job will be to determine where your reference monitor failed, and fix it to ensure an attacker cannot circumvent the security layer.



## Common Bugs
 * The reference monitor needs to track the state of the information on disk, but cannot re-read it for every access (due to efficiency concerns). A common mistake is when the attacker can cause the reference monitor’s state to diverge from the underlying system’s state, especially in error conditions. 

 * Time-of-check-to-time-of-use (TOCTTOU) bugs and other types of race conditions are a fairly common oversight for students. Some students write test cases that attempt to trigger a race condition to exploit these problems. This can result in essentially any sort of attack, even infinite loops in the reference monitor in some cases.

 * Some reference monitors inappropriately share state for different files. For example, there may be a global set of state that is used to store the first two bytes. By opening multiple files, an attacker may be able to overwrite this state and cause security and accuracy issues.

 * In rare cases, a student’s reference monitor may inappropriately retain state for a file. For example, an attacker may create a file, write some data, then close and delete the file. If the attacker recreates a file with the same name, the state should be cleared.

 * Many reference monitors had accuracy or security bugs as a result of not properly following the instructions.




## Example : Sample Implementation 

```
class LPFile():
  def __init__(self,filename,create):
    # globals
    mycontext['debug'] = False   
    self.LPfile = openfile(filename,create)
    self.length = 0

  def readat(self, bytes, offset):
    # Read from the file using the sandbox's readat...
    return self.LPfile.readat(bytes, offset)

  def writeat(self,data,offset):
    if not offset == self.length:
      # write the data and update the length (BUG?)
      self.LPfile.writeat(data,offset)
      self.length = offset + len(data)

    else:
    
      if '\n' not in data:
        self.LPfile.writeat(data,offset)
      else: # bug?
        loc = data.find('\n')
        # bug?
        self.LPfile.writeat(data[:loc]+"    "+data[loc:],offset)
```

### Code Analysis
Let's analyze one of the bugs in this implementation.  According to the specifications in [Part One](https://github.com/SeattleTestbed/docs/blob/master/EducationalAssignments/LeftPadPartOne.md), it should return RepyArgumentError if there are two '\n' which isn't implemented in this code, morever, this code inserts spaces before '\n', as a result you can't see the indentation. Another bug is that it should first update the length and write. Furthermore,  this code doesn't check if len(data) is greater than self.length when offset is less then self.length. It also assumes self.lenght = 0 which means that the file would be empty. Moreover, This example doesn't use any locks so you can introduce race conditions and perform a variety of attacks. 


## What to turn in?
----

 * Turn in the reference monitor that you have fixed.  The name of the reference monitor should be in the form of reference_monitor_[netId].r2py
All letters must be lowercase.
