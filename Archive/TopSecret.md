# Top Secret

 * TCP over UDP flow control
 * anonymous donation
 * other interactions with Tor project. 

# Documention

See the [wiki:Libraries/Tcup Readme] for instructions for using the library.

# Overview

To begin, this force will focus on multiplexing multiple reliable connections over UDP. This resembles TCP over UDP except (to start with) a single UDP connections is used for multiplexing multiple connections. Later on, this force will shift gears and move towards coordinating with the Tor project to handle anonymous donations by nodes that are running Tor.

If you do not have a sufficient background in networking, you should find a copy of Peter and Davie's 'Computer Networks' book and read the following chapter (listed for the 3rd edition of the book): 1, 2.4, 2.5, 5.1, 5.2, 6.

# Meetings

We meet 12:30-1:30pm on Wednesdays in CSE 314.

# Week 1

 * Implementation of StopAndWaitAssignment in repy
 * Read Chapters 1, 2.4 and 2.5 from Peterson and Davie

# Week 2

 * Mike : 3-way handshake
 * Richard : Sliding window
 * Andreas : complete StopAndWaitAssignment and finish reading
 * Ivan : external repy interface

# Week 3

 * Mike : 3-way handshake integration with Richard's codebase
 * Andreas : Controller class design and implementation for multiplexing and de-multiplexing TCP library connections onto a single internal UDP connection
 * Richard : Convert sequence numbers from numbering packets to numbering bytes. Also, support Mike and Andreas in their interactions with the codebase.
 
# Tasks
 * ~~Congestion control: congestion window, slow start, congestion avoidance~~
 * ~~Ports for multiplexing connections~~
 * ~~Cumulative acknowledgments~~
 * ~~Flow control: sliding window~~
 * ~~seq wrap-around protection~~
 * ~~Three way handshake~~
 * ~~Closing four-way handshake~~

 * Closing three-way handshake
 * Flow control: window scaling (for high bandwidth links)
 * Piggy-backing Acks on data -- extending header
 * TCP timestamps
 * Selective acknowledgments (SACK)
 * RTT estimation (Karn's algorithm and SRTT computation)
 * PMTU discovery for MSS estimate (possible in python/repy?)
 * Benchmarking
   * Performance comparison against vanilla TCP (LAN)
   * Fairness comparison against vanilla TCP (LAN)
   * Scalability


# Implementation details

## Design

 * Describe the Controller class and its purpose
 * Describe the Connection class and its purpose

## Common Classes, Methods, and Exceptions

 * Class Connection
   * Internal state
     * conn
     * remoteip, remoteport
     * localip, localport
     * state_machine
     * timeout, retries, maxdgramsize

   * External methods (API)
     * connect(remoteip, remoteport, timeout)
     * disconnect()
     * send(buffer, length, timeout)
     * receive(maxLen)
     * listen(ip, port, timeout)
     * accept(timeout)
     * bind(localip, localport)

 * Exceptions
   * UnknownStateError
   * NotConnectedError
   * TimeoutError
   * RangeError

# Testing

## Goals
 * Achieve full code coverage (use [figleaf](http://darcs.idyll.org/~t/projects/figleaf/doc/))
 * Integration tests that run across multiple machines
 * Malformed and invalid packet tests

## Unit tests
 * 

## Integration tests
 * A(local, X) = Connect two local endpoints with X TCP streams, then close connection(s).
 * B(local, X) = A(local, X), send data in a single direction (randomize sender) across all TCP streams, then close connection(s).
 * C(local, X) = A(local, X), send data in both directions simultaneously across all TCP streams, then close connection(s).
 * Do A,B,C with remote endpoints
 * Do A,B,C with multiple remote endpoints, 
   * Example: a<->b, b<->c, c<->a.

## Evil tests
 * Send ACKs for unsent data
 * Send inconsistent ACKs (Ack X, then Ack X/2, then Ack X, then Ack X/2, etc)
 * Send more than the advertised window size
 * Send a packet smaller than the TCP header
 * Send a malformed TCP header
   * Data packet without any Data
   * Data packet with wrong number of data bytes specified
   * others?
 * Send a FIN, and then send more data, lots more data

# References
 * [TCP on Wikipedia](http://en.wikipedia.org/wiki/Transmission_Control_Protocol)