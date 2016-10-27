
# Writing and Using Custom Security Layers in Repy V2
This guide is meant to explain security layers in Repy V2, how to write a custom security layer, and how to run code with a custom security layer.



## What is a Security Layer?
A security layer is a layer between the user and a public function or method. It is used to control the access or use of functions and methods.

For example, many operating systems only allow privileged users to read or modify certain files. With a security layer we can restrict access to certain files, even though we would normally have access to them.

## Running code through a security layer
### Preparing the location
You first need to prepare the location. The full directions are [wiki:RepyV2CheckoutAndUnitTests#Preparingthetests here]. Below is a summary:

 * Change into the `repy_v2` directory.
 * Create a folder called `prepared_tests`
 * Run `python preparetest.py -t prepared_tests/`

### Running the code
Change into the `prepared_tests` directory.

Run the following code:
```
python repy.py restrictions.default encasementlib.repy [security_layer].repy [program].repy
```

where `[security_layer]` is the name of the security layer, and `[program]` is the repy program.


## Writing a Security Layer
Repy allows the creation of custom security layers. This guide will cover creating layers for functions and methods.

### Header
For clarity, it is recommended to include the following at the beginning of your security layer:
```
TYPE="type"
ARGS="args"
RETURN="return"
EXCP="exceptions"
TARGET="target"
FUNC="func"
OBJC="objc"
```

### Footer
At the end of the code for the security layer, you need to call `secure_dispatch_module()`. It only should be called once.

### Functions
In order to create a security layer for a function, two things must be done:

1) The function must be defined

2) We need to map that function to an API function

For example, our machine likes to slack off for long periods of time. So we decided that our machine should always `sleep` for at least 2 seconds each time `sleep` is called.
```
def slacker_sleep(seconds):
  if(seconds < 2.0)
    seconds = 2.0
  sleep(seconds)
```

The next thing that needs to be done is to map our `slacker_sleep` function to the internal `sleep` function. To do this, we need to put a new entry in `CHILD_CONTEXT_DEF`, as follows:
```
CHILD_CONTEXT_DEF["sleep"] = {TYPE:FUNC,ARGS:((int,long,float),),EXCP:None,RETURN:None,TARGET:slacker_sleep}
```
Note that the key is the name of the API function, and `TARGET` is the name of our function that will act as a layer.

### Methods
Similar to a function, creating a security layer for a method requires

1) Defining a class that will be accessed.

2) Mapping the class methods to the original public methods.


For example, say we wanted to prevent the user from reading the first byte of a file.

```
class NoFirstByteFile():
  def __init__(self,file):
    self.file = file

  def readat(self,bytes,offset):
    if(offset == 0):
        raise RepyArgumentError("You can't read that first bit!")
    return self.file.readat(bytes,offset)

  def writeat(self,data,offset):
    return self.file.writeat(data,offset)

  def close(self):
    return self.file.close()

sec_file_def = {"obj-type":NoFirstByteFile,
                "name":"NoFirstByteFile",
                "readat":{TYPE:FUNC,ARGS:((int,long,type(None)),(int,long)),EXCP:Exception,RETURN:str,TARGET:NoFirstByteFile.readat},
                "writeat":{TYPE:FUNC,ARGS:(str,(int,long)),EXCP:Exception,RETURN:None,TARGET:NoFirstByteFile.writeat},
                "close":{TYPE:FUNC,ARGS:None,EXCP:None,RETURN:(bool,type(None)),TARGET:NoFirstByteFile.close}
               }
```

It should be noted that this will simply create a new object, and prepare it for use. However, Repy code does not use explicitly called constructors. Instead, factory functions are called instead. Therefore, we will need to also modify the return type of the `openfile` function.

Therefore, you will also need to do the following:
```
def openfile_restricted(filename, create):
  f = openfile(filename,create)
  return NoFirstByteFile(f)
	
CHILD_CONTEXT_DEF["openfile"] = {TYPE:OBJC,ARGS:(str,bool),EXCP:Exception,RETURN:sec_file_def,TARGET:openfile_restricted}
```

## Samples
### Sample for Functions
Here is the full code for our first security layer, the one that acts as an interface to `sleep`.

