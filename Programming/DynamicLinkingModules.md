# Dynamic Linking of Modules

One glaring problem for developers new to the repy platform is the lack of any sort of import or dynamic linking functionality.
The current alternative is to put code in separate modules and to use a pre-processor with special directives to statically link code into a final output file. This has a number of problems, such as difficulty of maintenance, security, code size, and redundancy of code. Many modules provide common functionality and are under active development, this means that package maintainers are required to update their code so that the static links are updated and many different programs end up with the same code just copied in.

A solution to this is to provide an import like mechanism that allows code to be dynamically linked at run time, much like vanilla python does.
Dylink is that solution for repy, and it is written as a library around the VirtualNamespace.

----

----

## The dylink module

Dylink is a self-contained repy module that augments the behavior of repy programs and provides new API calls.
To make dylink available, repy is started with dylink.py as the program to run, and the arguments specify the program
to execute with its corresponding arguments. Example:

```
python repy.py restrictions.default dylink.py prgrm args...
```

This allows dylink to initialize itself, and to provide the repy program with the API calls to perform dynamic linking.




## Dylink API

The dylink module provides three main API calls: dy_import_module, dy_import_module_symbols, and dy_dispatch_module.
These are documented separately

When modules are being imported, they have their callfunc set to "import" so that they can specifically
handle that case.




### dy_import_module_symbols

This API call allows a module to export its symbols directly into the current global context.
This is the python equivalent to "from X import *"

This API call takes only a single module argument, and like python the module's name is
specified without any file type suffix. E.g. foo.py is specified as foo. This may cause strange
behavior if there are several files with the same name but different suffixes. 

If you are planning to import a module named foo.py, it is best to not have any other files named
foo, foo.repy, foo.pp or foo.py.repy.

To use this API call, one would do:
```python
dy_import_module_symbols("X") # Same as 'from X import *'
```

This API call takes an additional parameter, which can specify the callfunc to use while importing.
By default, the import will set the callfunc to "import", but this can be specified as the second parameter
to dy_import_module_symbols.




### dy_import_module

This API call initializes a module into a self-contained object, without clutter the current global context.
This is the python equivalent to "import X as Y".

This API call takes the same arguments as dy_import_module_symbols, but it will return a module object.
This module object does not necessarily need to be named the same as the module.

The same warnings apply when importing a module that may have conflicting files.

To use this API call, one would do:
```python

Y = dy_import_module("X") # Same as 'import X as Y'
```

Like dy_import_module_symbols, this API call also takes an optional callfunc parameter.





### dy_dispatch_module

This API call is designed to help implementing repy programs which alter the behavior of other
repy programs. These are called 'repy modules'. Each module or program loaded by
dylink has a special global dictionary called CHILD_CONTEXT defined.

If a repy program wants to behave as a module, it may modify this dictionary and then call
dy_dispatch_module.

This has the effect of reading `callargs[0]`, and treating this as the next module in a chain to load.
dylink will then load that program in, create a VirtualNamespace around it, and evaluate it with
the CHILD_CONTEXT.

Important notes of behavior are:
 * The callfunc of the caller will be automatically set in CHILD_CONTEXT
 * If `CHILD_CONTEXT["callargs"]` is unmodified, then it will be set to `callargs[1:]`, which has the effect of "popping" the first element.

If you want to evaluate the next module with a completely customized context, the dy_dispatch_module() call takes
an optional dictionary which can be used instead of CHILD_CONTEXT. 

To use this API call, one would do:
```python

# Use the CHILD_CONTEXT
dy_dispatch_module() # Same as dy_dispatch_module(CHILD_CONTEXT)

# Use an empty context
dy_dispatch_module( {} )

```






## Changes to Repy

Dylink overrides the default VirtualNamespace object to provide its behavior.
This does not affect the usage of VirtualNamespace in any substantial way, but
it does add an additional optional argument to VirtualNamespace.evaluate().

The standard definition of VirtualNamespace.evaluate() takes only a 
dictionary context. However, the dylink version also has a named parameter
enable_dylink which defaults to True.

If True, then dylink will automatically be setup for that namespace before the evaluation happens. 

If False, then the dylink functions will be deleted from the context, and thus will be unavailable.




## Examples




### Performing Imports

In this example, we will define a library, "foo" that provides a function "bar". Then we will import the module from a test program and invoke "bar".

This will be our definition of foo.repy:

```python

def bar():
  return "Blah!"

```

Now we can use dylink in our test program, test.repy:

```python

if callfunc == "initialize":
  # Import foo, module style
  foo = dy_import_module("foo")

  # Try calling bar and baz
  print foo.bar()

  # Import bar, without a module, ala "from foo import *"
  dy_import_module_symbols("foo")

  # Again, call bar, without foo
  print bar()

```

This demonstrates the essential use of dylink and how it can be used to substitute import in repy programs.




### Defining a Module

In this example, we will define a module, "faster" that causes all sleeps() to return in half the time.
Then we will run a repy program with the module "faster" loaded.

First we will define faster.repy as:

```python

def half_sleep(time):
  # Reduce the time by 1/2
  time = 0.5 * time

  # Sleep by that amount
  sleep(time)

# Force the child to use this by redefining the standard sleep API call
# to instead point to half_sleep.
CHILD_CONTEXT["sleep"] = half_sleep

# Evaluate the next program
dy_dispatch_module()

```

This module redefines the "sleep" call of the next program to instead invoke half_sleep,
and thus alters the behavior of all the following modules and programs.

To invoke repy with this module we use:
```
python repy.py restrictions.default dylink.py faster.repy test.repy
```

Where test.repy is the final program to run.


