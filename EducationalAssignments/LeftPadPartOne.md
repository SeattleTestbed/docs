# Implement a Defensive Security System

This assignment will help you understand security mechanisms. You will be
guided through the steps of creating a reference monitor using the security
layer functionality in Repy V2. A reference monitor is an access control
concept that refers to an abstract machine that mediates all access to
objects by subjects. This can be used to allow, deny, or change the
behavior of any set of calls. While not a perfect way of validating your
reference monitor, it is useful to create test cases to see whether your
security layer will work as expected (the test cases may be turned in as
part of the next assignment). Please ask your instructor if test cases are available to you, some instructors may provide with test cases.

This assignment is intended to reinforce concepts about access control and
reference monitors in a hands-on manner. 




## Overview
----
In this assignment you will create a security layer which will always left indent 
after the '\n' newline character in a write that strictly appends to a file.   By 
"strictly appends", this means the first byte of the write is at the current end 
of file (after the last previously written data).  This is something that is 
sometimes done by a document editors, when they believe you have ended a paragraph.  
For this assignment, the '\n' character is treated as a newline and other characters 
(notably '\r') are not treated specially.

You should write test applications to ensure your reference monitor behaves properly 
in different cases and to test attacks against your monitor.    

#### The Reference Monitor Must:
1. Behave identically to a non-sandboxed program [RepyV2 API calls](../Programming/RepyV2API.md), except:
   * When writing to file using writeat() except when a write strictly appends to a file (as specified 
        in the next step).
   * All other calls (writeat()s that do not strictly append, readat()s, etc.) must be performed as
        they would in a non-sandboxed program!
2. If a writeat() strictly appends to a file, then:
  a. If it contains no '\n', perform the writeat() operation normally (as a non-sandboxed program)
  b. If it contains exactly one '\n' character, then perform a writeat() in the 
     same location, but with four space ' ' characters inserted before the '\n'.
  c. If it contains more than one '\n' character, raise a RepyArgumentError exception
3. Not produce any errors or output for any reason except as mentioned above  
   * Normal operations should not be blocked or produce any output  
   * Invalid operations should not produce any output to the user
4. Call readat() everytime writeat() is called.  This will be too slow and is forbidden.


Three design paradigms are at work in this assignment: accuracy,
efficiency, and security.

 * Accuracy: The security layer should only modify certain operations (a strictly
appending writeat() with one '\n') and raise an exception for certain other 
actions (a strictly appending writeat() with more than one '\n'). All situations 
that are not described above *must* match that of the underlying API.

 * Efficiency: The security layer should use a minimum number of resources,
so performance is not compromised.  For example, you may not call readat() 
everytime writeat() is called.  It is permissable to call readat() upon fileopen(),
however.

 * Security: The attacker should not be able to circumvent the security
layer. For example, if the attacker can cause a non-strictly appending write to
have '    ' inserted before '\n' or can cause the reference monitor to incorrectly
error or hang, then the security is compromised.



### Getting Python and RepyV2

