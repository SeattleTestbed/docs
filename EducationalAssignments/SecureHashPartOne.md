# Implement a Defensive Security System

This assignment will help you understand security mechanisms. You will be
guided through the steps of creating a reference monitor using the security
layer functionality in RepyV2. A reference monitor is an access control
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
In this assignment you will create a security layer which tracks the secure
hash of the files. This is an implementation of the file integrity checkers.
This is generally used for the verification of the files to prevent them 
from  being tampered in anyway. The main goal of this reference monitor is to monitor 
the secure hash of every 100 byte "block" of any file whose name starts with "trackme".

The block numbers start at 0 for every file. The block 0 contains bytes 0-99 of the file,
block 1 containing bytes 100-199, etc. Any such file will have entries in the "trackhash"
file for every 100 byte block or partial block if the block is not full.

The contents of the "trackhash" will list file name, block number, and hash as shown below:

trackme.foo 0 33F5165C660DB60B931CA3E623269C0E70988B08

trackme.foo 1 5A374DCD2E5EB762B527AF3A5BAB6072A4D24493

trackme.bar 0 2FA51E6427F3CF67EEF9C96F8DE40AABA4D377E9

#### The Reference Monitor Must:

1. Block access to the "trackhash" file so that the attack code does not modify, read, or delete it.
2. Only read the contents of a block from the disk when that block if first written to.
3. Not read any of the data as a part of openfile().

Finally, the reference monitor must keep the "trackhash" file up to date 
with the disk content any time control is transferred back to the user program. 
To make this easier, the reference monitor may read and write to the "trackhash" 
file as often as it chooses to. This makes it easier for the reference monitor
to ensure that the disk state is always consistent.

Three design paradigms are at work in this assignment: accuracy,
efficiency, and security.

 * Accuracy: The security layer should only stop certain actions from being blocked. 
 All other actions should be allowed. The security layer should accurately hash the 
 blocks of files in the trackhash file. read calls are allowed if-and-only-if the 
 block is written for the first time.
 
 * Efficiency: The security layer should use a minimum number of resources,
so performance is not compromised.  In particular, the security layer may not
read more blocks than are necessary.  

 * Security: The attacker should not be able to circumvent the security
layer. Hence, if the attacker can modify, read or delete the contents 
of "trackhash" file or is still able to read the contents of a block that 
is not first written to then the security is compromised, for example.


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
This security layer inadequately handles secured hashing for files in RepyV2.



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

class SecureFile():
	def __init__(self,filename,create):
		# globals
		mycontext['debug'] = False   
		
		# local (per object) reference to the underlying file
		self.fn = filename
		self.trackfn = 'trackhash'
		
		# make the files
		if create:
			# ensure to check your filename
			self.file = openfile(self.fn,create)
			self.trackfile = openfile(self.trackfn,True)

	def writeat(self,data,offset):	
		# applying hashfunction to your data - repy supports SHA1 library
		temp_data = applyHashFunction(data)
    		block_no = 0
		
		# Writing file contents in the "trackhash" file with filename, block no and hashed data
		# your data may not necessarily be in one entire block or begin from block no 0
		self.trackfile.writeat(self.fn+" "+str(block_no)+" "+temp_data,0)
		
		#close the trackhash file
		self.trackfile.close()

		# Write the requested data to the file using the sandbox's writeat call
		self.file.writeat(data, offset)		
  
	def readat(self,bytes,offset):
		# Read from the file using the sandbox's readat...
		# read the file only if the block is first written to
		return self.file.readat(bytes,offset)

	def close(self):
		self.file.close()

def secureopenfile(filename, create):
	return SecureFile(filename,create)

# The code here sets up type checking and variable hiding for you.  You
# should not need to change anything below here.
sec_file_def = {"obj-type":SecureFile,
                "name":"SecureFile",
                "writeat":{"type":"func","args":(str,(int,long)),"exceptions":Exception,"return":(int,type(None)),"target":SecureFile.writeat},
                "readat":{"type":"func","args":((int,long,type(None)),(int,long)),"exceptions":Exception,"return":str,"target":SecureFile.readat},
                "close":{"type":"func","args":None,"exceptions":None,"return":(bool,type(None)),"target":SecureFile.close}
           }

CHILD_CONTEXT_DEF["secureopenfile"] = {TYPE:OBJC,ARGS:(str,bool),EXCP:Exception,RETURN:sec_file_def,TARGET:secureopenfile}

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
if "trackme.foo" in listfiles():
  removefile("trackme.foo")

#Create a file
myfile = secureopenfile("trackme.foo",True)  

# Put some valid data in the file.
myfile.writeat("AbCd",0)

# I should be able to read it out.
assert('AbCd' == myfile.readat(None, 0))

# may read block 1 since it writes to block 1 and "hello" is
# contained entirely in that block
myfile.writeat("hello",123)

# may read blocks 2 and 3 since it writes to both blocks
myfile.writeat("goodbye",298)

# may not read any blocks since 1 and 2 were previously read above
myfile.writeat("konnichiwa",195)

# Close the file
myfile.close()


```

**Note:** All attacks should be written as RepyV2 files, using the `.r2py` extension.

#### Choice of File Names
----
It is important to keep in mind that only lowercase file names are allowed.
So in the above code, specifically:

```
# Open a file
myfile=openfile("look.txt", True)
```

`look.txt` is a valid file name, however `Look.txt` and `LOOK.TXT` are not.
Examples of other invalid files names are `.look.txt`, `look/.txt`, and 
`look().txt`. Essentially all non-alphanumeric characters are not allowed.

### Running your security layer
----
Finally, type the following commands at the terminal to run your security
layer with your attack program

```python repy.py restrictions.default encasementlib.r2py [security_layer].r2py [attack_program].r2py ```

Make sure you went through the "How to get RepyV2" section!


# Notes and Resources
----
 
 * For a complete list of syntax in Repyv2 please visit
   the **[RepyV2 API documentation](https://github.com/SeattleTestbed/docs/blob/master/Programming/RepyV2API.md)**
 
 * **[This paper](https://ssl.engineering.nyu.edu/papers/cappos_seattle_ccs_10.pdf)**
   is an excellent source for information about security layers

 * **Note:** It is possible to add multiple security layers to Repy, this
may be useful for testing different mitigations separately.  This is
done with the following command at the terminal:

```python repy.py restrictions.default encasementlib.r2py [security_layer1].r2py [security_layer2].r2py [security_layer3].r2py [program].r2py```

**Your security layer must produce no output!!**

 * In RepyV2, `log` replaces `print` from Python.  This may be helpful when
testing if Repy installed correctly.

# What to turn in?
----
 * Turn in a repy file called `reference_monitor_netid.r2py` with all
letters in lowercase. For example, if your netId is `jc123`, your reference monitor should be named `reference_monitor_jc123.r2py`

* **Never raise unexpected errors or produce any output.**  Your program
must produce no output when run normally.
