# Chainload-able Modules (Old, Obsolete)

The chainloader system was designed to conveniently provide behavior altering modules.
The main problem is how to provide a generic method of loading various bits of code that
want to alter the behavior of the repy program or to make new API functions available. Instead of having each module provide lots of boilerplate code that is potentially buggy and hard to debug, all the generic code to handle building up the context of the repy program is handled by the chainloader, allowing modules to focus on their little snippet of functionality.

----

----

## Chainloader Specific's
When a module is loaded by the chainloader, a module must behavior in a certain manner.
A module can also make certain assumptions that the chainloader guarantees.

As a general rule:
 * callfunc will be set, and its value is "initialize" on import
 * _context will point to global context dictionary
 * mycontext will be provided as an empty dictionary
 * There will be two special dictionaries MODIFIED_API and HOOKS

The MODIFIED_API dictionary tells the chainloader what the module intends to modify,
and accordingly updates the context that the repy program will execute in. You can either
override existing functions, e.g. API functions, or provide new functions.

The HOOKS dictionary allows modules to hook into certain events, and alter behavior.
There are the following hooks:
 * "start": Allows a module to impose on starting the main namespace. The value of `HOOKS["start"]` should be a function which takes a VirtualNamespace object and a dictionary context. The module should then return a VirtualNamespace and dictionary context. These can be the same,
or they may be modified and returned.

In terms of behavior, the following is a guideline:
 * Minimize time blocking execution (e.g. hurry up!)
 * Use a separate thread for long running tasks/computation, do not block on import or on the hooks
 * No need to worry about using mycontext, or cluttering a namespace, the module namespace is isolated
 * ONLY things in MODIFIED_API will be propagated to the repy child, and this is only done during the module import. E.g. changing openconn in your own context won't do anything, unless you explicitly put it in the dictionary.



## Examples


### Modifying an existing API call

Here is a simple module that interposes on calls to "sleep" and prints the runtime when sleeping and waking up.

```python

def new_sleep(time):
  print "Sleeping @ ",getruntime()
  sleep(time)
  print "Waking @ ",getruntime()


if callfunc == "initialize":
  MODIFIED_API["sleep"] = new_sleep

```

The module defines a new function called "new_sleep", and by setting a key in MODIFIED_API the chainloader will now use new_sleep for any call to sleep in the repy program.



### Adding a new API call

This simple modules adds a new API function called "loggit" which can be used for logging.

```python

# Name of the log file
LOG_FILE = "log." + getruntime() + ".txt"

def log_mesg(mesg):
  # Get the file handle
  fileh = mycontext["fileh"]

  # Write the time and the message
  fileh.write(getruntime() + " " + mesg)


# Initialize the module
if callfunc == "initialize":
  # Open the file
  mycontext["fileh"] = open(LOG_FILE, "w")

  # Make the loggit call available
  MODIFIED_API["loggit"] = log_mesg

```

Here the module opens a file, as defined by LOG_FILE, and stores the handle in mycontext as "fileh".
On every call to "loggit" in the program the log_mesg function gets called and logs the output to the file along with a timestamp.



### Using hooks

This simple module adjusts getruntime so that time 0 is when the main module was evaluated.

```python

def time_since_start():
  # Get the time the repy program was started
  start = mycontext["start"]

  # Subtract the program's start time from the processes start time
  return getruntime() - start  


def starting(virt, context)
  # Store the start time
  mycontext["start"] = getruntime()

  # Return everything unmodified
  return virt,context


# Setup
if callfunc == "initialize":
  MODIFIED_API["getruntime"] = time_since_start
  HOOKS["start"] = starting

```

This module hooks into the start sequence, and inside of "starting" store the current runtime. This time is used in "time_since_start" to return the time since that start sequence.
This way, when the repy program calls getruntime() it provides a more accurate measure of how long the actual program has been running, rather than the process.






