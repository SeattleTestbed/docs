 = Code Style Guidelines for the Seattle project =

These guidelines provide examples about what to do (or not to do) when writing code for the Seattle project.   These are based upon Justin's experiences working with Stork, [Guido van Rossum's ](http://www.python.org/dev/peps/pep-0008/) Python style guidelines, and the experiences and suggestions of team members.   Please give Justin feedback if there is anything you'd like to change.


----

----

One of Guido's key insights in building Python is that code is read much more often than it is written.  The guidelines provided here are intended to improve the readability of code and make it consistent across the wide spectrum of Python code.  The primary goal of the code we write for Seattle is **readability**.   The other features that your code must have are security, correctness, and robustness (notice that performance is not listed).   The purpose of this document is to help to improve the readability of Seattle code (which I believe strongly impacts the security, correctness, and robustness).   


A style guide is about consistency.  Consistency within a project is very important and since we're writing basically all of the code ourselves, there should be little reason for inconsistency.  


There is only one good reason to break a rule in the style guideline and that's when applying the rule would make the code less readable, even for someone who is used to reading code that follows the rules.




## Code lay-out
----

  Indentation

    Use 2 spaces per indentation level.

  Tabs

    Never use tabs to indent project code.   There should be no tabs in Seattle code.

  Maximum Line Length

    Try to limit most lines to a maximum of 79 characters.   This certainly should be done for comments, but use common sense when applying this rule to code!   I've seen developers who have a highly indented loop wrap a relatively short line across three separate lines to try to avoid going over 80 characters (don't do it!).

    The preferred way of wrapping long lines is by using Python's implied line
    continuation inside parentheses, brackets and braces.  If necessary, you
    can add an extra pair of parentheses around an expression, but sometimes
    using a backslash looks better.  Make sure to indent the continued line
    appropriately.  The preferred place to break around a binary operator is
    *after* the operator, not before it.  Some examples:
```python
class Rectangle(Blob):
  def __init__(self, width, height,
    color='black', emphasis=None, highlight=0):
    if width == 0 and height == 0 and 

        color == 'red' and emphasis == 'strong' or 

        highlight > 100:
      raise ValueError("sorry, you lose")
    if width == 0 and height == 0 and (color == 'red' or
        emphasis is None):
      raise ValueError("I don't think so -- values are %s, %s" %
          (width, height))
    Blob.__init__(self, width, height,
        color, emphasis, highlight)
```

  Blank Lines

    Separate top-level function and class definitions with at least 5 blank lines.

    Method definitions inside a class are separated by at least 2 blank lines.

    Use blank lines in functions to indicate logical sections and help to offset comments.




## Imports
----

    - Imports should usually be on separate lines, e.g.:

        Yes: 
```python
import os
import sys
```

        No:  
```python
import sys, os
```

    - It is preferable to import an entire module than items from the module

        Yes:
```python
import subprocess
```

        No: 
```python
from subprocess import Popen, PIPE
```

        Definitely Not: 
```python
from subprocess import *
```
        An exception to the last rule is when you must import items in a specific way for repy portability.

    - Imports are always put at the top of the file, just after any module
      comments and docstrings, and before module globals and constants.

    - Always use the absolute package path for all imports.


    - **Avoid circular imports**.   This is where ```a.py``` imports ```b.py``` and then either ```b.py``` or a path of imports from ```b.py``` imports ```a.py```.   This does really odd things to Python, in particular if you perform any actions during import.

    - Try to avoid performing actions on module import.   This doesn't play well with circular imports and is non-intuitive for most programmers.





## Whitespace in Expressions and Statements
----

  Pet Peeves

    Avoid extraneous whitespace in the following situations:

    - Immediately inside parentheses, brackets or braces.

      Yes: 
```python
spam(ham[1], {eggs: 2})
```
      No:  
```python
spam( ham[ 1 ], { eggs: 2 } )
```

    - Immediately before a comma, semicolon, or colon:

      Yes: 
```python
if x == 4: print x, y; x, y = y, x
```
      No:  
