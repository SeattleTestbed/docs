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
In this assignment you will create a security layer which keeps a backup
copy of a file in case it is written incorrectly.  This is a common
technique for things like firmware images where a system may not be able to
recover if the file is written incorrectly.  For this assignment, a
valid file must start with the character 'S' and end with the character
'E'.  If any other characters (including lowercase 's', 'e', etc.) are
the first or last characters, then the file is considered invalid. 

Applications use ABopenfile() to create or open a file. Files are created by 
setting create=True when calling ABopenfile(), the reference 
monitor will create a valid backup file called filename.a and an empty 
file we will write to called filename.b. When close() is called on the file, if both filename.a and filename.b are valid, the original file's data is replaced with the data of filename.b. If filename.b is not valid, the original file should take on the data of the backup a file. Afterward both the a and b file are discarded. 

Write test applications to ensure your reference monitor behaves properly 
in different cases and to test attacks against your monitor.    

#### The Reference Monitor Must:
1. Not modify or disable any functionality of any [RepyV2 API calls](../Programming/RepyV2API.md), such as:
   * Creating new files  
   * Opening an existing file  
   * Reading valid backup using readat()  
   * Writing to file using writeat(). This includes invalid writes, because  'S' and 'E'
may later be written to the begining and end of the file respectively.  
2. Check if file contents starts with 'S' and ends with 'E', only when close() is called.
3. Update the original file with the new data IF the new data is valid on close().
4. Not produce any errors  
   * Normal operations should not be blocked or produce any output  
   * Invalid operations should not produce any output to the user
#### The Reference Monitor Should:
1. Create two copies of the same file (filename.a and filename.b)   
   * One is a valid backup to read from, and the other is written to
2. When an app calls ABopenfile(), the method opens the A/B files, which 
 you should name filename.a and filename.b.
3. When the app calls readat(), all reads must be performed on the valid backup.
4. When the app calls writeat(), all writes must be performed on the written to file. 


Three design paradigms are at work in this assignment: accuracy,
efficiency, and security.

 * Accuracy: The security layer should only stop certain actions from being
blocked. All other actions should be allowed. For example, if an app
tries to read data from the backup file, this must succeed as per normal and
must not be blocked.  All situations that are not described above *must*
match that of the underlying API.

 * Efficiency: The security layer should use a minimum number of resources,
so performance is not compromised.  For example, keeping a complete copy of 
every file on disk in memory would be forbidden.

 * Security: The attacker should not be able to circumvent the security
layer. For example, if the attacker can cause an invalid file to be saved, read the "write to" file, or can
write to the backup file we read from, then the security is compromised.



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
This security layer inadequately handles A/B storage for files in RepyV2.



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

class ABFile():
  def __init__(self,filename,create):
    # globals
    mycontext['debug'] = False   
    # local (per object) reference to the underlying file
    self.Afn = filename+'.a'
    self.Bfn = filename+'.b'

    # make the files and add 'SE' to the readat file...
    if create:
      self.Afile = openfile(self.Afn,create)
      self.Bfile = openfile(self.Bfn,create)
      self.Afile.writeat('SE',0)


  def writeat(self,data,offset):
    
    # Write the requested data to the B file using the sandbox's writeat call
    self.Bfile.writeat(data,offset)
  
  def readat(self,bytes,offset):
    # Read from the A file using the sandbox's readat...
    return self.Afile.readat(bytes,offset)

  def close(self):
    self.Afile.close()
    self.Bfile.close()


def ABopenfile(filename, create):
  return ABFile(filename,create)




# The code here sets up type checking and variable hiding for you.  You
# should not need to change anything below here.
sec_file_def = {"obj-type":ABFile,
                "name":"ABFile",
                "writeat":{"type":"func","args":(str,(int,long)),"exceptions":Exception,"return":(int,type(None)),"target":ABFile.writeat},
                "readat":{"type":"func","args":((int,long,type(None)),(int,long)),"exceptions":Exception,"return":str,"target":ABFile.readat},
                "close":{"type":"func","args":None,"exceptions":None,"return":(bool,type(None)),"target":ABFile.close}
           }

CHILD_CONTEXT_DEF["ABopenfile"] = {TYPE:OBJC,ARGS:(str,bool),EXCP:Exception,RETURN:sec_file_def,TARGET:ABopenfile}

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
if "testfile.txt.a" in listfiles():
  removefile("testfile.txt.a")
if "testfile.txt.b" in listfiles():
  removefile("testfile.txt.b")
myfile=ABopenfile("testfile.txt",True)  #Create an AB file

# I should get 'SE' when reading an empty file...
assert('SE' == myfile.readat(None,0))

# put some valid data in the file.
myfile.writeat("Stest12345E",0)

# I should still get 'SE' because the file wasn't closed.
assert('SE' == myfile.readat(None,0))

#Close the file
myfile.close()


```

In the example above, a successful attack would cause an error when
 ```assert('SE'== myfile.readat(None, 0))``` 
is executed because the newly created valid file did not contain 'SE', meaning an invalid
read occurred

If the example above executed without error, meaning that the newly created file contained 'SE',
then the attack was successfully defended.

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

