# Virtual Namespaces

## Description

A virtual namespace is an abstraction around an arbitrary code string that has been evaluated for safety. A virtual namespace allows for executing code any given global context.
The code for each virtual namespace is vetted by a static code safety check, and then is an immutable part of the virtual namespace.

## API

A virtual namespace supports the following:

1.  Constructor
  * Two primary components, the code and the name.
  * Code must be given as a string.
  * A custom name can be provided, or "<string>" is used. The name is what is used when printing a stack trace,
    and can help debug in which file an error occurred. This is useful when stacking namespaces, or having other
    complicated interactions between namespaces.

2. evaluate()
  * Evaluates the code in the namespace with a provided global context. This context must be a SafeDict or dict object.
    dict objects are automatically converted to SafeDict object's, which prevent unsafe global keys from being used.


## Examples

How to implement "from X import foo":
```
   # Read in the code
   code = open("X.py").read()

   # "import" X.py as a module
   virt = VirtualNamespace(code, name="X")

   # Evaluate the module in our current global context
   virt.evaluate(_context)

```


How to emulate python eval():
```
  # Code string to evaluate
  strValue = "result = 123 * 2"

  # Get a new virtual namespace
  virt = VirtualNamespace(strValue)

  # Evaluate the code in an empty context
  virt_context = virt.evaluate({})

  # Extract the value of result
  result = virt_context["result"]

```


## Overriding the default API to provide different behavior

In this example, we will create 2 virtual namespaces, which call sleep() and then exitall().
However, we have modified exitall() so that repy will not exit until there are 2 calls to it.

```

# Copy our context for virt1 and virt2
context1 = _context.copy()
context2 = context1.copy()

# How many calls to exitall()
mycontext["exit_count"] = 0

# Wait for 2 calls before calling exitall()
def waitforboth():
  # Increment
  mycontext["exit_count"] += 1

  # Exit if necessary
  if mycontext["exit_count"] == 2:
    print "Exiting!"
    exitall()

if callfunc == "initialize":
  # Create two virtual namespaces to call exitall()
  virt1 = VirtualNamespace("sleep(0.5)
nexitall()")
  virt2 = VirtualNamespace("sleep(1.0)
nexitall()")

  # Re-map exitall to call waitforboth, then evaluate
  context1["exitall"] = waitforboth
  context2["exitall"] = waitforboth

  virt1.evaluate(context1)
  virt2.evaluate(context2)  

  # We should never get here
  print "Not here!"

```


So although the new virtual namespaces (virt1, virt2) have a function which looks the same as exitall() provided by repy, its behavior has been changed by the main namespace. This allows for chaining of namespaces that alter and improve behavior, as well as providing functionality such as logging and performance monitoring.


## Executing different code in the same context

It is possible to execute different code strings while sharing the same context. This might be useful for evaluating dynamic code strings in the current namespace as is done in this example:

```

if callfunc == "initialize":
  # Set RESULT = 1
  RESULT = 1

  # Create a new namespace
  virt1 = VirtualNamespace("RESULT = 5")

  # Print the result pre and post evaluation
  print RESULT
  virt1.evaluate(_context) # Evaluate in our context
  print RESULT

```

The output here is:

```
1
5
```

In this example, we create a new virtual namespace with a different code string from what is currently executing, but sharing our same context.
This allows the new namespace to manipulate our globals as its own.





