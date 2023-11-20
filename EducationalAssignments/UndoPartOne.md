# Implement a Defensive Security System

This assignment will help you understand security mechanisms. You will be guided
through the steps of creating a reference monitor using the security layer
functionality in Repy V2. A reference monitor is an access control concept that
refers to an abstract machine that mediates all access to objects by subjects.
This can be used to allow, deny, or change the behavior of any set of calls.
While not a perfect way of validating your reference monitor, it is useful to
create test cases to see whether your security layer will work as expected (the
test cases may be turned in as part of the next assignment). 

This assignment is intended to reinforce concepts about access control and
reference monitors in a hands-on manner. 


## Overview

In this assignment, you will implement a defense monitor to oversee file
operations in Repy. The monitor will enhance the default Repy behavior by adding
an undo functionality for writes. This defense monitor will ensure that software
follows certain rules and guidelines, preventing potential unauthorized actions.

The focus is on monitoring file write operations and allowing the last write to
be reverted. This undo capability mimics common document editors that let you
reverse your most recent edit.

You should write test applications to ensure your reference monitor behaves
properly in different cases and to test attacks against your monitor.    


### Specifications:

1. Your defense monitor should incorporate all the standard file operation
   methods, with an added method named `undo`.
2. A `writeat` operation will not immediately write its changes to the file. The
   changes will only be permanent (commit) after either of the following occur:
    - A subsequent valid `writeat` operation is executed.
    - The file is closed.
3. The `undo` operation will reverse the changes of the last valid `writeat`
   operation, making it as if it didn't happen. It's crucial to note that only
   the most recent operation can be undone. If there haven't been any `writeat`
   operations, the `undo` has no effect. If several `writeat` operations are
   consecutively executed, only the changes from the last valid `writeat` can be
   undone.
4. Aside from the ability to be undone and potentially delayed writes, all
   `writeat` operations should behave the same way as they do in the RepyV2 API.
   You are expected to keep track of the offset, to make sure the attack is not
   writing past the EOF.
5. The `undo` operation raises `FileClosedError` if the file is already closed.
6. The `readat` cannot read data that has not been committed to the file.

Three design paradigms are at work in this assignment: accuracy, efficiency, and
security.

 * Accuracy: The defense monitor should precisely and consistently manage file
operations. Only specific operations, such as `writeat`, should have their
behavior modified. All situations that are not described above *must* match that
of the underlying API.

 * Efficiency: The security layer should use a minimum number of resources, so
performance is not compromised.  For example, you may not call `readat()`
everytime `writeat()` is called.  It is permissable to call `readat()` upon
`fileopen()`, however.

 * Security: The defense layer should be robust against tampering and
circumvention. Attackers must not be able to bypass, disable, or exploit the
defense monitor's enhanced behaviors, ensuring the integrity and intended
functionality of file operations.


### Getting Python and RepyV2

