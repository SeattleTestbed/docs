# All of the Python You Need to Understand Repy (and None You Don't)

This tutorial is written for those who have background knowledge of object oriented programming languages such as C++ and Java. This tutorial focuses on introducing the subset of Python used in the Repy (Restricted Python) language supported by the Seattle testbed.   After reading this tutorial, you should walk through the [RepyTutorial Repy tutorial].

**NOTE WINDOWS USERS:** You must have Python2.5 or Python2.6 installed on your computer. Follow the instructions [InstallPythonOnWindows here] to check if Python2.5 or Python2.6 is currently installed on your system and to get directions on how to install Python2.6 if it is not installed.

**ALL USERS:**
You have to install Repy before starting the tutorial.
You can download Repy [here](https://seattleclearinghouse.poly.edu/download/flibble/).

----

----




## Overview
----




### How python programs are executed
----
Python is an interpreted language, which in a nutshell means that you do not need to compile python code in order to execute it. Here's an example of a program that prints ‘Hello World’.

```python
print “Hello, World”
```

To execute this program, you can place the above source code into a file, say ‘test.py’, and then run the program by executing the following statement on the command line:

```python
python test.py
```

This is the normal way to execute python code. However, since this tutorial is written for those who use Repy, we need to explain the different way to run Repy programs.

There are two ways to execute programs.
You can run your programs on your local computer or on a remote VM that you control.
Although our final goal is to run programs on the VMs, we explain the way to run programs on a local computer here because it's simple.

You can learn how to execute in the VMs in the [RepyTutorial Repy Tutorial].



#### Executing programs locally in Repy
----

You need to add more files as arguments to run the program above in your computer.

```python
python repy.py restrictions.test test.py
```

We need to make sure that you have the files named repy.py and restrictions.test in your current directory before executing the program like above.
If you don't have the restrictions.test, Here is the [raw-attachment:restrictions.test link]. 

Output is following

```python
Hello World
Hello World
Terminated
```


"Terminated" indicates that the program was terminated successfully. (This may not be displayed on all operating systems, and other operating systems may have different messages.)

"Hello World" is printed twice because of repys' architecture, which calls test.py twice.

If you want to print "Hello World" only once, you can change the code to the following:

```python
if callfunc == 'initialize':
    print "Hello World"
```

You need to insert an if block to execute your code one time in initialize status.  

Repy programs are called once upon program initialization and once upon normal program exit.   The callfunc variable is set to initialize or exit depending on what the circumstance is. There is more detail about this in [PythonVsRepy All of the Python You Need to Forget to Use Repy]. 

From now on, we suppose all code below is in the **if callfunc == 'initialize**' block.



#### Testing programs in the interactive mode.
----

Instead of executing this program from the command line in batch mode, you could enter and run the code in interactive mode.

Because Repy doesn't have the interactive mode, and uses different function names from regular python, you can test only simple function operations in the interactive mode.

```python
% python

>>> print “Hello, World”

Hello, World

>>>
```

While in interactive mode, you can test your simple code before executing and look up the command history by using the arrow keys.
To exit interactive mode, hit ctrl-d on Unix or ctrl-z on Windows. 



### Non-restricted type
----

Type is not declared in Python. However, the Python interpreter keeps track of the type of all objects. Thus Python variables don’t have types, but their values do.

```python
x = 10*10 
print x
x = “Hello”
print x
```

Result
```python
100
Hello
```



### High-level operations
----

Python contains many high level operations.

Here is a simple example that prints the number of words in ‘Hello World”


```python
print len(“Hello World”.split())
```

Result:

```python
2
```

The method split() is a member of the string class. It splits a string into a list of words and len() returns the number of elements in a list.



## Basic Grammar
----



### Block Definition
----

```python
for i in range(10):
     print i
```

In C++ and Java, we use curly braces({}) as a block definition, but in Python, it has a different syntax.

The first line should end with a **colon(:)** and from the next line on, lines should be **indented** until you've reached the end of the block.

In the example code, the range() function returns a list of consecutive integers. This will result in 10 iterations of the loop, 0 through 9.




### Flow Control
----



#### if Statements
----

Perhaps the most well-known statement type is the if statement. For example:

```python
x = 42
if x < 0:
    x = 0
    print ’Negative changed to zero’
elif x == 0:
    print ’Zero’
elif x == 1:
    print ’Single’
else:
    print ’More’
```

Result
```python
More
```

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif‘ is short for ‘else if’, and is useful to avoid excessive indentation. An if ... elif ... elif ... sequence is a substitute for the switch or case statements found in other languages.




#### while Statements
----

Just like in most languages, there is a while statement that loops until the condition is false.

```python
x = 1
while x < 10:
  x = x + x  
  print x   # this will print 2, 4, 8, 16


while False:
  print "boo" # this will never print

while True:
  print "hi" # this will print "hi" forever...

```




#### for Statements
----

The for statement in Python differs a bit from what you may be used to in C or Pascal. Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C), Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence. For example (no pun intended):