```python
if x == 4 : print x , y ; x , y = y , x
```

    - Immediately before the open parenthesis that starts the argument
      list of a function call:

      Yes: 
```python
spam(1)
```
      No:  
```python
spam (1)
```

    - Immediately before the open bracket that starts an indexing or
      slicing:

      Yes: 
```python
dict['key'] = list[index]
```
      No:  
```python
dict ['key'] = list [index]
```

    - More than one space around an assignment (or other) operator to
      align it with another.

      Yes:
```python
x = 1
y = 2
long_variable = 3
```

      No:
```python
x             = 1
y             = 2
long_variable = 3
```


  Other Recommendations

    - Always surround these binary operators with a single space on
      either side: assignment (=), augmented assignment (+=, -= etc.),
      comparisons (==, <, >, !=, <>, <=, >=, in, not in, is, is not),
      Booleans (and, or, not).

    - Use spaces around arithmetic operators:

      Yes:
```python
i = i + 1
submitted += 1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

      Maybe not:
```python
i=i+1
submitted +=1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```

    - Compound statements (multiple statements on the same line) are
      not allowed.

      Yes:
```python
if foo == 'blah':
  do_blah_thing()
do_one()
do_two()
do_three()
```

      No:
```python
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()
```

      Definitely not:
```python
if foo == 'blah': do_blah_thing()
else: do_non_blah_thing()

try: something()
finally: cleanup()

do_one(); do_two(); do_three(long, argument,
    list, like, this)

if foo == 'blah': one(); two(); three()
```



## Comments
----

    Comments that contradict the code are worse than no comments.  Always make
    a priority of keeping the comments up-to-date when the code changes!

    Comments should be complete sentences.  If a comment is a phrase or
    sentence, its first word should be capitalized, unless it is an identifier
    that begins with a lower case letter (never alter the case of
    identifiers!).

    If a comment is short, the period at the end can be omitted.  Block
    comments generally consist of one or more paragraphs built out of complete
    sentences, and each sentence should end in a period.

    You should use two spaces after a sentence-ending period.

    When writing English, Strunk and White apply.   This means you shouldn't have spelling or
    grammar errors.   It also helps to make the project's code look more professional.

  Block Comments

    Block comments generally apply to some (or all) code that follows them,
    and are indented to the same level as that code.  Each line of a block
    comment starts with a # and a single space (unless it is indented text
    inside the comment).

    Paragraphs inside a block comment are separated by a line containing a
    single #.

  Inline Comments

    Use inline comments very sparingly.

    An inline comment is a comment on the same line as a statement.  Inline
    comments should be separated by at least two spaces from the statement.
    They should start with a # and a single space.


    Inline comments are unnecessary and in fact distracting if they state
    the obvious.  Don't do this:
```python
x = x + 1                 # Increment x
```

    But sometimes, this is useful:
```python
x = x + 1                 # Compensate for border
```




  Purpose of Comments

    Comments should give the reader the context for why you are performing a specific action and indicate authorship and mindset.

    It is very important that when you change code you didn't write you
    comment the change.   I've spent days looking for bugs that people
    introduced because they changed code they thought they understood.
    '''Any time you make changes to a module or function you didn't write, use
    your initials in a comment describing the scope and purpose of the change.'''

    Use the comment to explain what you are thinking when you make the
    change.  

    old code:
```python
for line in file("foo"):
  print line.split()[1]
```

    new code:
```python
for line in file("foo"):
  # JAC: Need to check if there is a second word, if not then we
  # can skip the line because it isn't relevant to the output.   
  # Prior code threw an IndexError in this case.
  if len(line.split()) > 2:
    print line.split()[1]
