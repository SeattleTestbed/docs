# Fixing your security layer

In this assignment you will analyze the bugs in your security layer from [Part
One](./ImmutableVersionOne.md)
and fix them.  You may want to use test cases from [Part
Two](./ImmutableVersionTwo.md)
to help identify these bugs.  


## Overview

In this assignment you are fixing your reference monitor.  You have been given a
bunch of test programs that try to compromise your reference monitor.  Your job
will be to determine where your reference monitor failed, and fix it to ensure
an attacker cannot circumvent the security layer.

##  Code Analysis 

Given below is a section taken from the sample reference monitor given
in [Part One](./ImmutableVersionOne.md#a-basic-and-inadequate-defense).

```py
class VMFile():
    def __init__(self, filename, create):
    # globals
    # If a file with the same 'filename' already exists, this creates a new version 'filename.v1'.
    # (Incomplete: does not handle further versions like v2, v3, etc.)
        if create:
            if filename in listfiles():
                # File exists → create version 1
                # bug ?
                prev_file = openfile(filename, False)
                content = prev_file.readat(None, 0)

                new_name = filename + ".v1"
                self.VMfile = openfile(new_name, True)
                self.VMfile.writeat(content, 0)
            else:
                # File doesn't exist → create filename
                # bug ?
                self.VMfile = openfile(filename, True)
        else:
            # Open existing file normally
            self.VMfile = openfile(filename, False)

    def readat(self, num_bytes, offset):
        # bug ?
        return self.VMfile.readat(num_bytes, offset)

    def writeat(self, data, offset):
        # bug ?
        return self.VMfile.writeat(data, offset)

    def close(self):
        return self.VMfile.close()


def LPopenfile(filename, create):
    # bug ?
    return VMFile(filename, create)

def LPremovefile(filename):
    removefile(filename)

def LPlistfiles():
    # bug ?
    return listfiles()
```

Let's analyze some of the bugs in this implementation (not in any specific order).

1. As outlined in the specifications in [PartOne](./ImmutableVersionOne.md), if the openfile() is called on an already open file, then the relevant error (`FileInUseError`) must be thrown. This scenario is not correctly handled in the sample implementation.

2. Similarly, if the create=True is used on a versioned file, it should raise RepyArgumentError("Cannot create explicit version files"), as manual version creation is not allowed.

3. The reference monitor needs to track the state of the information on disk, but cannot re-read it for every access (due to efficiency concerns). A common mistake is when the attacker can cause the reference monitor’s state to diverge from the underlying system’s state, especially in error conditions. The reference monitor and disk's states should be in sync.

4. Race conditions and Time-of-check-to-time-of-use (TOCTTOU) issues are frequent oversights. Attackers may exploit timing gaps between checks and operations to corrupts state or bypass restrictions. Such bugs can cause inconsistencies or even infinite loops in the reference monitor.

5. Some reference monitors inappropriately share state for different files. An attacker may be able to exploit this and cause security and accuracy issues.

6. Many reference monitors had accuracy or security bugs as a result of not properly following the instructions.

7. Finally, this example doesn't use locks, which makes it vulnerable to multi-threaded race conditions - effectively the same root cause as TOCTTOU problems but arising from concurrent access.


## What to turn in?

* Submit 2 files:
  1. 1 r2py file: Your reference monitor should be named as `reference_monitor_[netid].r2py` with all
letters in lowercase . For example, if your netid is `abc123`, the file should be named: `reference_monitor_abc123.r2py`.
  2. 1 pdf file: Write up a 1 page report explaining the rationale behind the vulnerabilities and how you fixed them. Name it `[netid].pdf`.

* **Never raise unexpected errors or produce any output.**  Your reference monitor must
produce no output when run normally, with a valid attack case. Make sure that you remove any `log()` statements used for debugging before submission.

* You are required to modify your reference monitor so that it generates no output (logs or errors) when any valid attack case (from Part 2.2, after invalid attack cases have been identified and excluded) is executed against it.
