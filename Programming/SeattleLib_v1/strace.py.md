# strace.py

This namespace can be used as an intermediary logging namespace to log calls to the Repy API functions. Essentially this allows a user or a client to trace his or her calls. Repy bases a lot of functionality off this.


### Classes & Functions


```
def traced_call(self,name,func,args,kwargs,no_return=False,print_args=True,print_result=True):
```
   Traces the function call.


```
class NonObjAPICall():
```
   Used for API calls that don't return objects


```
class SocketObj():
```
   This class is used for socket objects.


```
class LockObj():
```
   This class is used for lock objects


```
class FileObj():
```
   This class is used for file objects


```
def wrapped_openconn(*args, **kwargs):
```
   Wrap the call to openconn, tracing the call as well.


```
def wrapped_waitforconn(*args, **kwargs):
```
   Wrap the call to waitforconn, tracing the call as well.


```
def wrap_all():
```
   Wrap all the API calls so they can be traced