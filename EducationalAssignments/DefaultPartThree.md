# Fixing your security layer

In this assignment you will analyze the bugs in your security layer from [Part
One](./DefaultPartOne.md)
and fix them.  You may want to use test cases from [Part
Two](./DefaultPartTwo.md)
to help identify these bugs.  


## Overview

In this assignment you are fixing your reference monitor.  You have been given a
bunch of test programs that try to compromise your reference monitor.  Your job
will be to determine where your reference monitor failed, and fix it to ensure
an attacker cannot circumvent the security layer.

##  Code Analysis 

Given below is a section taken from the sample reference monitor given
in [Part One](./DefaultPartOne.md#a-basic-and-inadequate-defense).

```py
class LPFile():
  def __init__(self, filename, create):
    # globals
    mycontext['debug'] = False

    if create == False and 'default' in listfiles():
      # bug ?
      default_file = openfile('default', False)
      content = default_file.readat(None, 0) 
      self.LPfile = openfile(filename, True)
      self.LPfile.writeat(content, 0)
      default_file.close()
    else:
      # bug ?
      self.LPfile = openfile(filename, create)

  def readat(self, num_bytes, offset):
    return self.LPfile.readat(num_bytes, offset)

  def writeat(self, data, offset):
    # bug ?
    self.LPfile.writeat(data, offset)

  def close(self):
    # bug ?
    self.LPfile.close()
        
def LPopenfile(filename, create):
  return LPFile(filename, create)

def LPremovefile(filename):
  # bug ?
  removefile(filename) 
```

Let's analyze some of the bugs in this implementation (not in any specific order).

1. As outlined in the specifications in [PartOne](./DefaultPartOne.md), if the `default` file is absent,
and we try to open a non-existent file with create=False, then the relevant 
error (`FileNotFoundError`) must be thrown. This scenario is not correctly handled in the sample implementation.

2. Similarly, if the `default` file is modified (created/written to/deleted), then we need to delete all files that were created 
during the run and are not open at the moment of modification. To achieve this, the state of all (open) files created during the 
run should be tracked. You can use the global variable `mycontext` to store this state. For efficiency, only filenames or 
file handles should be stored, rather than the actual file contents.

3. One common edge case often overlooked by students occurs when attempting to open a non-existent file with 
create=False while default is already open. If it's not handled correctly, this will cause a FileInUseError, which 
shouldn't happen. To prevent this, the reference monitor should maintain a reference to the file handle of default, 
whenever default is open (so that it can be used to create new templates). Also note that storing the contents of default 
in memory at all times is not an optimal solution due to efficiency concerns.

4. Finally, this example doesn't use locks, which can lead to race conditions, thus allowing various types of multi-threading attacks.


## What to turn in?

* Submit 2 files:
  1. 1 r2py file: Your reference monitor should be named as `reference_monitor_[netid].r2py` with all
letters in lowercase . For example, if your netid is `abc123`, the file should be named: `reference_monitor_abc123.r2py`.
  2. 1 pdf file: Write up a 1 page report explaining the rationale behind the vulnerabilities and how you fixed them. Name it `[netid].pdf`.

* **Never raise unexpected errors or produce any output.**  Your reference monitor must
produce no output when run normally, with a valid attack case. Make sure that you remove any `log()` statements used for debugging before submission.

* You are required to modify your reference monitor so that it generates no output (logs or errors) when any valid attack case (from Part 2.2, after invalid attack cases have been identified and excluded) is executed against it.
