# sockettimeout.repy


sockettimeout.repy is a library that causes sockets to timeout if a receive / send call blocks for more than an allotted amount of time. It implements this by using the Repy openconn, waitforconn, and stopconn functions.

### Classes & Functions


```
class _timeout_socket():
```
   Provides a socket like object which supports custom timeouts for send() and recv().


```
def timeout_openconn(desthost, destport, localip=None, localport=None, timeout=5):
```
    Returns a socket object for the user. Same as the Repy openconn.


```
def timeout_waitforconn(localip, localport, function, timeout=5):
```
    Wrapper for the Repy waitforconn.


```
def timeout_stopcomm(commhandle):
```
    Wrapper for the Repy stomcomm function.


### Usage

```

"""
# hello world
include sockettimeout.repy


def mycallback(ip, port, sockobj, commhandle, listenhandle):
  try:
    # This should hang until it times out.
    sockobj.recv(100)
  except SocketTimeoutError:
    pass
  except:
    raise
  else:
    raise Exception("No SocketTimeoutError raised by sockobj.recv()")
  
  
def server():
  commhandle = timeout_waitforconn(getmyip(), 12345, mycallback)


def client():
  sockobj = timeout_openconn(getmyip(), 12345)
  # The timeout on the socket the callback gets is 5 seconds. We want to
  # avoid the socket being closed because we lose the reference to it. 
  sleep(10)
  # The client never sends anything.


def main():
  server()
  client()
  sleep(.1)
  exitall()


if callfunc == 'initialize':
  main()
```