```python
a = [’cat’, ’window’, ’defenestrate’]
for x in a:
    print x, len(x)
```

Result
```python
cat 3
window 6
defenestrate 12
```



#### break and continue Statements, and else Clauses on Loops
----

The break statement, like in C, breaks out of the smallest enclosing for or while loop.
The continue statement, also borrowed from C, continues with the next iteration of the loop.
Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement.

This is exemplified by the following loop, which searches for prime numbers:

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, ’equals’, x, ’*’, n/x
            break
    else:
        # loop fell through without finding a factor
        print n, ’is a prime number’
```

Result
```python
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```



### Function Definition (def)
----

```python
def square(x):
    return x*x
```


The keyword def is used to define a function. Note once again that the colon and indenting are used to define a block which serves as the function body. A function can return a value, using the return statement. However, the function does not have a type even if it does return something, and the object returned could be anything—an integer, a list, or whatever.



#### Default Argument Values
----
```python
def convert_string_to_number(stringvalue, base=10):
    return int(stringvalue,base)
```

Functions can also have arguments that have default values. The argument vales do not need to be specified by the caller. The following function call ```convert_string_to_number('1234')``` is the same as ```convert_string_to_number('1234',10)```.



#### Keyword Arguments
----
If you have some functions with many parameters, and you want to specify only some of them, then you can give values for such parameters by naming them - this is called keyword arguments.  We use the name (keyword) instead of the position (which we have been using all along) to specify the arguments to the function.

There are two advantages - one, using the function is easier since we do not need to worry about the order of the arguments. Two, we can give values to only those parameters which we want, provided that the other parameters have default argument values.

```python
def func(a, b=5, c=10):
    print 'a is', a, 'and b is', b, 'and c is', c

func(3, 7)
func(25, c=24)
func(c=50, a=100)
```

Output

```python
a is 3 and b is 7 and c is 10
a is 25 and b is 5 and c is 24
a is 100 and b is 5 and c is 50
```



#### Arbitrary Argument Lists
----
Finally, the least frequently used option is to specify that a function can be called with an arbitrary number of arguments. These arguments will be wrapped up in a tuple (see Tuples in Sequences). Before the variable number of arguments, zero or more normal arguments may occur.

```python
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
```



### Reading and Writing Files
----

open() returns a file object, and is most commonly used with two arguments: open(filename, mode).

```python
f = open(’/tmp/workfile’, ’w’)
```

The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be ’r’ when the file will only be read, ’w’ for only writing (an existing file with the same name will be erased), and ’a’ opens the file for appending.  Any data written to the file is automatically added to the end. ’r+’ opens the file for both reading and writing. The mode argument is optional; ’r’ will be assumed if it’s omitted.

When you’re done with a file, call f.close() to close it and free up any system resources taken up by the open file. After calling f.close(), attempts to use the file object will automatically fail.



## Sequences
----

Sequences are array-like but with some differences.



### Lists
----

Lists are denoted by brackets and commas.

There are some useful list operations.
```python
x = [1, 2]
```

```python
x.append(3)

Result: 
[1, 2, 3]
```

```python
x[0]

Result:
1

x[-1]

Result:
3
```
Python array has not only the same indexing structure as other languages but also backward indexing(negative indexing).

In the example above,

|      Value     |  1  |  2  |  3  |
| Positive Index |  0  |  1  |  2  |
| Negative Index | -3  | -2  | -1  |





```python
x.extend([-4, 5])

Result: 
[1, 2, 3, -4, 5]
```

```python
del x[2]

Result: 
[1, 2, -4, 5]
```

```python
x.remove(5)

Result: 
[1, 2, -4]
```

```python
z = x[1:3] # array "slicing": give the first element specified through the last element specified minus one.   Since the elements in a Python list are numbered 0, 1, 2, etc., x[1:3] will return elements 1 and 2.

Result: 
[2, -4]
```

```python
x[1:] # all elements starting with index 1

Result: 
[2, -4]
```

```python
x[:2] # all elements up to but excluding index 2