Please refer to the [SeattleTestbed Build Instructions](../Contributing/BuildInstructions.md#prerequisites)
for details.

Once you have built RepyV2 into a directory of your choice, change into that
directory. Use the command below in order to run your RepyV2 applications:

```python2 repy.py restrictions.default encasementlib.r2py [security_layer].r2py [application].r2py```

(Replace '[security_layer].r2py' and '[application].r2py' by the names of the
security layers and application that you want to run.) 

In order to test whether or not these steps worked, please copy and paste
the code found below for the sample security layer and sample attack.

If you got an error, please go through the troubleshooting section found below.

### Troubleshooting Repy code
----
If you can't get Repy files to run, some of the following common errors may
have occurred:

 * using `print` instead of `log`:

Repy is a subset of Python, but its syntax is slightly different.  For
example, Python's `print` statement cannot be used; Repy has `log` for
that. For a full list of acceptable syntax please see
[https://github.com/SeattleTestbed/docs/blob/master/Programming/RepyV2API.md]

 * command line errors:

**files are missing:** In the above command line call, you must have
`repy.py`, restrictions.default, encasementlib.r2py, the security layer and
the program you want to run in the current working directory.  If any or
all of the above files are not in that directory then you will not be able
to run repy files.  

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
----
Now that you have Repy and Python, you may need a refresher on how to use
them.  The following tutorials provide this information.

 * Official [Python tutorial](http://docs.python.org/tutorial/)
 * [Differences between RepyV2 and Python](../Programming/PythonVsRepyV2.md)
 * List of [RepyV2 API calls](../Programming/RepyV2API.md)



## Building the security layer
----
The following program is a sample security layer, it is not complete and does not 
handle all cases required by the API. Remember, you have no idea how the
attacker will try to penetrate your security layer, so it is important that
you leave nothing to chance!  


### A basic (and inadequate) defense

Time to start coding!  Let's inspect a basic security layer.  

```
"""
This security layer inadequately handles LeftPad writeat()s that strictly append



Note:
    This security layer uses encasementlib.r2py, restrictions.default, repy.py and Python
    Also you need to give it an application to run.
    python repy.py restrictions.default encasementlib.r2py [security_layer].r2py [attack_program].r2py 
    
    """ 
TYPE="type"
ARGS="args"
RETURN="return"
EXCP="exceptions"
TARGET="target"
FUNC="func"
OBJC="objc"

class LPFile():
  def __init__(self,filename,create):
    # globals
    mycontext['debug'] = False   
    if create:
      self.LPfile = openfile(self.filename,create)
      self.length = 0


  def writeat(self,data,offset):
    if not offset == self.length:
      # write the data and update the length (BUG?)
      self.LPfile.writeat(data,offset)
      self.length = offset + len(data)

    else:
    
      if '\n' not in data:
        self.writeat(data,offset)
      else: # bug?
        loc = data.find('\n')
        # bug?
        self.writeat(data[:loc]+"    "+data[loc:],offset)

  
  def close(self):
    self.LPfile.close()


def LPopenfile(filename, create):
  return LPFile(filename,create)




# The code here sets up type checking and variable hiding for you.  You
# should not need to change anything below here.
sec_file_def = {"obj-type":LPFile,
                "name":"LPFile",
                "writeat":{"type":"func","args":(str,(int,long)),"exceptions":Exception,"return":(int,type(None)),"target":LPFile.writeat},
                "readat":{"type":"func","args":((int,long,type(None)),(int,long)),"exceptions":Exception,"return":str,"target":LPFile.readat},
                "close":{"type":"func","args":None,"exceptions":None,"return":(bool,type(None)),"target":LPFile.close}
           }

CHILD_CONTEXT_DEF["openfile"] = {TYPE:OBJC,ARGS:(str,bool),EXCP:Exception,RETURN:sec_file_def,TARGET:LPopenfile}

# Execute the user code
secure_dispatch_module()
```



### Testing your security layer
----
In this part of the assignment you will pretend to be an attacker. Remember
the attacker's objective is to bypass the A/B restrictions or cause
the security layer to act in a disallowed manner. By understanding how the
attacker thinks, you will be able to write better security layers.  

An example of an attack is found below:

```
# clean up if the file exists.
if "testfile.txt" in listfiles():
  removefile("testfile.txt")

myfile=openfile("testfile.txt",True)  #Create a file

myfile.writeat("12345678",0) # no difference, no '\n'

myfile.writeat("Hi!",0) # writing early in the file

myfile.writeat("Append!\nShould be indented!!!",8) # strictly appending...

assert(' ' == myfile.readat(None,17)) # this location should contain a space...

#Close the file
myfile.close()


```

If the reference monitor is correct, there should be no assertion failure...

**Note:** All attacks should be written as Repy V2 files, using the .r2py extension.

#### Choice of File Names
----
Filenames may only be in the current directory and may only contain lowercase letters, numbers, the hyphen, underscore, and period characters. Also, filenames cannot be '.', '..', the blank string or start with a period. There is no concept of a directory or a folder in repy. Filenames must be no more than 120 characters long.

### Running your security layer
----
Finally, type the following commands at the terminal to run your security
layer with your attack program

```python repy.py restrictions.default encasementlib.r2py [security_layer].r2py [attack_program].r2py ```

Make sure you went through the "How to get RepyV2" section!


# Notes and Resources
----
 
 * For a complete list of syntax in Repyv2 please visit:
 * **[https://github.com/SeattleTestbed/docs/blob/master/Programming/RepyV2API.md]**
 
 * The following link is an excellent source for information about security layers: **[https://ssl.engineering.nyu.edu/papers/cappos_seattle_ccs_10.pdf]**

 * **Note:** It is possible to add multiple security layers to Repy, this
may be useful for testing different mitigations separately.  This is
done with the following command at the terminal:

```python repy.py restrictions.default encasementlib.r2py [security_layer1].r2py [security_layer2].r2py [security_layer3].r2py [program].r2py```

**Your security layer must produce no output!! **

 * In repy log replaces print from python.  This may be helpful when
testing if Repy installed correctly.


# Extra Credit
----
For extra credit, program that keeps all old versions of files and allows
read from any of them.  Writing to any old file creates a new (empty) version
of that file.
Do not submit this code inside your assignment. Submit a separate copy for extra credit.



# What to turn in?
----
 * Turn in a repy file called reference_monitor_[ netid ].r2py with all
letters in lowercase.

* **Never raise unexpected errors or produce any output.**  Your program
must produce no output when run normally.

 * For extra credit turn in a second repy file called extra_credit_[netid].r2py  **You must turn in separate files for the normal assignment and extra credit**
