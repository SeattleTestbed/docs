# All of the Python You Need to Forget to Use RepyV2

DISAMBIGUATION NOTE: This is the **RepyV2** version of the page.
There is a separate page for Repy version 1 in `PythonVsRepy.md`.

This tutorial is written for those who are familiar with the Python
programming language, and want to start using RepyV2. The syntax and
many of the properties of RepyV2 should be very familiar for Python
users, but there are some noticeable differences. 

Many Python built-ins are not allowed in RepyV2. This is to ensure
maximum cross platform compatibility and security for end users.
Python modules are not allowed to be imported in RepyV2 (see below),
however porting Python code to RepyV2 takes minimal effort. 
 
----



## Global Variables
----
In RepyV2 global variables are not allowed. In place of this there
is an implicit dictionary called `mycontext` which can be used to
create globally visible variables. 
```python
mycontext['pagecount'] = mycontext['pagecount'] + 1
```



## Import statements
----
In RepyV2 there are no `import` statements. Instead make use of the
dynamic linking facility of `seattlelib_v2/dylink.r2py`.

If you have the file `a.r2py`:
```python
def foo():
  log("foo")
```

You can use `dylink` to link the module code in:
  ```python
a = dy_import_module("a.r2py")

a.foo()  # This calls into the foo function of a.r2py
```

This looks and works similar to importing a module in Python, and then
accessing its definitions.

In order for your program to be able to use `dy_import_module`,
provide `dylink.r2py` as the first argument to `repy.py` (when you
start your sandbox on the command line):

``` 
python repy.y restrictionsfile dylink.r2py your_program_goes_here.r2py
```

or the `run`/`start` command (when using `seash`):
```
start dylink.r2py your_program_goes_here.r2py
```

Needless to say, you will need to upload `dylink.r2py` and all of the
dependencies of your program before you can use this `seash` command.


## Input
There are no RepyV2 mechanisms to read user input. Providing the python
`input` and `raw_input` methods is impractical, since the intent of
RepyV2 is to run as a background process on user machines. There is
no terminal to accept input from.

However, your RepyV2 program can listen on network sockets, and you
may use `netcat` or similar tools to send data to your RepyV2 program.


## Python Built-Ins Not in RepyV2
Below is a list of the Python built-ins that are **not** allowed in RepyV2.
See `repy_v2/safe.py` for details.

```
all, any, bin, callable, compile, complex, delattr, dir, enumerate,
eval, execfile, globals, hash, help, id, input, iter, lambda, locals,
next, property, raw_input, reload, reversed, sorted, staticmethod,
super, unichr, unicode, vars, yield, __import__
```


## Common Python Constructs and Their Repy Counterparts
----

#### sys.argv
Programs written in Python use `sys.argv``` to access arguments to
the file. In RepyV2 the variable `callargs` behaves the same as
`sys.argv[1:]`

#### `__name__`
There is no `__name__` variable. In Python it is common to use the
following code to see if a file was invoked directly (on the other hand,
importing a module invokes it indirectly):
```python
if __name__ == "__main__":
 main()
```

In RepyV2 the corresponding implicit variable is `callfunc`. A similar
RepyV2 program would include:
```python
if callfunc == "initialize":
  main()
```



## Python Modules
----
Python modules are not directly allowed in RepyV2. This is to ensure
safety for Seattle users, so all code run in a VM can be strictly
controlled. Many Python modules have RepyV2 equivalents. See the
[SeattleTestbed/seattlelib_v2](https://github.com/SeattleTestbed/seattlelib_v2)
repository for a complete list.



### Files
----
#### `open()`
RepyV2 has an [`openfile(filename, create)` call](https://github.com/SeattleTestbed/docs/blob/master/Programming/RepyV2API.md#openfilefilename-create)
that behaves similarly to the Python native `open`. 
    
The file to be opened may only contain the characters `a-z0-9.-_`, and
cannot start with a `.`.

The object returned by ```open()``` is similar to the Python
[`file`](http://docs.python.org/library/stdtypes.html#file-objects) object,s
and provides similar functionality: `readat`, `writeat`, `close`.


#### `os.listdir()`
RepyV2 provides the function `listfiles()` which is equivalent to a
call to Python's `os.listdir('.')`.

Since file access is only allowed within a VM, `listfiles` does not
take a directory argument. The list returned will contain all the
files in the current working directory. 


#### `os.remove()`
Remove a file from the user program area. The call has the same filename
character restrictions as `openfile` .

The RepyV2 call `removefile(f)` is equivalent to Python's `os.remove(f)`.


### Time
----
#### `time.sleep()`
The `sleep(seconds)` function in Repy behaves similarly to
[[time.sleep(seconds)](http://docs.python.org/library/time.html#time.sleep)]
in Python, causing execution of the current program to halt for the
specified number of seconds. 


#### `threading.Timer`
In Python, to start a timer you typically have code such as:
```python
import threading

def hello(str):
  print "hello,", str

t = threading.Timer(30.0, hello, ["world"])
t.start()
# after 30 seconds, "hello, world" will be printed
```

In RepyV2, combine the `createthread` and `sleep` functions.
A Repy equivalent would be:
```python
def hello(str):
  log("hello", str, "\n")

def sleep_then_call(pause_in_seconds, call_function, call_args):
  # This function returns a function that takes no arguments. Yet
  # the returned function "remembers" (via a closure) the variables
  # defined in the outside scope.
  # This construction is required as we cannot pass arguments to
  # the function that we supply to createthread.
  def configured_timer_function():
    sleep(pause_in_seconds)
    call_function(*call_args)
  return configured_timer_function

configured_function_for_new_thread = sleep_then_call(30, hello, ["world"])
createthread(configured_function_for_new_thread)
```

#### `time.time()`
In RepyV2 you make make use of the `getruntime()` function. This
returns a float representing the runtime of the current program,
which is equivalent to the Python:
```python
time.time() - starttime #starttime is when the program started execution
``` 

For programs that actually want the current wallclock time (rather
than using it to measure elapsed time as most programmers seem to use
it), the library `seattlelib_v2/time.r2py` provides NTP time.


	
### Networking

There are several native Repy functions provided to make common networking operations easier. Many don't have direct Python equivalents, but are convenience functions. See the RepyTutorial for examples of these functions.


#### `socket.gethostbyname_ex(name)`
In RepyV2, rather than use [socket.gethostbyname(name)](http://docs.python.org/library/socket.html#socket.gethostbyname),
use `gethostbyname(name)`. The behaviour is the same, so you can write
RepyV2 which looks like
```python
ip_address = gethostbyname("www.google.com")
```



### Threading
----
#### `threading.Lock()`
In RepyV2 use `createlock()` to create new instances Mutex objects.
The object's behaviour is the same in RepyV2 as it is in Python:
it supports the `acquire` and `release` operations. 


