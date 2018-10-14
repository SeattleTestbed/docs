# Implement a Defensive Security System

This assignment will help you understand security mechanisms. You will be
guided through the steps of creating a reference monitor using the security
layer functionality in Repy V2. A reference monitor is an access control
concept that refers to an abstract machine that mediates all access to
objects by subjects. This can be used to allow, deny, or change the
behavior of any set of calls. While not a perfect way of validating your
reference monitor, it is useful to create test cases to see whether your
security layer will work as expected. (The test cases may be turned in as
part of the next assignment.)

This assignment is intended to reinforce concepts about access control and
reference monitors in a hands-on manner. 






## Overview
----
In this assignment you will create a security layer which prevents writes that
do not maintain even parity for all 8 byte-aligned sequences in a file. 
(What this means is described more precisely below.)  Parity is often used to 
detect errors or tampering for data.

Your security layer will purely focus on storage of information in a file.  
Using the minimal number of read blocks possible, you must determine if an 
operation would change the parity.  Your security layer must track enough 
information about the parity of any 8-byte sequences read so that it need not
read the sequence more often than is necessary.  

All write operations must either complete or be blocked.  All writes that would 
not cause the parity of a 8-byte sequence to be non-even must be permitted.  
Any write that would cause the parity of any 8-byte sequence to be non-even
must be blocked by throwing a RepyParityError exception.

Note that in some cases there will be an incomplete sequence (e.g., the last 
5 bytes of a 13 byte file).  Parity is not checked for an incomplete sequence
(it is only checked when the sequence is completed).  

Note that the behavior of other system calls must not be changed in a way
that is visible to the running program.  Reading from a file, opening a file, 
etc. must appear to operate in the same manner.

Three design paradigms are at work in this assignment: accuracy,
efficiency, and security.

 * Accuracy: The security layer should stop writeat calls if-and-only-if
they would result in non-even parity. All other actions should be allowed. 
For example, if an app tries to read data a file or write data that results
in even parity 8-byte sequences these operations must succeed as per normal 
and must not be blocked.  All situations that are not described above *must*
match that of the underlying API.

 * Efficiency: The security layer should use a minimum number of resources,
so performance is not compromised.  In particular, the security layer may not
read more 8-byte sequences than are necessary.  Hint: it is *always* possible 
to read two or fewer 8 byte blocks per writeat().

 * Security: The attacker should not be able to circumvent the security
layer. Hence, if the attacker can cause a file with a non-even 8-byte sequence
to be written then the security is compromised, for example.


### Parity and 8-byte sequences

For this assignment a file is conceptually broken up into 8-byte sequences. 
Every consecutive series of 8 bytes (from the beginning of a file) is its own
8-byte sequence.  So, the first 8 bytes (bytes 1-8) are the first sequence, the 
next 8 bytes (bytes 9-16) are the second, etc.  

Note that a write may be performed on a non-8-byte-aligned portion of the 
file.  E.g., bytes 5-17 may be written in a single write.  For that write, the 
first, second, and third 8 byte sequence are all modified.

In terms of parity, each byte has a parity based upon its value when calling 
ord() in python.  Each byte that has a parity divisible by 2 is considered to
be even.  An 8-byte sequence is considered to be even if there are an even
number of non-even bytes in the sequence.  In other words, if there are 0,
2, 4, 6, or 8 non-even bytes, the sequence is considered to be even.  Also,
if a sequence has not been completely written (because it is at the end of a 
file), it is always considered to have even parity for the purposes of a 
write being allowed or blocked.


### Getting Python and RepyV2

