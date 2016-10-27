# Importing Repy Code to Python: The ```repyhelper``` module



## Introduction
----

As repy is currently implemented, the only way to make use of repy code from within the context of python is to use a combination of the repyportability module and .mix files. .mix files require preprocessing, which quickly becomes cumbersome during development. 

In order to ease the pain of porting repy to python, the ```repyportability``` module was created. It's intended to do away with .mix files, and provide a simple interface for making use of repy code within python. 

----

----



## API
----

The following are defined in the repyhelper module:



### translate
----
```
  <Purpose>
    Translate a Repy file into a valid python module that can be imported by
    the standard "import" statement. 
    
      Creates a python file correspond to the repy file in the current directory, 
    with all '.' in the name replaced with "_", and ".py" appended to it to make
    it a valid python module name.
    Performs several checks to only perform a translation when necessary, and to 
    prevent accidentally clobbering other files.    
      The repyhelper and repyportability modules must be in the module path for the
    translated files
      Note that the optional arguments used to set variables are only inserted if 
    the file is retranslated--otherwise they are ignored.
  
  <Arguments>
    repyfilename:
      A valid repy file name that exists. 
    shared_mycontext:
      Optional parameter whether or not the mycontext of this translation should 
      be shared, or the translation should have it's own. Default True
    callfunc:
      Optional parameter for what the callfunc of this translation should be.
      Should be a valid python string. Default "import"
    callargs:
      A list of strings to use as the repy's "callargs" variable. Default empty list.
      
  <Exceptions>
    TranslationError if there was an error during file generation
  
  <Side Effects>
    Creates a python file correspond to the repy file, overwriting previously 
    generated files that exists with that name
  
  <Returns>
    The name of the Python module that was created in the current directory. This
    string can be used with __import__ to import the translated module.
```

  

  ==== Example 1 ====
  Import a python file using the "from X import *" syntax, which will result in scoping similar to repy includes. Say foo defined the function bar:
  ```python
import repyhelper
repyhelper.translate("foo.repy")
from foo_repy import *
bar()
  ```



#### Example 2
  Import the file foo.repy to the local namespace as the module foo. Say foo defined the function bar:
  ```python
import repyhelper
module_name = repyhelper.translate("foo.repy")
foo = __import__(module_name)
foo.bar()
  ```




### translate_and_import
----
```translate_and_import``` is to simplify the ```translate``` interface even more, by performing the actual import as well. ```translate_and_import``` results in the same behavior as a .mix file's include would; the file gets imported, and all of it's defined functions/variables are then visible in the current global scope.

```
  <Purpose>
    Translate   a repy file to python (see repyhelper.translate), but also import
    it to the current global namespace. This import is the same as 
    "from <module> import *", to mimic repy's include semantics, in which
    included files are in-lined. Globals starting with "_" aren't imported. 
    
  <Arguments>
    filename:
      The name of the repy filename to translate and import
    shared_mycontext:
      Whether or not the mycontext of this translation should be shared, or
      the translation should have it's own. Default True
    callfunc:
      Optional parameter for what the callfunc of this translation should be.
      Should be valid python string. Default "import"
    callargs:
      A list of strings to use as the repy's "callargs" variable. Default []
    preserve_globals:
      Whether or not to preserve globals in the current namespace.
      False means globals in current context will get overwritten by globals
      in filename if the names clash, True means to keep current globals in the
      event of a collision. Default False
  
  <Exceptions>
    TranslationError if there was an error during translation
  
  <Side Effects>
    Creates/updates a python module corresponding to the repy file argument,
    and places references to that module in the current global namespace 
  
  <Returns>
    None
```



#### Example 1
Say foo.repy defined the function bar:
  ```python
import repyhelper
repyhelper.translate_and_import('foo.repy')
bar()
  ```

#### Example 2
Say foo.repy defined the function bar:
  ```python

def bar():
  pass

import repyhelper
repyhelper.translate_and_import('foo.repy', preserve_globals=True)
bar() #calls the bar defined above, not foo.repy's bar
  ```

#### Example 3
Each library must include any functions that it uses, even if they will be included elsewhere.   If you have the following three files, you will see a NameError when calling ```foo_foobar()``` because ```b.repy``` does not include ```a.repy``` but uses it.

```python
justinc@nara:~/test> cat a.repy
def a_foo():
  print "hello"
justinc@nara:~/test> cat b.repy
def b_bar():
  a_foo()   # OOPS, needed to include a.repy
justinc@nara:~/test> cat foo.repy
include a.repy
include b.repy

def foo_foobar():
  a_foo()
  b_bar()

justinc@nara:~/test> python
Python 2.5.2 (r252:60911, Dec  1 2008, 18:10:01)
[GCC 4.3.1 20080507 (prerelease) [gcc-4_3-branch revision 135036]] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import repyhelper
>>> repyhelper.translate_and_import('foo.repy')
>>> foo_foobar()
hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "foo_repy.py", line 21, in foo_foobar
    b_bar()
  File "b_repy.py", line 17, in b_bar
    a_foo()
NameError: global name 'a_foo' is not defined
>>>
```



### set_shared_context(context)
----
By default, translated repy modules share the mycontext dictionary. It's initially empty, but can be assigned using ```set_shared_context```. Note that this completely overwrites whatever the shared mycontext dictionary previously held. 

```
  <Purpose>
    Set the shared mycontext dictionary
  
  <Arguments>
    context:
      A dict to use as the new mycontext
  
  <Exceptions>
    TypeError if context is None
  
  <Side Effects>
    Reassigns the shared_context dict to be context
  
  <Returns>
    None
 ```




### TranslationError
----
If an error occurs during translation, a ```TranslationError``` will be raised. The cause of the error will be included in the message string, but is usually caused by an error locating or reading from the file, or finding unexpected input.





### set_importcachedir
----
```
  <Purpose>
    Repyhelper creates Python versions of repy files.   This function sets
    the location where those all files will be stored.   By default, files are 
    stored wherever they are found in the python path.   If a relative path
    name is specified, by default, files are instead stored in the first 
    directory in the Python path sys.path[0] (usually the current directory)
  
  <Arguments>
    newimportcachedir:
       The location where all files should be stored.   Use None to restore 
       the default behavior

  <Exceptions>
    TypeError if the path is invalid.
    ValueError is thrown if the newimportcachedir isn't in the path
  
  <Side Effects>
    None.
  
  <Returns>
    None.                            
```

  


For all examples, let's assume our ```sys.path``` for modules looks like ```['.', '/usr/lib/repy', '/usr/lib/python2.5', '/tmp']```.
  ==== Example 1 ====
  By default, modules without path information are written into their directory.
  ```python
import repyhelper
module_name = repyhelper.translate_and_import("foo.repy")
# A file foo_repy.py is written to /usr/lib/repy

  ```



#### Example 2
  When given path information, the files are written into ```sys.path[0]```
  ```python
import repyhelper
module_name = repyhelper.translate_and_import("/usr/lib/repy/foo.repy")
# A file foo_repy.py is written to the current directory
  ```



#### Example 3
  The location of these files can be controlled with ```set_importcachedir```
  ```python
import repyhelper
repyhelper.set_importcachedir('/tmp')
module_name = repyhelper.translate_and_import("foo.repy")
# A file foo_repy.py is written to /tmp
  ```




#### Example 4
  A call to ```set_importcachedir``` also changes the location of files with paths.
  ```python
import repyhelper
repyhelper.set_importcachedir('/tmp')
module_name = repyhelper.translate_and_import("/usr/lib/repy/foo.repy")
# A file foo_repy.py is written to /tmp
  ```
