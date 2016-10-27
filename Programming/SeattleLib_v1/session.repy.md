# session.repy

This module wraps communications in a signaling protocol. The purpose is to overlay a connection-based protocol with explicit message signaling. Session lets both the sides of the communication send and receive messages over a connected stream.

### Functions

```
def session_recvmessage(socketobj):
```
   Grabs the next message off the socket connection.


```
def session_sendmessage(socketobj,data):
```
   Sends the message to the socket connection.

   Notes: 

   * The protocol is to send the size of the message followed by 
n and then the message itself. The size of a message must be able to be stored in sessionmaxdigits. A size of -1 indicates that this side of the connection should be considered closed.
   

### Usage


```
# connect to the server
mailserversockobj= openconn('www.gmail.com', 2525)
# send my credentials
session_sendmessage(mailserversockobj, 'user:justinc password:12345
n')
# see if it worked
serverresponse = session_recvmessage(mailserversockobj)

def client_connection_callback(ip, port, clientsockobj, mych, mainch):
 # read credentials
 credential_info = session_recvmessage(clientsockobj)

 if credentials_are_valid(credential_info):
   session_sendmessage(clientsockobj, 'OK')
 else:
   session_sendmessage(clientsockobj, 'ERROR: Credentials are invalid!
n')
```


Note that the client will block while sending a message, and the receiver will block while recieving a message. While it should be possible to reuse the connectionbased socket for other tasks so long as it does not overlap with the time periods when messages are being sent, this is inadvisable.


