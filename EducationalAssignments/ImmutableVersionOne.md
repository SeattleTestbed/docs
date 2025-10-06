# Implement a Defensive Security System


This assignment will help you understand security mechanisms. You will be guided through the steps of creating a reference monitor using the security layer functionality in Repy V2.  A reference monitor is an access control concept that refers to an abstract machine that mediates all access to objects by subjects. This can be used to allow, deny, or change the behavior of any set of calls.  


One critical aspect of creating a reference monitor is to ensure it cannot be bypassed and handles all cases correctly. While not a perfect way of validating your reference monitor, it is useful to create test cases to see whether your security layer will work as expected (the test cases may be turned in as part of the next assignment).  


This assignment is intended to reinforce concepts of immutability, access control, and state consistency. By the end, you should understand how to design a security layer that preserves history and enforces tamper resistance.

## Overview

In this assignment, you will implement a defense monitor to enforce immutable, versioned files in Repy. The monitor will enhance the default Repy file behavior by ensuring that once a file version is closed, it can never be modified again, and new versions are created in a controlled, linear order.  
You should write test applications to ensure your reference monitor behaves properly in different cases and to test attacks against your monitor.

## Specifications

1. Your defense monitor should incorporate all the standard file operation methods, from opening a file, reading and writing to it, to closing it.  All operations must behave identically to RepyV2 (without your security layer) except as mentioned below.
2. You can assume that no files exist when your security layer begins running the application.  
3. When a user calls `openfile(filename, True)`, if `filename` already exists,  your security layer must create a new “version” of the file that can be opened.  This version will be given a new version number and must begin with the contents of the latest version file as its contents.
4. Note that a new version cannot be created while the latest version is open. If `openfile()` is called on an already open file, it shall throw the relevant error that it would have done in RepyV2 (`FileInUseError`).
5. Versioned files can be accessed using `openfile(originalfilename + '.v' + str(num), create)`, where `num` starts from 1. If `create=True` is used on a versioned file, raise `RepyArgumentError("Cannot create explicit version files")`, as manual version creation is not allowed.
6. As is the case in normal RepyV2, if an `openfile` call with `create=False`, open the file only if that version exists; otherwise, raise `FileNotFoundError`.
7. Reading from older versions is always allowed, but writing to them is permanently disallowed.  Any attempt to write to an older version should raise a `FileInUseError`.
8. File deletion (`removefile`) is not allowed for any file. Any attempt must raise a `RepyArgumentError`.
9. The `listfiles()` call in RepyV2 should not show that versions of files exist.  It should just show the listing of all files that were created, regardless of how many versions of those file exist.

## Three Design Paradigms

As in earlier assignments, three paradigms are at work:

- **Accuracy:** The defense monitor should precisely and consistently manage file operations. All unspecified actions must behave exactly as in the underlying API.  
- **Efficiency:** The security layer should use minimal resources. Do not cache or copy entire files in memory—only copy when creating a new version.  
- **Security:** The defense layer should be robust against tampering and circumvention. Attackers must not be able to bypass, disable, or exploit the defense monitor’s enhanced behaviors, ensuring that immutability and versioning are always enforced as intended.

## Getting Python and RepyV2

Please refer to the [SeattleTestbed Build
Instructions](../Contributing/BuildInstructions.md#prerequisites) for details.  

Once you have built RepyV2 into a directory of your choice, change into that directory. Use the command below in order to run your RepyV2 applications:

```bash
python2 repy.py restrictions.default encasementlib.r2py [security_layer].r2py [application].r2py
```

(Replace `[security_layer].r2py` and `[application].r2py` by the names of the security layers and application that you want to run.)

In order to test whether or not these steps worked, please copy and paste the code found below for the sample security layer and sample attack.  

You should not get any errors (or outputs) when running the test. If not, please go through the troubleshooting section found below.

### Troubleshooting Repy code
---

If you can't get Repy files to run, some of the following common errors may have occurred:

- **using `print` instead of `log`:**  
  Repy is a subset of Python, but its syntax is slightly different. For example, Python's `print` statement cannot be used; Repy has `log` for that. For a full list of acceptable syntax please see  
  <https://github.com/SeattleTestbed/docs/blob/master/Programming/RepyV2API.md>

- **command line errors:**

  **files are missing:** In the above command line call, you must have `repy.py`, `restrictions.default`, `encasementlib.r2py`, the security layer and the program you want to run in the current working directory. If any or all of the above files are not in that directory then you will not be able to run repy files.

### Tutorials for Repy and Python
----

Now that you have Repy and Python, you may need a refresher on how to use them.
The following tutorials provide this information.

 * Official [Python tutorial](http://docs.python.org/tutorial/)
 * [Differences between RepyV2 and Python](../Programming/PythonVsRepyV2.md)
 * List of [RepyV2 API calls](../Programming/RepyV2API.md)

## Building the security layer   
------

The following program is a sample security layer, it is not complete and does not handle all cases required by the API. Remember, you have no idea how the attacker will try to penetrate your security layer, so it is important that you leave nothing to chance!

#### A basic (and inadequate) defense

Time to start coding! Let's inspect a basic security layer. You can use the code given below as a template for your reference monitor.  
You may save the file as `reference_monitor_[netid].r2py`.

```py
"""
This security layer inadequately handles the Versioned and Immutable functionality

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


class VMFile():
    def __init__(self, filename, create):
        if create:
            self.VMfile = openfile(filename, True)
        else:
            self.VMfile = openfile(filename, False)

    def readat(self, num_bytes, offset):
        return self.VMfile.readat(num_bytes, offset)

    def writeat(self, data, offset):
        return self.VMfile.writeat(data, offset)

    def close(self):
        return self.VMfile.close()


def LPopenfile(filename, create):
    return VMFile(filename, create)

def LPremovefile(filename):
    removefile(filename)

def LPlistfiles():
    return listfiles()


# The code below sets up type checking and variable hiding for you.
# You should not change anything below this point.
sec_file_def = {
    "obj-type": VMFile,
    "name": "VMFile",
    "writeat": {"type": "func", "args": (str, (int, long)), "exceptions": Exception, "return": (int, type(None)), "target": VMFile.writeat},
    "readat": {"type": "func", "args": ((int, long, type(None)), (int, long)), "exceptions": Exception, "return": str, "target": VMFile.readat},
    "close": {"type": "func", "args": None, "exceptions": Exception, "return": (bool, type(None)), "target": VMFile.close}
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

CHILD_CONTEXT_DEF["listfiles"] = {
    TYPE: FUNC,
    ARGS: None,
    EXCP: Exception,
    RETURN: [str],
    TARGET: LPlistfiles
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
# --- Create first version of "testfile" ---
# Calling openfile with create=True should create a new version.
f1 = openfile("testfile", True)

# Write initial content at offset 0.
f1.writeat("HelloWorld", 0)

# Close the file to finalize the first version's contents.
f1.close()

# --- Create second version of "testfile"  ---
# Calling openfile again with create=True should create the next version, and copy the previous version's contents into the new version.
f2 = openfile("testfile", True)

# Read the entire file from offset 0 (pass None to read the whole file) and verify the copy occurred.
assert f2.readat(None, 0) == "HelloWorld"

# Close v2.
f2.close()
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

* Your task is to implement the reference monitor to try to account for all scenarios implied by the given specifications.

* **Never raise unexpected errors or produce any output.**  Your reference monitor must
produce no output when run normally, with a valid attack case. Make sure that you remove any `log()` statements used for debugging before submission.