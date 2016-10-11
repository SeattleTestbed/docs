# Sleight Of Hand

 * NAT traversal
 * IPv6
 * DHCP support 

# Overview

This team focuses on peer-to-peer communication with the server (data multiplexing/demultiplexing and nameserver). Its main goal is to implement the software on Windows Mobile for communicating the nameserver and the other phone as well as the software on the data server for NAT traversal (simply data forwarding in the server). There are two components to the software (server and client) running on the virtual machine available in the handheld device. (Please look at the first attachment.)

The most challenging part is to make the protocol between phones, data server and nameserver. Implementation will be divided to client on the phone, server on the phone and data server. Below is the detail assignment to the person each. 

 * Making the protocol and then its implementation on the phone and the data server
 * Data multiplexing/demultiplexing (simply data forwarding) over a channel on the data server
 * Find the data server and update the location on the phone 

[[Image(NAT_traversal.jpg)]]

# Meetings

Tuesdays 3:30-4:00pm. 

## Milestone 1

Working NAT layer.   

Dennis: look up / advertisement for forwarder and server.

Armon: protocol for multiplexing connections.

Eric: forwarder logic.



## Milestone 1 cleanup

Dennis:   Allow connections on different ports, intelligently choose from multiple forwarders, error conditions for current code.   

Armon:   Separate out the connection multiplexing code (ask Richard), ??MAC addresses??, error messages should be the same as openconn / waitforconn. 

Eric:    Forwarder with separate sockets, limits on the forwarder, sleeps go away.