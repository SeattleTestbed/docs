
# Fixing your security layer

In this assignment you will analyze the bugs in your security layer from [[Part One](https://github.com/SeattleTestbed/docs/blob/master/EducationalAssignments/ParityPartOne.md)] and fix them.  You may want to use test cases from [Part Two](https://github.com/SeattleTestbed/docs/blob/master/EducationalAssignments/ParityPartTwo.md) to help identify these bugs.  Finally, you will write a report discussing the different classes of bugs that your code had, and why.




## Overview
----
In this assignment you are fixing your reference monitor.  You have been sent a bunch of test programs that try to compromise your reference monitor.  Your job will be to determine where your reference monitor failed, and fix it to ensure an attacker cannot circumvent the security layer.



## Common Bugs
 * The reference monitor needs to track the state of the information on disk, but cannot re-read it for every access (due to efficiency concerns). A common mistake is when the attacker can cause the reference monitor’s state to diverge from the underlying system’s state, especially in error conditions. For example, if the program attempts to write past the end of a file (or before the beginning of a file), the reference monitor may incorrectly update its state. As a result, the reference monitor will improperly block or allow writes since the disk contents differ. This can cause both security and accuracy issues.

 * Time-of-check-to-time-of-use (TOCTTOU) bugs and other types of race conditions are a fairly common oversight for students. Some students write test cases that attempt to trigger a race condition to exploit these problems. This can result in essentially any sort of attack, even infinite loops in the reference monitor in some cases.

 * Some reference monitors inappropriately share state for different files. For example, there may be a global set of state that is used to store the first two bytes. By opening multiple files, an attacker may be able to overwrite this state and cause security and accuracy issues.

 * In rare cases, a student’s reference monitor may inappropriately retain state for a file. For example, an attacker may create a file, write some data, then close and delete the file. If the attacker recreates a file with the same name, the state should be cleared.

 * Many reference monitors had accuracy or security bugs as a result of not properly following the instructions.
 
 * Most common mistakes were, failing to properly evaluate a block that is partially written and failing to handle multiple writes. 



## Example : Sample implementation of the writeat function

```
def writeat(self,data,offset):
    thisdata = data
    while thisdata:
        eightbytesequence = thisdata[:8]
        thisdata = thisdata[8:]
        even = True
        for thisbyte in eightbytesequence:
          if ord(thisbyte) % 2:
            even = not even
        if even:
          self.file.writeat(eightbytesequence, offset)
        else:
          raise RepyParityError("Non-even parity write to file")
```

### Code Analysis
Let's analyze one of the bugs in this implementation.  According to the specifications in [Part One](https://github.com/SeattleTestbed/docs/blob/master/EducationalAssignments/ParityPartOne.md), if the length of the last block is less than 8, the parity of that block is assumed to be even. But this code does not handle that. Further more, the code does not read any existing data from the file before performing the parity check. This is a security bug and accuracy bug, for reasons, that do not allow writing valid data whose length is less than 8 and failing to evaluate the modified block rather than just the data being written.


## What to turn in?
----

 * Turn in the reference monitor that you have fixed.  The name of the reference monitor should be in the form of reference_monitor_netId.r2py
e.g. reference_monitor_jcappos.r2py
All letters must be lowercase.
 * In addition to your reference monitor, submit a one-page PDF document, in which you discuss the different classes of bugs you had in your reference monitors and why.
What kind of bug did you experience, what caused the bug, and what did you do to fix it?