```

    Now when someone reads the new code they can understand why you
    changed what you did.   If the original author reads your updated 
    code, they can tell if you misunderstood their code and easily fix 
    it (but if you misunderstood the code, this is a hint it needs better comments).

    If you spend time struggling to understand something in code, it is 
    useful to put a comment indicating you find it unclear but you *think* 
    this is what is intended.   This helps us to locate portions of the code 
    that need to be cleaned up and also indicates "how" to clean the code.
    
  Comments should describe why you are performing an action, not what action you are performing.   

    No:
```python
i = i + 2     # add 2 to i
```
    Yes: 
```python
i = i + 2     # skipping even numbers since even numbers > 2 are not prime
```

    An exception to this rule is if you need to do some "magic operation" in the code.
```python
# reuse the socket if it's recently been closed but is available 
socketobj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```



  Hints for writing good comments

    It is helpful many times to write comments as questions
```python
# Is the file correctly signed?
if (foo.bar(fn)):
```


    The "right time" to write comments is as you write the code 
    (sometimes I even write them before the code).   You will never 
    have a better understanding of the code than when you write it.


    If you are making assumptions then you should check that your 
    assumptions are valid.   If you can't test your assumptions then 
    at least comment your code
```python
total = 0
for item in list:
  # The list should contain only integers
  total = total + item
```


  Comment quantity

    There is no hard and fast rule for the number of comments a file 
    should have.   However, one way to check it is to read only the 
    comments (not the code).   If you could re-construct the code using 
    only the comments, you are likely at the right level of comments.   

    Note that "well commented" modules may have more lines of comments 
    than lines of code!  





## Documentation Strings
----

    Conventions for writing good documentation strings (a.k.a. "docstrings")
    are immortalized in [PEP 257](http://www.python.org/dev/peps/pep-0257/)

    - Write docstrings for all public modules, functions, classes, and
      methods.  Docstrings are not necessary for non-public methods, but you
      should have a comment that describes what the method does.  This comment
      should appear after the "def" line.


    - Note that most
      importantly, the """ that ends a multiline docstring should be on a line
      by itself, and preferably preceded by a blank line, e.g.:
```python
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.

"""
```

    - For one liner docstrings, it's okay to keep the closing """ on the same
      line.


   Example documentation strings for files, modules, and classes.

      Each file should have a header block that explains the purpose of the
      module, when it was started, who wrote it (or made very substantial
      revisions), and a list of any caveats or issues with the module.
