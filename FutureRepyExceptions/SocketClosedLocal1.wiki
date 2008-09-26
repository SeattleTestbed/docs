In the FutureRepyExceptionHierarchy, SocketClosedLocal occurs when a socket is closed, and a user tries calling:

 * `socket.recv()` when there is no more data to be read
 * or `socket.send()`