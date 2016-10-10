# parallelize.repy

Seattle provides this parallelization module so it is easy for users to performs actions in parallel to make it easy for a user to call a function with a list of tasks. Usage of this module is purely optional and depends on the programmer's idiosyncrasies. This is not required.

This module is adapted from code in seash which had similar functionality.
	
For the programmer using this module. It's really important to write concurrency safe code for the functions they provide us. It will not work to write:
	
def foo(...):
  mycontext['count'] = mycontext['count'] + 1
	
There must be some form of locking implemented to prevent errors in critical sections!

### Functions

```
def parallelize_closefunction(parallelizehandle):
```
   Clean up the state created after calling parallelize_initfunction.

   Notes: 

   * parallelizehandle is the handle returned by parallelize_initfunction.
   * Returns True if the parallelizehandle was recognized or False if the handle is invalid or already closed.


```
def parallelize_abortfunction(parallelizehandle):
```
   Cause pending events for a function to abort. Events will finish processing their current event.

   Notes: 

   * parallelizehandle is the handle returned by parallelize_initfunction.
   * ParallelizeError is raised if the handle is unrecognized.
   * Returns true if the function was not previously aborting and is now, or False if the function was already set to abort before the call.


```
def parallelize_isfunctionfinished(parallelizehandle):
```
   Indicate if a function is finished

   Notes:

   * parallelizehandle is the handle returned by parallelize_initfunction.
   * ParallelizeError is raised if the handle is unrecognized.
   * Returns True if the function has finished, False if it is still has events running.


```
def parallelize_getresults(parallelizehandle):
```
   Get information about a parallelized function

   Notes:

   * parallelizehandle is the handle returned by parallelize_initfunction
   * ParallelizeError is raised if the handle is unrecognized.
   * Returns a dictionary with the results. The format is {'exception':list of tuples with (target, exception string), 'aborted':list of targets, 'returned':list of tuples with target, return value)}


```
def parallelize_initfunction(targetlist, callerfunc,concurrentevents=5, *extrafuncargs):
```
   Call a function with each argument in a list in parallel

   Notes:

   * targetlist is the list of arguments the function should be called with. Each argument is passed once to the function. Items may appear in the          list multiple times
   * callerfunc is the function to be called.
   * concurrentevents are the number of events to issue concurrently (default 5). No more than len(targetlist) events will be concurrently started.
   * extrafuncargs are the extra arguments the function should be called with (every function called is passed the same extra args).
   * ParallelizeError is raised if there isn't at least one free event. However, if there aren't at least concurrentevents number of free events,      this is not an error (instead this is reflected in parallelize_getstatus)in the status information.
   * Returns a handle used for status information, used above.

### Includes

[wiki:SeattleLib/uniqueid.repy]