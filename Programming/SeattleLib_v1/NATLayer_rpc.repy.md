# NATLayer_rpc.repy

This module provides a method of transferring data to machines behind firewalls or Network Address Translation (NAT). NatLayer_rpc.repy is appropriate for a lot of clients, since we can assume that many users are sitting behind firewalls and routers.

### Functions

```
def nat_openconn(destmac, destport, localip=None, localport=None, timeout = 5, forwarderIP=None,forwarderPort=None,usetimeoutsock=False):
```
   Opens a connection to a server behind a NAT.
  
   Notes:

   * destmac is a string identifer for the destination server.
   * destport is the port on the host to connect to.
   * timeout is how long before timing out the forwarder connection.
   * forwarderIP is used if its necessary to force a forwarder to connect to. This will be automatically resolved if None.
   * forwarderPort must be specified if this is forwarderIP is used.
   * usetimeoutsock can be used as a timeout_openconn instead of openconn to connect to the forwarder. WARNING you must include sockettimeout.repy to use this.
   * Returns a socket-like object that can be used for communication. 
   * Socket functions can be used just like the python module. See http://docs.python.org/library/socket.html.



```
def nat_stopcomm(handle):
```
   Stops listening on a NATConnection, which was initially opened by nat_waitforconn.
    
   Notes:

   * handle is the handle returned by nat_waitforconn.
  

```
def nat_check_bi_directional(localip,port,forwarderIP=None,forwarderCltPort=None):
```
   Allows a vessel to determine if they can establish a bi-direction connection with the nat layer

   Notes: 

   * If forwarderIP/forwarderPort are not specified, a forwarder will be automatically selected. They can also be explicitly specified.      
forwarderPort must be a client port.
   * localip is the ip to be used for a temporary waitforconn.
   * port is the port to be used for a temporary waitforconn.
   * Returns True if the client needs to use the nat layer, False if they don't.



```
def nat_waitforconn(localmac, localport, function, forwarderIP=None, forwarderPort=None, forwarderCltPort=None, errdel=None,persist=True):
```
   Allows a server to accept connections from behind a NAT.

   Notes: 

   * If forwarderIP/forwarderPort are not specified, a forwarder will be automatically selected. They can also be explicitly specified. forwarderPort must be a client port.
   * forwarderCltPort is the port for clients to connect to on the explicitly specified forwarder. All forwarder information must be specified if this is set.
   * errdel is used to set the Error Delegate for the underlying multiplexer. See Multiplexer.setErrorDelegate. Argument should be a function pointer, the function should take 3 parameters, (mux, location, exception)
   * persist will be set to true the natlayer will reconnect to another forwarder in the case of failure, this is the recommeneded default 
   * Retuns a handle, which can be used with nat_stopcomm to stop listening.



```
def nat_waitforconn_alive():
```
   Informs the caller of the current state of the NAT waitforconn. i.e. if the multiplexer is still alive. Returns true if the connection to the forwarder is established and alive, False otherwise.    



### Includes

[wiki:SeattleLib/NAT_advertisement.repy]

[wiki:Multiplexer.repy]