```
# Repy V2 Security Layer Sample - Function - Code
# slacker_sleep.repy

# Defining constants for later use
TYPE="type"
ARGS="args"
RETURN="return"
EXCP="exceptions"
TARGET="target"
FUNC="func"
OBJC="objc"

# Defining our function
def slacker_sleep(seconds):
  if(seconds < 2.0):
    seconds = 2.0
  sleep(seconds)

# Mapping our function to sleep() 
CHILD_CONTEXT_DEF["sleep"] = {TYPE:FUNC,ARGS:((int,long,float),),EXCP:None,RETURN:None,TARGET:slacker_sleep}

# Dispatch
secure_dispatch_module()

```

The next thing to do is to actually test this code. The easiest way would be to call sleep for a minuscule amount of time, and see that it's upped to 2 seconds.

To do that, save the following code to a new file, `slacker_sleep_test.repy`
```
# Repy V2 Security Layer Sample - Function - Test
# slacker_sleep_test.repy

log("Start")
sleep(0.000000001)
log("Finish")
```

Run the test code by calling:
```
python repy.py restrictions.default encasementlib.repy slacker_sleep.repy slacker_sleep_test.repy
```

If there was a noticeable delay between Start and Finish, the layer worked properly. 

### Sample for Methods
Here is the full code for our second layer, the one that acts as an interface to `file.readat`.

```
# Repy V2 Security Layer Sample - Methods - Code
# no_first_byte.repy

# Defining constants for later use
TYPE="type"
ARGS="args"
RETURN="return"
EXCP="exceptions"
TARGET="target"
FUNC="func"
OBJC="objc"


# Creating our class
class NoFirstByteFile():
  def __init__(self,file):
    self.file = file

  def readat(self,bytes,offset):
    if(offset == 0):
        raise RepyArgumentError("You can't read that first bit!")
    return self.file.readat(bytes,offset)

  def writeat(self,data,offset):
    return self.file.writeat(data,offset)

  def close(self):
    return self.file.close()

# Creating the mappings for our class 

sec_file_def = {"obj-type":NoFirstByteFile,
                "name":"NoFirstByteFile",
                "readat":{TYPE:FUNC,ARGS:((int,long,type(None)),(int,long)),EXCP:Exception,RETURN:str,TARGET:NoFirstByteFile.readat},
                "writeat":{TYPE:FUNC,ARGS:(str,(int,long)),EXCP:Exception,RETURN:None,TARGET:NoFirstByteFile.writeat},
                "close":{TYPE:FUNC,ARGS:None,EXCP:None,RETURN:(bool,type(None)),TARGET:NoFirstByteFile.close}
               }

# Creating a new version of openfile so it creates a NoFirstByteFile object, instead of a normal file.
def openfile_restricted(filename, create):
  f = openfile(filename,create)
  return NoFirstByteFile(f)
	
# Mapping openfile to our new version of openfile
CHILD_CONTEXT_DEF["openfile"] = {TYPE:OBJC,ARGS:(str,bool),EXCP:Exception,RETURN:sec_file_def,TARGET:openfile_restricted}

# Dispatch
secure_dispatch_module()
```

We should then write some code to test our security layer. Given the simplicity of our changes, this should be enough:
```
# Repy V2 Security Layer Sample - Methods - Test
# no_first_byte_test.repy

tempfile = openfile("sample.txt",True)
tempfile.writeat("Hello",0)
try:
  tempfile.readat(2,0)
except:
  pass
else:
  log("No exception was thrown")
```

We can run the code through the security layer by running: 
```
python repy.py restrictions.default encasementlib.repy no_first_byte.repy no_first_byte_test.repy
```

## Further Reference
[repy_v2/benchmarking-support/allnoopsec.py](https://seattle.poly.edu/browser/seattle/branches/repy_v2/benchmarking-support/allnoopsec.py) is an empty security layer that doesn't perform any operations.

[repy_v2/benchmarking-support/all-logsec.py](https://seattle.poly.edu/browser/seattle/branches/repy_v2/benchmarking-support/all-logsec.py) is security layer that performs logging functions.