Result: 
[1, 2]
```

```python
x.index(-4)

Result: 
2
```

```python
2 in x

Result: 
True
```

```python
x = 10
y = 20
[x, y] = [y, x]

Result: 
x = 20, y =10
```

```python
# To loop over two or more sequences at the same time, 
# the entries can be paired with the zip() function.

names = ['John', 'Mary', 'Paul']
answers = ['yellow', 'pink', 'blue']
for name, color in zip(names, answers):
    print name + ' likes ' + color

Result: 
John likes yellow
Mary likes pink
Paul likes blue
```  



### Tuples
----

Tuples are like lists, but are immutable. They are enclosed by parentheses or nothing at all, rather than brackets. The parentheses are mandatory if there is an ambiguity without them, e.g., in function arguments. A comma must be used in the case of an empty or single tuple, e.g., (,) and (5,).

The same operations can be used, except those which would change the tuple. So for example

```python
x = (1,2,’abc’)
print x[1] # prints 2
print len(x) # prints 3
x.pop() # illegal, due to immutability
```



### Strings
----

Strings are essentially tuples of character elements. But they are quoted instead of surrounded by parentheses, and have more ﬂexibility than tuples of character elements would have.

```python
x = ‘abcde’
x[2]

Result:
‘c’
```


```python
x = x[0:3] + ‘z’ + x[3:5]

Result: 
x = ‘abczde’
```



### Dictionaries (Hashes)
----

Dictionaries are associative arrays. The statement

```python
x = {’abc’:12,’sailing’:’away’}
```

sets x to what amounts to a 2-element array with x[’abc’] being 12 and x[’sailing’] equal to ’away’. We say that ’abc’ and ’sailing’ are keys, and 12 and ’away’ are values. Keys can be strings or any immutable object, e.g., numbers and tuples. Use of tuples as keys is quite common in Python applications, and you should keep in mind that this valuable tool is available.

Internal storage is organized as a hash table. This is why Perl’s analog of Python’s dictionary concept is actually called a hash.

Here are examples of usage of some of the member functions of the dictionary class:

```python
x = {’abc’:12,’sailing’:’away’}
```

```python
x[’abc’]

Result:
12
```

```python
y = x.keys()

Result: 
[’abc’, ’sailing’]
```

```python
z = x.values()

Result: 
[12, ’away’]
```

```python
x[’uv’] = 2

Result: 
{’abc’: 12, ’uv’: 2, ’sailing’: ’away’}
```



## Class
----



### Structure
----

The keyword ‘self’ is analogous to this in C++ and Java.
Static variables in Python is ‘class name.variable name’.
The constructor for a class is !__init!__.



### Sample Class
----

```python
class Complex:
    count = 0
    def __init__(self, realpart, imagpart):
        Complex.count += 1
        self.r = realpart
        self.i = imagpart
```



### Derived Classes
----

**superclass.!__init!__(self)** 

If a class b is the subclass of a class a, we need to write it like this:

```python
class b(a):
    def __init__(self,xinit): # constructor for class b
        self.x = xinit # define and initialize an instance variable x
        a.__init__(self) # call base class constructor
```



## Exception Handling
----

Python functions usually don't have C-style error return code to check to see whether they succeeded. Instead, you use Python’s try/except exception-handling mechanism:

```python
try:
    f = open(callargs[0])
except:
    print ’open failed:’, callargs[0]
```

Here’s another example:

```python
try:
    i = 5
    y = x[i]
except IndexError:
    print ’no such index:’, i
```

But the Python idiom also uses this for code which is not acting in an exception context. Say for example we want to find the index of the number 8 in the list x.  If there is no such number in x, then we will append x to the list and return its index. We could do it this way:

```python
try:
    place = x.index(8)
except IndexError:
    x.append(8)
    place = len(x) - 1
```

The try statement has another optional clause which is intended to define clean-up actions that must be executed under all circumstances. A finally clause is always executed before leaving the try statement, whether an exception has occurred or not. For example:

```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print "division by zero!"
    else:
        print "result is", result
    finally:
        print "executing finally clause"
```

Results are following

```python
divide(2, 1)
result is 2
executing finally clause

divide(2, 0)
division by zero!
executing finally clause

divide("2", "1")
executing finally clause
Traceback (most recent call last):
File "<stdin>", line 1, in ?
File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: ’str’ and ’str’
```

As you can see, the finally clause is executed in any event.

Note that an uncaught exception will cause the script to terminate.

