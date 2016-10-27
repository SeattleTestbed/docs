# Potential Seattle Services
----

What follows is a variety of cooperative P2P libraries and services that may be implemented on top of Seattle. These are lightweight enough to be supported by nodes running Seattle nodes, and which can provide non-trivial and useful functionality to developers of distributed systems. As long as the node runs Seattle, these services are available locally to the developer

## WAN P2P environment
----
 * Detour routing
    A failure detection service that provides higher routing reliability during outages and routing mis-configurations.

 * Unique forms of file transfer
    BitTorrent swarming to provide efficient distribution of large files among multiple nodes.

 * Multi-flow transfers
    Stream data between hosts over multiple UDP channels to reduce loss rates (ala Skype)

 * Tor routing
    Anonymous routing via the Tor network.

 * NAT traversal
    UDP and TCP whole punching to access nodes behind middle boxes.

 * Structured Streams
    Lightweight TCP tunneling over UDP

 * Peer selection
    Select peers based on their network properties, such as latency and throughput using iPlane nano.

 * Hidden service advertisement
    Use Tor's hidden service feature to advertise a service without disclosing its location

 * Mobility / Tracking support
    Find a host as it changes IP addresses


## LAN/WAN environment
----
 * Computation
    Facilitate large scale distributed computation tasks using MapReduce.

 * Consistency primitives
    Take advantage of Paxos, two and three phase commit distributed algorithms to organize nodes and synchronize distributed state machines.

 * Transactions support
    Use transactional semantics of BEGIN/ROLLBACK/COMMIT and some number of operations in between. With file logging for durability.

 * IPv6 support
    Transparently support IPv6 traffic

