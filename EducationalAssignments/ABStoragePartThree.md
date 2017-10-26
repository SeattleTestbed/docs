
# Fixing your security layer

In this assignment you will analyze the bugs in your security layer from [[Part One](ABStoragePartOne.md)] and fix them.  You may want to use test cases from [Part Two](ABStoragePartTwo.md) to help identify these bugs.  Finally, you will write a report discussing the different classes of bugs that your code had, and why.




## Overview
----
In this assignment you are fixing your reference monitor.  You have been sent a bunch of test programs that try to compromise your reference monitor.  Your job will be to determine where your reference monitor failed, and fix it to ensure an attacker cannot circumvent the security layer.



## Common Bugs
 * The reference monitor needs to track the state of the information on disk, but cannot re-read it for every access (due to efficiency concerns). A common mistake is when the attacker can cause the reference monitor’s state to diverge from the underlying system’s state, especially in error conditions. For example, if the program attempts to write past the end of a file (or before the beginning of a file), the reference monitor may incorrectly update its state. As a result, the reference monitor will improperly block or allow writes since the disk contents differ. This can cause both security and accuracy issues.

 * Time-of-check-to-time-of-use (TOCTTOU) bugs and other types of race conditions are a fairly common oversight for students. Some students write test cases that attempt to trigger a race condition to exploit these problems. This can result in essentially any sort of attack, even infinite loops in the reference monitor in some cases.

 * Some reference monitors inappropriately share state for different files. For example, there may be a global set of state that is used to store the first two bytes. By opening multiple files, an attacker may be able to overwrite this state and cause security and accuracy issues.

 * In rare cases, a student’s reference monitor may inappropriately retain state for a file. For example, an attacker may create a file, write some data, then close and delete the file. If the attacker recreates a file with the same name, the state should be cleared.

 * Many reference monitors had accuracy or security bugs as a result of not properly following the instructions.  



## Case 1: Sample implementation of the close function

```
def close(self):
  self.Afile.close()
  self.Bfile.close()
```

### Code Analysis
Let's analyze one of the bugs in this implementation.  According to the specifications in [Part One](ABStoragePartOne.md), When close() is called on the file, if a file is not valid, it is discarded. If both files are valid, the older one is discarded. In the code above, there exists no logic to verify the content of the file and perform validation. Further file read would lead to the invalid file being read or valid file being written to. This is a security issue.

## Case 2: Sample implementation of the open call - initialize function - False flag

```
if create:
  self.Afile = openfile(self.Afn,create)
  self.Bfile = openfile(self.Bfn,create)
  self.Afile.writeat('SE',0)
```

### Code Analysis
Let's analyze one of the bugs in this implementation.  According to the specifications in [Part One](ABStoragePartOne.md), Any valid operation should not be blocked. When open() is called with flag False, it should be handled. In the code above, there exists no logic to perform file open with flag False. Further file read/write would lead to error thrown as the file handle would not be created. This is an accuracy issue.

## Case 3: Sample implementation of the open call - initialize function - New file 'SE' write

Similarly, when flag is True and the file exists already (Flag would be ignored, look at Repy documentation), every time 'SE' write would be performed to a already existing file. This behavior does not abide to the rules mentioned where 'SE' write should happen only to a file that did not exist before.


## What to turn in?
----

 * Turn in the reference monitor that you have fixed.  The name of the reference monitor should be in the form of reference_monitor_[poly_username].r2py
e.g. reference_monitor_jcappos.r2py
All letters must be lowercase.
 * In addition to your reference monitor, submit a one-page PDF document, in which you discuss the different classes of bugs you had in your reference monitors and why.
What kind of bug did you experience, what caused the bug, and what did you do to fix it?