Please refer to the [SeattleTestbed Build Instructions](../Contributing/BuildInstructions.md#prerequisites)
for details.

Once you have built RepyV2 into a directory of your choice, change into that
directory. Use the command below in order to run your RepyV2 programs:

```python repy.py restrictions.default encasementlib.r2py [security_layer].r2py [program].r2py```

(Replace `[security_layer].r2py` and `[program].r2py` by the names of the
security layers and program that you want to run.) 

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
 * Downloading the wrong version of seattle:

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
The following program is a basic and incomplete sample code for you to get
an idea about writing security layer. Remember, you have no idea how the
attacker will try to penetrate your security layer, so it is important that
you leave nothing to chance!  


### A basic (and inadequate) defense

Time to start coding!  Let's inspect a basic security layer.  

```
"""
This security layer inadequately handles parity for files in RepyV2.



Note:
    This security layer uses encasementlib.r2py, restrictions.default, repy.py and Python
    Also you need to give it an application to run.
    python repy.py restrictions.default encasementlib.r2py [security_layer].r2py [attack_program].r2py 
    
    """ 
class RepyParityError(Exception):
    pass

class EvenParityFile():
  def __init__(self,filename,create):
    # globals
    mycontext['debug'] = False   
    # local (per object) reference to the underlying file
    self.fn = filename
 
    self.file = openfile(self.fn,create)


  def writeat(self,data,offset):
   
    # check the parity of the data written
    # NOTE: This is wrong in many ways!!!!
    thisdata = data
    while thisdata:
        eightbytesequence = thisdata[:8]
        thisdata = thisdata[8:]
        even = True
        for thisbyte in eightbytesequence:
          # for each byte, if it is odd, flip even to be the opposite
          if ord(thisbyte) % 2:
            even = not even
            
        # actually call write, if we are supposed to...
        if even:
          self.file.writeat(eightbytesequence,offset)
        # ...or error out.
        else:
          raise RepyParityError("Non-even parity write to file")
  
  
  def readat(self,bytes,offset):
    # Read from the file using the sandbox's readat...
    return self.file.readat(bytes,offset)

  def close(self):
    self.file.close()


def parityopenfile(filename, create):
  return EvenParityFile(filename,create)




# The code here sets up type checking and variable hiding for you.  You
# should not need to change anything below here.
sec_file_def = {"obj-type":EvenParityFile,
                "name":"EvenParityFile",
                "writeat":{"type":"func","args":(str,(int,long)),"exceptions":Exception,"return":(int,type(None)),"target":EvenParityFile.writeat},
                "readat":{"type":"func","args":((int,long,type(None)),(int,long)),"exceptions":Exception,"return":str,"target":EvenParityFile.readat},
                "close":{"type":"func","args":None,"exceptions":None,"return":(bool,type(None)),"target":EvenParityFile.close}
           }

CHILD_CONTEXT_DEF["openfile"] = {"type":"objc","args":(str,bool),"exceptions":Exception,"return":sec_file_def,"target":parityopenfile}
CHILD_CONTEXT_DEF["RepyParityError"] = {"type":"any","target":RepyParityError}
# Execute the user code
secure_dispatch_module()
```



### Testing your security layer
----
In this part of the assignment you will pretend to be an attacker. Remember
the attacker's objective is to bypass the parity restrictions or cause
the security layer to act in a disallowed manner. By understanding how the
attacker thinks, you will be able to write better security layers.  

An example of a test / attack is found below:

```
if "testfile.txt" in listfiles():
  removefile("testfile.txt")

myfile=openfile("testfile.txt",True)  #Create a parity file

# put some valid data in the file.
myfile.writeat("AA",0)

# I should be able to read it out.
assert('AA' == myfile.readat(None,0))

# However, this write should fail...
try:
  myfile.writeat("BCBCBC",2)
except RepyParityError:
  pass  # should happen
else:
  log("should have been an error instead!")
  
#Close the file
myfile.close()


```

**Note:** All attacks should be written as Repy V2 files, using the .r2py extension.

#### Choice of File Names
----
It is important to keep in mind that only lowercase file names are allowed.
So in the above code, specifically:

```
# Open a file
myfile=openfile("look.txt",True)
```

look.txt is a valid file name, however Look.txt and LOOK.TXT are not.
Examples of other invalid files names are, _look.txt, look/.txt, and 
look().txt. Essentially all non-alphanumeric characters are not allowed.

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
 
 * The following link is an excellent source for information about security layers: **[http://isis.poly.edu/~jcappos/papers/cappos_seattle_ccs_10.pdf]**

 * **Note:** It is possible to add multiple security layers to Repy, this
may be useful for testing different mitigations separately.  This is
done with the following command at the terminal:

```python repy.py restrictions.default encasementlib.r2py [security_layer1].r2py [security_layer2].r2py [security_layer3].r2py [program].r2py```

**Your security layer must produce no output!! **

 * In repy log replaces print from python.  This may be helpful when
testing if Repy installed correctly.

# What to turn in?
----
 * Turn in a repy file called reference_monitor_[ netid ].r2py with all
letters in lowercase.

* **Never raise unexpected errors or produce any output.**  Your program
must produce no output when run normally.