Please refer to the [SeattleTestbed Build
Instructions](../Contributing/BuildInstructions.md#prerequisites) for details.

Once you have built RepyV2 into a directory of your choice, change into that
directory. Use the command below in order to run your RepyV2 applications:

```bash
python2 repy.py restrictions.default encasementlib.r2py [security_layer].r2py [application].r2py
```

(Replace `[security_layer].r2py` and `[application].r2py` by the names of the
security layers and application that you want to run.) 

In order to test whether or not these steps worked, please copy and paste the
code found below for the sample security layer and sample attack.

You should get an `RepyArgumentError` when running the test.  If not, please go
through the troubleshooting section found below.


### Troubleshooting Repy code

If you can't get Repy files to run, some of the following common errors may have
occurred:

 * using `print` instead of `log`:

Repy is a subset of Python, but its syntax is slightly different.  For example,
Python's `print` statement cannot be used; Repy has `log` for that. For a full
list of acceptable syntax please see
[https://github.com/SeattleTestbed/docs/blob/master/Programming/RepyV2API.md]

 * command line errors:

**files are missing:** In the above command line call, you must have `repy.py`,
restrictions.default, encasementlib.r2py, the security layer and the program you
want to run in the current working directory.  If any or all of the above files
are not in that directory then you will not be able to run repy files.  

<!--
AR: This doesn't apply when building from source or getting the runtime tarball only (it does for clearinghouse downloads).
 * Downloading the wrong version of Seattle:

Seattle is operating system dependent.  If you download the Windows
version, you need to use the Windows command line.  For Windows 7 this is
PowerShell.  You can open a new terminal by going to start, search, type
powershell.  If you downloaded the Linux version you must use a Linux OS
and Linux terminal.  

-->


### Tutorials for Repy and Python

Now that you have Repy and Python, you may need a refresher on how to use them.
The following tutorials provide this information.

 * Official [Python tutorial](http://docs.python.org/tutorial/)
 * [Differences between RepyV2 and Python](../Programming/PythonVsRepyV2.md)
 * List of [RepyV2 API calls](../Programming/RepyV2API.md)


## Building the security layer

The following program is a sample security layer, it is not complete and does
not handle all cases required by the API. Remember, you have no idea how the
attacker will try to penetrate your security layer, so it is important that you
leave nothing to chance!  


### A basic (and inadequate) defense

Time to start coding! Let's inspect a basic security layer.

```py
"""
This security layer inadequately handles the undo functionality

Note:
    This security layer uses encasementlib.r2py, restrictions.default, repy.py and Python
    Also you need to give it an application to run.
    python repy.py restrictions.default encasementlib.r2py [security_layer].r2py [attack_program].r2py 
    
"""
TYPE = "type"
ARGS = "args"
RETURN = "return"
EXCP = "exceptions"
TARGET = "target"
FUNC = "func"
OBJC = "objc"


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
        self.LPfile.writeat(self.pending_data, self.pending_offset)
        self.pending_data = data
        self.pending_offset = offset

    def undo(self):
        self.pending_data = None
        self.pending_offset = None

    def close(self):
        self.LPfile.close()

def LPopenfile(filename, create):
    return LPFile(filename, create)

# The code here sets up type checking and variable hiding for you.
# You should not need to change anything below here.
sec_file_def = {
    "obj-type": LPFile,
    "name": "LPFile",
    "writeat": {"type": "func", "args": (str, (int, long)), "exceptions": Exception, "return": (int, type(None)), "target": LPFile.writeat},
    "readat": {"type": "func", "args": ((int, long, type(None)), (int, long)), "exceptions": Exception, "return": str, "target": LPFile.readat},
    "undo": {"type": "func", "args": None, "exceptions": None, "return": type(None), "target": LPFile.undo},
    "close": {"type": "func", "args": None, "exceptions": Exception, "return": (bool, type(None)), "target": LPFile.close}
}

CHILD_CONTEXT_DEF["openfile"] = {
    TYPE: OBJC,
    ARGS: (str, bool),
    EXCP: Exception,
    RETURN: sec_file_def,
    TARGET: LPopenfile
}

# Execute the user code
secure_dispatch_module()
```


### Testing your security layer

In this part of the assignment you will pretend to be an attacker. Remember the
attacker's objective is to bypass the A/B restrictions or cause the security
layer to act in a disallowed manner. By understanding how the attacker thinks,
you will be able to write better security layers.  

An example of an attack is found below:

```py
# clean up if the file exists.
if "testfile.txt" in listfiles():
  removefile("testfile.txt")

# create a file
myfile=openfile("testfile.txt",True)

# intial write to the file
myfile.writeat("12345678",0)

# attempt to overwrite the beginning of the file
myfile.writeat("Hi!",0) 

# now, undo the previous write
myfile.undo()

# the contents should still be "12345678" as the overwrite was undone
assert("12345678" == myfile.readat(8,0))

# close the file
myfile.close()
```

If the reference monitor is correct, there should be no `RepyArgumentError`.

**Note:** All attacks should be written as Repy V2 files, using the `.r2py`
extension.


### Choice of File Names

Filenames may only be in the current directory and may only contain lowercase
letters, numbers, the hyphen, underscore, and period characters. Also, filenames
cannot be '.', '..', the blank string or start with a period. There is no
concept of a directory or a folder in repy. Filenames must be no more than 120
characters long.


### Running your security layer

Finally, type the following commands at the terminal to run your security layer
with your attack program

```bash
python repy.py restrictions.default encasementlib.r2py [security_layer].r2py [attack_program].r2py
```

Make sure you went through the "How to get RepyV2" section!


# Notes and Resources
 
 * For a complete list of syntax in Repyv2 please visit:
    **[https://github.com/SeattleTestbed/docs/blob/master/Programming/RepyV2API.md]**
 
 * The following link is an excellent source for information about security
   layers:
    **[https://ssl.engineering.nyu.edu/papers/cappos_seattle_ccs_10.pdf]**

 * **Note:** It is possible to add multiple security layers to Repy, this may be
useful for testing different mitigations separately.  This is done with the
following command at the terminal:

```bash
python repy.py restrictions.default encasementlib.r2py [security_layer1].r2py [security_layer2].r2py [security_layer3].r2py [program].r2py
```

 * **Your security layer must produce no output!!**

 * In repy log replaces print from python.  This may be helpful when testing if
Repy installed correctly.


# What to turn in?

 * Turn in a repy file called `reference_monitor_[ netid ].r2py` with all
letters in lowercase.

* **Never raise unexpected errors or produce any output.**  Your program must
produce no output when run normally.
