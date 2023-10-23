# Fixing your security layer

In this assignment you will analyze the bugs in your security layer from [Part
One](https://github.com/SeattleTestbed/docs/blob/master/EducationalAssignments/UndoPartOne.md)
and fix them.  You may want to use test cases from [Part
Two](https://github.com/SeattleTestbed/docs/blob/master/EducationalAssignments/UndoPartTwo.md)
to help identify these bugs.  


## Overview

In this assignment you are fixing your reference monitor.  You have been given a
bunch of test programs that try to compromise your reference monitor.  Your job
will be to determine where your reference monitor failed, and fix it to ensure
an attacker cannot circumvent the security layer.


## Common Bugs

 * The reference monitor needs to track the state of the information on disk,
   but cannot re-read it for every access (due to efficiency concerns). A common
   mistake is when the attacker can cause the reference monitor’s state to
   diverge from the underlying system’s state, especially in error conditions.

 * Time-of-check-to-time-of-use (TOCTTOU) bugs and other types of race
   conditions are a fairly common oversight for students. Some students write
   test cases that attempt to trigger a race condition to exploit these
   problems. This can result in essentially any sort of attack, even infinite
   loops in the reference monitor in some cases.

 * Some reference monitors inappropriately share state for different files. For
   example, there may be a global set of state that is used to store the first
   two bytes. By opening multiple files, an attacker may be able to overwrite
   this state and cause security and accuracy issues.

 * In rare cases, a student’s reference monitor may inappropriately retain state
   for a file. For example, an attacker may create a file, write some data, then
   close and delete the file. If the attacker recreates a file with the same
   name, the state should be cleared.

 * Many reference monitors had accuracy or security bugs as a result of not
   properly following the instructions.


## Example : Sample Implementation 

```py
class LPFile():
    def __init__(self, filename, create):
        # globals
        mycontext['debug'] = False
        self.LPfile = openfile(filename, create)
        self.pending_data = None
        self.pending_offset = None

    def readat(self, bytes, offset):
        # Read from the file using the sandbox's readat...
        return self.LPfile.readat(bytes, offset)

    def writeat(self, data, offset):
        # bug ?
        self.LPfile.writeat(self.pending_data, self.pending_offset)
        self.pending_data = data
        self.pending_offset = offset

    def undo(self):
        # bug ?
        self.pending_data = None
        self.pending_offset = None

    def close(self):
        # bug ?
        self.LPfile.close()
```

### Code Analysis

Let's analyze some of the bugs in this implementation.

According to the specifications in [Part
One](https://github.com/SeattleTestbed/docs/blob/master/EducationalAssignments/UndoPartOne.md),
the `writeat` function is designed to work such that the provided data is not
immediately written to the file. Instead, it should be stored in a "pending"
state. Here, the `writeat` writes to the file immediately without any form of
delay. Another bug is that on closing the file, the function doesn't check or
commit any `pending_data` to the file. Thus, if there was any `pending_data`
from the last `writeat` operation, it will be lost and not written to the file.

There's no error handling for scenarios like writing with a negative offset,
writing beyond the end of the file, etc. Such error checks are essential to
prevent data corruption and unexpected behavior. Furthermore, there's no
mechanism to update or manage the current length of the file. This can cause
problems, especially if you're trying to prevent writing beyond the end of the
file or if you're trying to append data correctly. Moreover, this example
doesn't use any locks so you can introduce race conditions and perform a variety
of attacks. 


## What to turn in?

 * Never raise unexpected errors or produce any output. Your program must
   produce no output when run normally.
 * Turn in the reference monitor that you have fixed.  The name of the reference
monitor should be in the form of `reference_monitor_[ netid ].r2py`. All letters
must be lowercase.
