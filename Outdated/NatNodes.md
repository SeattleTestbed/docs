# Bringing NAT NODES into the Testbed



----

## What are NAT NODES

Our testbed is made up of donated resources from around the world, giving us a testbed that models the behavior of the real Internet.  As such some of the nodes of our testbed are behind middle boxes such as Network Address Translators and Fire walls.  

For testbed users to be able to acquire and use VMs we need to open connections to the controlling node manager.  If the node manager is behind a middle box this can be a problem.  To ensure such connectivity is possible we use a NAT Forwarding technique.
----
## NAT Forwarding in the Seattle Testbed

NAT Forwarding is a method used to gain bi-directional connectivity in the presence of a middle box.  NAT nodes can open outgoing connections, but may experience troubles when listening for incoming connections. The process takes place in 6 steps.

1. Using the NAT forwarding library, a node that would normally listen for an incoming TCP connection (a server) will instead actively open a connection to an intermediate node (a forwarder).  This TCP connection persists for as long as the server needs to listen for connections.

2.  The NAT forwarding library on the server application advertises a key (unique identifier for the node) and the connection information (an IP and port) for the forwarder.

3.  A testbed user who wants to access a VM will use a client application to do so.

4. The NAT forwarding library on the client application will look up the key corresponding to the server (node manager) it wants to connect to and obtain connection information for the forwarder. The client then establishes a TCP connection to the forwarder.

5. The forwarder receives a connection request from the client, and passes the request to the NAT forwarding library on the server.  The server establishes a new connection to the forwarder.  The forwarder then begins transparently passing traffic between the client and server.

6. The NAT forwarding library on both the client and server applications passes a TCP-socket object up the application, the socket provides a "virtual" TCP connection, with the forwarder invisible to the application itself.  

----
[[Image(NatNodes.jpg)]]
----

## Intermittent connectivity / IP address changes

Some node managers may experience intermittent connectivity and may change their IP address over time.  Since the NAT forwarding library on the server advertises a unique key (and not the current IP address) clients looking to connect to the server will always be able to find the server using the server's key.  This solution won't help if a connection is lost during communications, but client / server programs should already be able to deal with connection loss and need only reconnect to continue operating.  

----

## Forwarder Deployment

Many Forwarders are deployed and managed as a service on the Seattle testbed.  Each forwarder advertises its location under a common identifier in a DHT.  When servers need to connect to a forwarder the NAT forwarding library uses the DHT to get a list of all active forwarders and chooses one to connect to.  The forwards themselves are written in repy and run inside of VMs on testbed nodes.

----


## Performance

Passing all traffic through an intermediate node does have an impact on performance.  The NAT forwarding solution described here is only used in the testbed to exchange control messages with the node manager, so the performance penalty is far less important than reliable communication.  Additionally only nodes that can not be contacted directly will use the forwarding service (see section below).  Programs running inside of a VM will not be affected as the NAT forwarding layer does not automatically impose itself on VM communications.  Those who want their programs running in a VM behind a NAT or firewall to have bi-directional connectivity can make use of the NAT forwarding service / library, or write their own solution if better performance is required.

----

## Deciding

Only nodes that can not be contacted directly will use the forwarding service.  Before the node manager starts listening for a connection a test is performed to determine if outside parties are able to connect to the node.  If bi-directional connectivity is available the NAT forwarding library is not used.
----

## Using the VMs on NAT Nodes

VMs on Nat Nodes can be used exactly like any other VM in the testbed, but traffic to and from vessel may not get through due to the middle box.  This is actually an important part of the testbed as we want vessels that truly model the behavior of Internet nodes.  So vessels behind NATs will act just like computers on the Internet behind NATs.  NAT nodes are easily identifiable in the testbed so if you don't want to use them, or if you want to use the forwarding library in your vessel, that's easy to do.
