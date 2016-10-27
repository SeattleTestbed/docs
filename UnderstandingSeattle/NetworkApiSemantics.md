

----
## Introduction and Purpose


This page is designed to specify in detail the behaviour of network API calls under various circumstances.  Each call and it's possible interactions are explained.  

For a basic description and understanding of the API calls first see [wiki:RepyApi]

----
## Abstractions

To aid in the description of call interactions I will define some useful abstractions.  The repy environment may or may not be implemented using these abstractions, but they are useful mental constructs for considering call behaviour.

''tcp_conn_table'' - a table with columns localip,localport,remoteip,remoteport for all open tcp connections

''tcp_listen_table'' - a table with columns localip,localport for all tcp listeners

''udp_listen_table'' - a table with columns localip,localport


----
## openconn


A call to openconn will attempt to establish a TCP connection to a remote host.  The call will either return a socketlike object, or raise an exception (in the case of failure).  If the connection is successful an entry is placed into the ''tcp_conn_table''.

To know the result of a call to openconn we must consider:


1. Is there a conflicting tuple in the ''tcp_conn_table''.  A conflicting entry is one where all columns match.

2. Are sockets resources available

3. Can network connectivity to the remote host be established

4. will the host accept the connection

5. Will the connection be established within the timeout value

The result of a call to openconn is:


```
if (not matching entry in tcp_conn_table) AND 
      (sockets available) AND 
      (network connectivity to host can be established) AND 
      (the remote host accepts the connection) AND 
      (the connection can be established before the timeout expires):
  
  place an entry into tcp_conn_table
  return a socekt_like_obj
else:
  raise an exception
```

----
## waitforconn


A call to waitforconn will attempt to register a callback function and begin listening for TCP connections at the specified local ip and port.  A free event will be used for a socket selector thread (no free event is consumed if the socket selector thread is already running from a previous waitforconn)  A successful call to waitforconn will return a commhandle, a failed call will result in an exception.

To know the result of a call to waitforconn we must consider:

1. Is there a conflicting tuple in the ''tcp_listen_table'', a conflicting entry is one where all columns match.

2. Is there a connection to the network

3. Are there free events OR is the socket selector already running


The result of a call to waitforconn is:


```

if (there are free events OR the socket selector is running) AND (there is a network connection):
  if no matching tuple in listen table:
    make entry in listen table
    start the listener and register the callback function
  elif:
    replace the callback function
  return a commhandle
else:
  raise an exception
```


After effects:

Once a callback function has been registered a thread runs to listen for connections, whenever a tcp connection is established the resulting socketlikeobj is processed by the user specified callback function.  If there are no free events available when a connection is established the callback function will not be called until an event is available.


----
## stopcomm

A call to stopcomm will stop the listener and remove the entry from the corresponding listen table.  True is returned for success and False for failure.

----
## sendmess


A call to sendmess will attempt to send a message to a  remote host.  The call will either return the number of bytes sent, or raise an exception (in the case of failure).

To know the result of a call to sendmess we must consider:

1. Is there a connection to the network
2. Can the host name specified be resolved

The result of a call to sendmess is:


```
if (there is a network connection) AND (the host name can be resolved):
     send the packet
     return bytes sent
else:
  raise an exception
```

----
## recvmess


A call to recvmess will attempt to register a callback function and begin listening for arriving messages at the specified local ip and port.  A free event will be used for a socket selector thread (no free event is consumed if the socket selector thread is already running from a previous recvmess)  A successful call to recvmess will return a commhandle, a failed call will result in an exception.

To know the result of a call to waitforconn we must consider:

1. Is there a connection to the network

2. Are there free events OR is the socket selector already running

The result of a call to recvmess is:

```

if (there are free events OR the socket selector is running) AND (there is a network connection):
  if no matching tuple in listen table:
    start the listener and register the callback 
    return a commhandle
else:
  raise an exception
```


After effects:

Once a callback function has been registered a thread runs to listen for connections, whenever a message is received it is processed by the user specified callback function.  If there are no free events available when a message is received the callback function will not be called until an event is available.

----
# Socket Objects

see bottom of page for state diagram.

----
## socket.send(bytes)

A call to send will attempt to transmit bytes to the remote host connected via the stream abstraction.  A call to send will either block waiting for the underlying network stack to accept the bytes, or will return the number of bytes successfully delivered to the underlying network stack.  

----
## socket.recv(n)

A call to recv will attempt to return to the application n bytes delivered over the stream abstraction.  The call will either block waiting for bytes to be delivered from the underlying network stack, or will return <= n bytes from the stream.

----
## socket.willblock()

A call to `willblock` determines if calls to `recv` or `send` will block or not.  A tuple of the form `(Bool, Bool)` is returned indicating if `recv` and `send` will or will not block. (`True for blocking, `False for non-blocking)

----
## socket.close()

A call to close completely closes the local end of the stream abstraction.  After calling close the local socket will raise an exception on any class to send or recv.  The remote end of the socket will still be able to call recv until all data previously delivered is read.  

----
## Socket State Diagram

[[Image(socketstate.jpg)]]







