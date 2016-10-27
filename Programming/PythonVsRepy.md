# All of the Python You Need to Forget to Use Repy

This tutorial is written for those who are familiar with the Python programming language, and want to start using Repy. The syntax and many of the properties of Repy should be very familiar for Python users, but there are some noticeable differences. 

Many Python built-ins are not allowed in Repy. This is to ensure maximum cross platform compatibility and security for end users. Python modules aren't allowed to be imported (see below), however porting python code to Repy takes minimal effort. 
 
----

----



## Global Variables
----
In Repy global variables are not allowed. In place of this there is an implicit dictionary called ```mycontext``` which can be used to create globally visible variables. 
```python
mycontext['pagecount'] = mycontext['pagecount'] + 1
```



## Import statements
----
In Repy there are no ```import``` statements. In its place make use of the **include** statement. ```include``` takes the specified file and inlines its content to that place in the Repy program. 

If you have the file ''a.repy'':
  ```python
def foo():
    print "foo"
  ```
And a file ''b.repy'':
  ```python
include a.repy
def bar():
    print "bar"
  ```

You can use the repy preprocessor to produce a file like:
  ```python
def foo():
    print "foo"

def bar():
    print "bar"
  ```

To do this run ```python repypp.py b.repy out.repy```. The a.repy file does not need to be pre-processed also. The file out.repy will contain the code for a.repy included inside the code for b.repy at the appropriate place. 

## Input
There are no Repy mechanisms to read user input. Providing the python ```input``` and ```raw_input``` methods is impractical, since the intent of Repy is to run as a background process on user machines. There is no terminal to accept input from. 

## Python Built-Ins Not in Repy
Below is a list of the Python built-ins that are **not** allowed in Repy 

 * all
 * any
 * bin
 * callable
 * compile
 * complex
 * delattr
 * dir
 * enumerate
 * eval
 * execfile
 * globals
 * hash
 * help
 * id
 * input
 * iter
 * lambda
 * locals
 * next
 * property
 * raw_input
 * reload
 * reversed
 * sorted
 * staticmethod
 * super
 * unichr
 * unicode
 * vars
 * yield
 * !__import!__






## Common Python Constructs and Their Repy Counterparts
----

#### sys.argv
  Programs written in Python use ```sys.argv``` to access arguments to the file. In Repy the variable ```callargs``` behaves the same as ```sys.argv[1:]```

#### ```__name__```
  There is no ```__name__``` variable. In python it's common to use the following code to see if a file invoked directly:
  ```python
if __name__ == "__main__":
   main()
  ```

  In Repy the corresponding implicit variable is **callfunc**. A similar Repy program would include:
    ```python
if callfunc == "initialize":
  main()
    ```

  This ensures that the following code is only executed once. Note that if you use the Repy ```include``` statement and the above if statement, both files' initialize blocks will be executed. 

  Repy scripts are called twice: on entry ```callfunc``` is set to "intialize". At exit ```callfunc``` is surprisingly enough called "exit".




## Python Modules
----
Python modules aren't directly allowed in Repy. This is to ensure safety for Seattle users, so all code run in a VM can be strictly controlled. Many Python modules have Repy equivalents, which are listed below:



### Files
----
#### open()
  Repy has a builtin **open()** that behaves similarly to the Python native ```open```. 
    
  The file to be opened may only contain the characters 'a-zA-Z0-9.-_', and cannot be . or ..

  The object returned by ```open()``` is similar to the Python [[file](http://docs.python.org/library/stdtypes.html#file-objects)] object, and provides most of the same functionality.


#### os.listdir()
  Repy provides the function **listdir()** which is equivalent to a call to Python
    ```python
os.listdir('.')
    ```
  Since file access is only allowed within a VM, there is no need to provide ```listdir()``` with any arguments. The list will contain all the files in the current working directory. 
#### os.remove()
  Remove a file from the user program area. Has the same filename character restrictions as ```open``` 
  The following Repy code
    ```python
removefile(f)
    ```
  Is equivalent to the following Python
    ```python
os.remove(f)
    ```


### Time
----
#### time.sleep()
  Repy's **sleep()** function behaves similarly to [[time.sleep()](http://docs.python.org/library/time.html#time.sleep)], causing execution of the current program to halt for the specified number of seconds. 

#### Timer
  In python, to start a timer you typically have code such as:
    ```python
def hello(str):
  print "hello,", str

t = Timer(30.0, hello, ["world"])
t.start() # after 30 seconds, "hello, world" will be printed
    ```

  In repy use the **settimer()** function. A repy equivalent would be 
    ```python
def hello(str):
    print "hello," str

t = settimer(30.0, hello, ["world"])
    ```

  In order to cancel the timer, use 
    ```python
canceltimer(t)
    ```

#### time.time()
  In repy you make make use of the **getruntime()** function. This returns a float representing the runtime of the current program, which is equivalent to the Python:
    ```python
time.time() - starttime #starttime is when the program started execution
    ``` 

  For programs that actually want the "time" (rather than using it to measure elapsed time as most programmers seem to use it), there is a library that does a NTP lookup and provides the correct global time.


	
### Networking
----

There are several native Repy functions provided to make common networking operations easier. Many don't have direct Python equivalents, but are convenience functions. See the RepyTutorial for examples of these functions.


#### socket.gethostbyname_ex(name)
  In Repy, rather than use [[socket.gethostbyname_ex(name)](http://docs.python.org/library/socket.html#socket.gethostbyname_ex)], use **gethostbyname_ex(name)**. The behaviour is the same, so you can write Repy which looks like
    ```python
gethostbyname_ex("www.google.com")
    ```



### Threading
----
#### threading.Lock()
  In Repy use **getlock()** to create new instances Mutex objects. The object's behaviour is the same in Repy as it is in Python: it supports the **acquire** and **release** operations. 


