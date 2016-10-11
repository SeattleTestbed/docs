# Sliding Window Protocol

In this assignment, you will extend the [StopAndWaitAssignment Stop and Wait Assignment] with the [sliding window algorithm](http://en.wikipedia.org/wiki/Sliding_window). The purpose of this algorithm is to enable the sender to use the available network bandwidth more efficiently. This is achieved by sending more than one packet at a time before waiting to receive acknowledgements. This ''pipelining'' of packets makes for a much higher bandwidth communication protocol. 

----

----



## Overview
----

To complete this assignment you must reuse the API specified for the [StopAndWaitAssignment Stop and Wait Assignment] library. You must also submit a client and server programs that stress-test your implementation by sending a lot of data.  Lastly, you will evaluate your implementation and compose a report to describe and explain the performance of your code.



### Extended Reliable API
----

Your protocol should extend the stop-and-wait interface of the library from the [StopAndWaitAssignment Stop and Wait Assignment]. Extend the library by changing the definition of ''reliable_config'' to be:
```python     
reliable_config(maxdgramsize, retries, timeoutinms, windowsize) # No return
```
The **windowsize** argument of this function is optional and restricts the number of messages the client can have pipelined, or outstanding at a time. A window size value of 0 will cause the client to never send a packet. By default, the window size should be set to 3.



### Extended Reliable Client
----

Your client program should take the following arguments:
```
reliable_client inputfile serverhost serverportnum [srchost srcportnum] [maxdgramsize nretries timeoutms windowsize]
```

In the above, ''windowsize'' is an optional argument that specifies the value to be used when calling the ''reliable_config()'' function.



## Step 0: Preparation
----
Read and implement the [StopAndWaitAssignment Stop and Wait Assignment].




## Step 1: Extension
----
Change your stop and wait protocol to implement the sliding window protocol.  The client reads a data file and sends the data to the server in packets of specific size. The client uses a user-defined packet size, and sends multiple packets at time -- enough to fill a ''windowsize'' sized buffer.  When the server receives a data packet, it replies with an acknowledgment (ack) packet, but only if the data packet's message number is the next one in order. Otherwise, the server ignores the data packet.

If an ack message is not received in a user defined number of milliseconds, the client resends the packet. The client will continue to resend the packet a user defined number of times until it receives an ack packet. Once the client receives an ack for the left most packet in its window, it "slides" its window over by one packet, allowing it to send the packet that is now in the right-most point of the window. This process continues until the client sends all of its data.

The server program, receives the data and outputs the data it receives to a file.



## Notes
----

 * **IMPORTANT:** You should number your packets by messages not byte number.
 * As with stop-and-wait, your protocol should run as a library that is included into a client program, **reliable_client.repy** and a server program, **reliable_server.repy**.  You should put your protocol implementation in a file called **reliable.repy** and include it in the client and server programs.  Then, you'll need to pre-process your reliable_client.repy and reliable_server.repy programs.
 * You may find it helpful to run both on the same computer using local code execution during development.   Additionally, you should test on LAN nodes before moving to WAN nodes.
 * You will need to extend your stop-and-wait header from a single alternating bit.  It's okay if your header is variable sized. 
 * When the client receives an ack packet for data packet N, you can assume that the server has received all data packets with message numbers < N.
 * Like with stop-and-wait, your protocol should send the next packet immediately after receiving an ack from the receiver indicating that the window now allows more packets to be sent. Do not rely on sleep() and use locks to achieve this (see the Notes section in the stop-and-wait assignment for more information).



## Extra Credit
----
Try one of these extra credit ideas:
 * Cumulative ACK-ing: save out of order packets.  If the server receives a packet inside the window, the server should keep it around.  Then when the missing packets come, the server should cumulatively process all the packets.
 * Fixed size packet numbering: make your packet numbers wrap-around.  In real protocols, the header has only a fixed number of bits to indicate the packet number. For this, you can use "%", python's modulo operator.
 * Congestion control: implement the [slow start algorithm](http://en.wikipedia.org/wiki/Slow-start).



## What to turn in?
----

Turn in a tar file called "reliable.tar" that contains a directory called Reliable. This directory contains:
 * reliable.repy
 * reliable_server.repy
 * reliable_client.repy
 * results.pdf
 * README

The file results.pdf contains the results of your evaluation. The file called README contains any information we might need in evaluating your solution. For example, bugs and limitations should be included in the README file. 