```python
"""
<Program Name>
  storkreport.py

<Started>
  February 4, 2005

<Author>
  sethh@cs.arizona.edu
  Justin Cappos
  Jeffry Johnston

<Purpose>
  Provides Error Reporting/Logging Utility Functions.

  The functions are named loosely based on the syslog levels.  However,
  because syslog has 7 priority levels, and stork only has 4, the
  send_error and send_out_* series only contain debug, info, warning, and
  err (notice, alert, and emergency were omitted).  send_syslog supports
  all seven levels, however.

  Current syslog implementation assumes local syslog (no remote servers),
  and a facility of LOG_USER (defaults from the syslog module).

  On July 10th, 2007, Justin is doing a pretty substantial rewrite.   Blame
  him for any resulting cruft.
"""
```

      Documentation strings are needed for every function in a module that 
      will be called from other modules.   It is recommended to create comment 
      blocks for long functions even if they are private to a module.   There are 5 main
      parts of a function comment block: purpose, arguments, exceptions,
      side effects, and return value.   The purpose is to specify everything someone
      who calls your function needs to know (so they don't need to look at the code).
      For example:
```python
def redirect_stdout(stream):
  """
  <Purpose>
    Redirects the standard output stream (stdout) to a new file stream.
    If this is the first time that output has been redirected, the
    original stdout stream will be saved for use with the restore_stdout
    function.

  <Arguments>
    stream:
           The new file stream for stdout.

  <Exceptions>
    TypeError on bad parameters.

  <Side Effects>
    Changes sys.stdout.

  <Returns>
    None.
  """
```

      Here's a copy-and-paste ready version:
```python
 """
  <Purpose>
    ...

  <Arguments>
    ...

  <Exceptions>
    ...

  <Side Effects>
    ...

  <Returns>
    ...
  """
```

      In general the use of classes is discouraged (link to below), but in the 
      cases it is clear classes should be used, use the following format:
```python
class single_conn(Thread):
  """
  <Purpose>
    Wraps up the client side of arizonacomm into a single class.
  <Side Effects>
    Defaults to running itself in a thread.
  <Example Use>
    # open a connection
    connection = single_conn()
    # write information to the connected party
    connection.send("hello")
    # and disconnect without checking if they have said anything
    connection.disconnect()
  """   
```

Classes that are used for exceptions can be written more succinctly (since the purpose, side effects, example use are obvious).
```python
class UserError(Exception):
  """This exception indicates the user provided us with bad input"""
```



## Naming Conventions
----


  Descriptive Naming Styles


    Use descriptive variable and function names.

      Put at least one adjective in each variable name like 'slicename' or 
      'inputfileobj' or 'deststring'.   Also make sure that the type of the 
      variable is readable by looking at the name.   Also, the word "file" is 
      ambiguous, use fileobj or filename (fn is an acceptable abbreviation for 
      filename).   

      These rules are especially important for function arguments or variables that have long lifespans.

    Yes:
```python
inputfileobj = file(inputfn)   # fn is an acceptable abbreviation for file name
deststring = "abc" + currentstring
slicename = "uw_seattle"
```
     
    No:
```python
inobj = file(filename)
dest = "abc" + current
name = "uw_seattle"
```
 
    Definitely not:
```python
i = i + 1
```

      The only case where it is okay to use single letter variable names is for arguments 
      passed into a constructor or using e for an exception.   For example:
```python
class foo:
  ... # doc string omitted
  itemcount = None
  maxitemcount = None
  itemlist = None
  def __init__(self, i, m):
    self.itemcount = i
    self.maxitemcount = m
    self.itemlist = []

  def popanitem(self):
    try:
      return self.itemlist.pop()
    except KeyError, e:
      # Raise an error, the list is empty...
      raise KeyError("Can't pop an empty foo")
```


    General Variable Names

      Should be the same as function names, always use lower case, using 
      an underscore if a separation is needed, such as: popanitem or pop_an_item

    Constants
        
      Variables which are set once and never change value should be all
      upper case, if a seperator is needed use an underscore.
      

    Exception Names

      Because exceptions should be classes, the class naming convention
      applies here.  However, you should use the suffix "Error" on your
      exception names (if the exception actually is an error).

    Global Variable Names

      (Let's hope that these variables are meant for use inside one module
      only.)  The conventions are about the same as those for functions.

      If you can do it without globals in an intelligent way, then don't use globals.   
      When you must use globals then explain why you need to use globals.   An example 
      that uses globals in a good way is a program that keeps a cache.

    Function Names

      Function names should be lowercase, with words separated by underscores
      as necessary to improve readability.

      !mixedCase is allowed only in contexts where that's already the
      prevailing style (e.g. threading.py), to retain backwards compatibility.

    Function and method arguments

      Always use 'self' for the first argument to instance methods.

      If a function argument's name clashes with a reserved keyword, it is
      generally better to append a single trailing underscore rather than use
      an abbreviation or spelling corruption.  Thus "print_" is better than
      "prnt".  (Perhaps better is to avoid such clashes by using a synonym.)






## Programming Recommendations
----


    - Comparisons to singletons like None should always be done with
      'is' or 'is not', never the equality operators.

      Also, beware of writing "if x" when you really mean "if x is not None"
      -- e.g. when testing whether a variable or argument that defaults to
      None was set to some other value.  The other value might have a type
      (such as a container) that could be false in a boolean context!

    - Use class-based exceptions.

      String exceptions in new code are forbidden, because this language
      feature is being removed in Python 2.6.

      Modules or packages should define their own domain-specific base
      exception class, which should be subclassed from the built-in Exception
      class.  Always include a class docstring.  E.g.:
```python
class MessageError(Exception):
  """Base class for errors in the email package."""
```

      Class naming conventions apply here, although you should add the suffix
      "Error" to your exception classes, if the exception is an error.
      Non-error exceptions need no special suffix.

    - When raising an exception, use "raise ValueError('message')" instead of
      the older form "raise ValueError, 'message'".

      The paren-using form is preferred because when the exception arguments
      are long or include string formatting, you don't need to use line
      continuation characters thanks to the containing parentheses.

    - When catching exceptions, mention specific exceptions
      whenever possible instead of using a bare 'except:' clause.

      For example, use:
```python
try:
  import platform_specific_module
except ImportError:
  platform_specific_module = None 
```

      A bare 'except:' clause will catch SystemExit and KeyboardInterrupt
      exceptions, making it harder to interrupt a program with Control-C,
      and can disguise other problems.  If you want to catch all
      exceptions that signal program errors, use 'except Exception:'.

      A good rule of thumb is to limit use of bare 'except' clauses to two 
      cases:

         1) If the exception handler will be printing out or logging
            the traceback; at least the user will be aware that an
            error has occurred.  

         2) If the code needs to do some cleanup work, but then lets
            the exception propagate upwards with 'raise'.
            'try...finally' is a better way to handle this case.

    - Additionally, for all try/except clauses, limit the 'try' clause
      to the absolute minimum amount of code necessary.  Again, this
      avoids masking bugs.

      Yes:
```python
try:
  value = collection[key]
except KeyError:
  return key_not_found(key)
else:
  return handle_value(value)
```

      No:
```python
try:
  # Too broad!
  return handle_value(collection[key])
except KeyError:
  # Will also catch KeyError raised by handle_value()
  return key_not_found(key)
```



    - Use ```assert``` sparingly.   

      Assert has some tricky semantics because it is a statement, not a function.   Thus you cannot call assert with a string to raise in the logical way

```
assert(x = y, 'x and y must be equal')   # BAD CODE
```

The above code will actually always be True because the tuple (bool, 'string') is True.

      You should use assertions only when it is truly an internal error (i.e. somewhere it should be impossible to reach).   Even so, it is fine to log / exitall instead.



    - Use string methods instead of the string module.

      String methods are always much faster and share the same API with
      unicode strings.  Override this rule if backward compatibility with
      Pythons older than 2.0 is required.

    - Use ''.startswith() and ''.endswith() instead of string slicing to check
      for prefixes or suffixes.

      startswith() and endswith() are cleaner and less error prone.  For
      example:

        Yes: 
```python
if foo.startswith('bar'):
```

        No:  
```python
if foo[:3] == 'bar':
```

    - Object type comparisons should always use isinstance() instead
      of comparing types directly.

        Yes: 
```python
if isinstance(obj, int):
```
        No:  
```python
if type(obj) is type(1):
```

      When checking if an object is a string, keep in mind that it might be a
      unicode string too!  In Python 2.3, str and unicode have a common base
      class, basestring, so you can do:
```python
if isinstance(obj, basestring):
```

      The types module has the StringTypes type defined for that purpose, e.g.:
```python
import types
if isinstance(obj, types.StringTypes):
```

    - For sequences, (strings, lists, tuples), use the fact that empty
      sequences are false.

      Yes: 
```python
if not seq:
if seq:
```
      No: 
```python
if len(seq)
if not len(seq)
```

    - Don't write string literals that rely on significant trailing
      whitespace.  Such trailing whitespace is visually indistinguishable and
      some editors (or more recently, reindent.py) will trim them.

    - Don't compare boolean values to True or False using ==

        Yes:   
```python
if greeting:
```

        No:    
```python
if greeting == True:
```

        Worse: 
```python
if greeting is True:
```

      However, there are a few cases where a function may return True, False, or other values.   In these cases, checking if a value with an unknown type is True or False, is allowed.

    - Use the % string formatting operator only when necessary

      The string formatting operator '%' provides a convenient way to do printf like substitution of variables in strings.  It's better in many cases to put variables in line when you don't need the more advanced options (like fixed length fields).  The issue is that the string formatting operator makes understanding the output difficult in many cases.   For example in the following example, it's difficult to read the code and determine what the resulting output will look like:
```python
print "python %s %s %s/vesselinfodir/ %s/ > /tmp/carter.out 2> /tmp/carter.err"%(carter_script, dist_char, prefix,prefix)
```

      A better way to write this:
```python
print "python "+carter_script+" "+dist_char+" "+prefix+"/vesselinfodir/ "+prefix+"/ > /tmp/carter.out 2> /tmp/carter.err"
```


   - Use else statements for handling errors, not for normal flow in most cases.

For example, if you have a function that is supposed to take a positive integer argument, don't do the following:

```python
if x > 0:
   ...
else: # x must be 0
   ...
```

It may be the case that x is negative, a different type, etc.   Instead do the following:


```python
if x > 0:
   ...
elif x == 0: # x must be 0
   ...
else:
   raise InternalError('Expected x to be a positive integer, not "'+str(x)+'"')
```




 == Potpourri ==

    Unix not Windows style text files.

      If you develop on Windows make sure you use dos2unix before checking in.




    Avoid objects


      Objects are a terrific programming tool when used correctly, but make code 
      nearly unreadable when used poorly.   Unfortunately, even experienced developers 
      have a hard time knowing how to correctly use objects.   About 80% of the code one 
      could write is equally good with and without objects.   10% is easier with objects 
      and 10% is easier without them.   Seattle code should use objects only in very 
      rare cases.   The 90% of the code where objects can be avoided without significant 
      impact, should be written without objects.



    No lambda functions or lisp-esque code

      Don't use lambda functions.   Don't use map, flatten, etc.   It's best not to use 
      these functions and to write longer code that produces the same result instead 
      because using these functions makes your code very dense and difficult to read.

      Do not use syntax like:
```python
must_testy = [must_test(line) for line in changed.split("
n")]
```


    Write test cases

      Since you're going to test your module anyways before integrating it 
      into the rest of Seattle (right?), it makes sense to do it in a reusable way.   
      This way when you make changes later, you can immediately test to see if anything 
      is broken.

      Write 90% tests.   The test should make sure that it will catch 90% of the 
      potential problems with the function.   Avoid writing 50% tests (that only 
      check a common case or two) and avoid writing 99.9% tests because it will 
      consume too much of your time.

      All "external" functions **must** be tested.   Internal functions (starting with ```__```) are up to your discretion.

    Never use short circuit evaluation to produce output

      No:
```python
if synched or askokcancel("Change slice without synching?", "You
have changes that are not synched with the repository. These changes
will be lost if you change the slice right now. 
n
nClick OK to change
slice without synching.", default=CANCEL):
  # then clause
else:
  # else clause
```

      Yes:
```python
if not synched:
  if askokcancel("Change slice without synching?", "You have
      changes that are not synched with the repository. These changes will
      be lost if you change the slice right now. 
n
nClick OK to change
      slice without synching.", default=CANCEL):
    #then clause
  else:
    #else clause
else:
  #then clause
```

     or if the then and else clauses are large write:
```python
if not synched:
  isok = askokcancel("Change slice without synching?", "You have
      changes that are not synched with the repository. These changes will
      be lost if you change the slice right now. 
n
nClick OK to change
      slice without synching.", default=CANCEL):
  else:
    isok = True

if isok:
  #then clause
else:
  #else clause
```

     Writing the code the first way is hard for someone to read.   The
     second two ways make it more clear that you are relying on the short
     circuit evaluation to perform or avoid the evaluation of the
     askokcancel function.


    Don't use os.popen or os.system

     These are deprecated and we've found bugs in them.   Don't use them!   Use subprocess instead.

    Don't use subprocess.Popen with a string argument (#508).

     Call subprocess.Popen with a first argument that looks like ['command', 'arg1', 'arg2', ...].   Do not use 'command arg1 arg2 ...'!


    Avoid changing directory (#487).
     
     Changing the current directory can cause multithreaded programs to break is scary ways and is usually an indication of bad programming style.   Don't do it!

    Don't use mutable objects as argument defaults (#828).

     If they are modified in the function (or returned and modified outside of the function), the changes persist to future function calls.
     If you want the default of an empty list or dict, for example, use a default of None and then check for this value in the function and
     assign an empty list/dict inside the function.