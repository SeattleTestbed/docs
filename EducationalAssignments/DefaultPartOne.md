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
support for a default file to be used when files are opened without creating them first. 
This defense monitor will ensure that software follows certain rules and guidelines, preventing potential unauthorized actions.

You should write test applications to ensure your reference monitor behaves
properly in different cases and to test attacks against your monitor.    


### Specifications:

1. Your defense monitor should incorporate all the standard file operation methods, from opening a file, reading and writing to it, to closing and deleting it. 

2. In addition, if a specially named file - `default` - exists, it shall be used as a template when opening files without creating them first.
Eg: Calling `openfile('foo', True)` should create and open a new empty file called `foo` (assuming it's not present already). However, calling `openfile('foo', False)` should create a new file using `default` as the template. If `default` doesn't exist, throw the relevant error (`FileNotFoundError`).

3. If default is created, written to, or deleted, then all closed files that were previously created gets deleted. Any files that are already open must be left unchanged.

Three design paradigms are at work in this assignment: accuracy, efficiency, and
security.

* Accuracy: The defense monitor should precisely and consistently manage file
operations. Only specific operations, such as `openfile()`, should have their
behavior modified. All situations that are not described above *must* match that
of the underlying API.

* Efficiency: The security layer should use a minimum number of resources, so
performance is not compromised. For example, it is not permissible to store the 
contents of `default` in memory all the time. However, this is allowed when you're
copying the contents of default to a new file.

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

You should not get any errors (or outputs) when running the test.  If not, please go
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
You can use the code given below as a template for your reference monitor.

You may save the file as `reference_monitor_[netid].r2py`.

```py
"""
This security layer inadequately handles the default functionality

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

        if create == False and 'default' in listfiles():
            default_file = openfile('default', False)
            content = default_file.readat(None, 0) # Read from the file using the sandbox's readat
            self.LPfile = openfile(filename, True)
            self.LPfile.writeat(content, 0)
            default_file.close()
        else:
            self.LPfile = openfile(filename, create)

    def readat(self, num_bytes, offset):
        return self.LPfile.readat(num_bytes, offset)

    def writeat(self, data, offset):
        self.LPfile.writeat(data, offset)

    def close(self):
        self.LPfile.close()
        
def LPopenfile(filename, create):
    return LPFile(filename, create)

def LPremovefile(filename):
    removefile(filename) 


# The code below sets up type checking and variable hiding for you.
# You should not change anything below this point.
sec_file_def = {
    "obj-type": LPFile,
    "name": "LPFile",
    "writeat": {"type": "func", "args": (str, (int, long)), "exceptions": Exception, "return": (int, type(None)), "target": LPFile.writeat},
    "readat": {"type": "func", "args": ((int, long, type(None)), (int, long)), "exceptions": Exception, "return": str, "target": LPFile.readat},
    "close": {"type": "func", "args": None, "exceptions": Exception, "return": (bool, type(None)), "target": LPFile.close}
}

CHILD_CONTEXT_DEF["openfile"] = {
    TYPE: OBJC,
    ARGS: (str, bool),
    EXCP: Exception,
    RETURN: sec_file_def,
    TARGET: LPopenfile
}

CHILD_CONTEXT_DEF["removefile"] = {
    TYPE: FUNC,
    ARGS: (str,),
    EXCP: Exception,
    RETURN: type(None),
    TARGET: LPremovefile
}

# Execute the user code
secure_dispatch_module()
```


### Testing your security layer

In this part of the assignment you will pretend to be an attacker. Remember the
attacker's objective is to bypass the restrictions or cause the security
layer to act in a disallowed manner. By understanding how the attacker thinks,
you will be able to write better security layers.  

A valid attack case is found below. 

You may save the file as `[netid]_attackcase.r2py`.

```py
# Clean up if the files exist
if "default" in listfiles():
  removefile("default")
if "testfile.txt" in listfiles():
    removefile("testfile.txt")

# Create a default file
default = openfile("default", True)

# Initial write to default
default.writeat("TEMPLATE", 0)

# Close default
default.close()

# Open a file that doesn't exist
myfile = openfile("testfile.txt", False)

# Read from the file. 
# Passing None as first argument indicates that we want to read the whole file from offset 0.
assert myfile.readat(None, 0) == "TEMPLATE"

# Close the file
myfile.close()
```

The given defense layer should not output any errors when used with this simple attack case.
However, you need to modify the reference monitor and the attack case to account for any possible scenario.

**Note:** All attacks should be written as Repy V2 files, using the `.r2py` extension.


### Choice of File Names

Filenames may only be in the current directory and may only contain lowercase
letters, numbers, the hyphen, underscore, and period characters. Also, filenames
cannot be '.', '..', the blank string or start with a period. There is no
concept of a directory or a folder in repy. Filenames must be no more than 120
characters long.


### Running your security layer

Finally, type the following command at the terminal to run your security layer
with your attack program.

```bash
python repy.py restrictions.default encasementlib.r2py reference_monitor_[netid].r2py [netid]_attackcase.r2py
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


# What to turn in ?

* Turn in a single repy file called `reference_monitor_[netid].r2py` with all
letters in lowercase. If your net id is abcd123, then the file you upload must be named `reference_monitor_abcd123.r2py`.

* Your task is to implement the reference monitor to try to account for all scenarios implied by the given [Specifications](#specifications).

* **Never raise unexpected errors or produce any output.**  Your reference monitor must
produce no output when run normally, with a valid attack case. Make sure that you remove any `log()` statements used for debugging before submission.

