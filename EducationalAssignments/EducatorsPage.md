# Educator Portal
This page contains information for educators wishing to use Seattle in the classroom.  We would love for you to tell us about your experiences using Seattle in the classroom. For a quick intro you might also want to watch our [wiki:UnderstandingSeattle/DemoVideo five-minute demo] of Seattle in action! If you have any questions about any of the materials on this page, please contact ``` jcappos -AT- poly -DOT- edu ```



## Networking / Distributed Systems Assignments

### Complete Assignments

The following set of assignments have complete descriptions, and have fully documented instructor solutions. These assignments are geared toward an undergraduate class in networks or distributed systems.

 * The [wiki:EducationalAssignments/TakeHome Take-Home Assignment] introduces [wiki:SeattleShell seash (Seattle Shell)] and teaches about connectivity on the Internet.   This is a great starting point to understand how Seattle can help you in a classroom setting.   It's also a nice demo for classes that don't have programming assignments, but want to illustrate practical networking concepts.

 * The [wiki:EducationalAssignments/StopAndWait Stop and Wait Assignment] has students implement a reliable messaging protocol on top of UDP.   This is a good first assignment in that it is simple to code, but gets students familiar with Seattle and allows them to measure practical Internet properties.  For comparison, Part 1 of [this assignment](http://www.cs.washington.edu/education/courses/461/06wi/HW/HW2/index.html) is a C version of the assignment.

 * The [wiki:EducationalAssignments/SlidingWindow Sliding Window Assignment] is an advanced extension to the Stop and Wait Assignment above.

 * The [wiki:EducationalAssignments/LinkState Link State Routing Assignment] has students implement a link state routing protocol over the Internet.   Students implement Dijkstra's shortest path routing and then apply this to route packets in an attempt to minimize latency.

 * The [wiki:EducationalAssignments/WebServer Web Server Assignment] (based on [this assignment](http://www.cs.washington.edu/education/courses/461/08au/projects/proj2.html)) and [wiki:EducationalAssignments/ChatServer Chat Server Assignment] focus on building applications that use the network.   Students build network applications that run on top of Seattle and understand applications like HTTP and layering of network services.

 * The [wiki:EducationalAssignments/Chord Distributed Hash Table Assignment] has students build a peer-to-peer routing layer.   Students begin by building an implementation of the popular DHT Chord.   This will work well for routing messages over LAN topologies, but will fail in many WAN scenarios due to non-transitive connectivity.   Students then use one-hop detour routing to route around failures.


### Other Assignment Ideas
A more complex set of assignments can also be designed for use with Seattle. The following assignment ideas are intended to show the scope of assignments Seattle can support.


 * Dynamic Resource Acquisition

    This assignment focuses on acquiring and migrating computation. Students are given a simple program that serves a webpage. The students' task is to find the most efficient way to serve the webpage to an initially unknown set of clients. The students begin by implementing a program to load, start and stop programs (similar to the experiment manager) on their nodes. However, a student's program can only acquire a fixed amount of resources across all nodes. The students' goal is to have the webpage served quickly to a set of clients that periodically request the page. The students use DynDNS to register the IP addresses for their nodes with a single hostname. The clients (run by the instructor) look up this hostname and request the page from one of the nodes returned by DynDNS.
    
    This assignment demonstrates that locality is important in distributed data references, and that resources present in the cloud have a cost and must be evaluated. This assignment also builds students' experience with acquiring and migrating resources to handle an unknown client workload.


 * Global Data Store

    Some cloud computing models provide an interface to a global, persistent store (like Amazon's S3 or Google's AppEngine). While Seattle provides local persistent storage, there is no preexisting global store. Such a system can be constructed from a set of nodes that cooperatively replicate and manage data. This project requires that student implementations operate correctly over LAN with multiple readers / writers and gracefully recovers from node failures. For a more difficult project, the global store can be required to run on globally distributed nodes. This extension teaches students to deal with high failure likelihood and to overcome non-transitive connectivity, both of which are typical problems for distributed systems deployed at global scale.


### Project Ideas
Advanced undergraduate and graduate courses in networks and distributed systems can also use Seattle for a class project. Seattle project can involve everything from highly scalable, and complex distributed systems, to measurements of global Internet traffic patterns, to ubiquitous computing topics. The two project ideas below are examples of what such a graduate-level project would entail.

  * [wiki:RepyMapReduce A MapReduce service]

    The MapReduce algorithm harnesses the power of a multiple nodes to parallelize those computations that can be functionally decomposed into some number of map and reduce stages.  Once completed, students would be able to use their implementations of MapReduce for practical compute jobs by simply supplying a map(), reduce(), and hash() methods to their MapReduce service.  An example use of MapReduce is to implement a page-rank algorithm on a large subset of Wikipedia pages to find the “most popular” page.  Using a database dump of Wikipedia’s pages, students can use one MapReduce pass to parse out all internal Wikipedia links and to generate a stem and leaf plot of all pages in Wikipedia.  Using this list multiple MapReduce passes with the page rank algorithm will yield the comparative page rank for every Wikipedia page, creating a flat index that can be made accessible to users through a web server.


  * P2P Data Streaming

    One of the uses for Seattle is as a measurement platform. Because Seattle nodes are spread throughout the Internet, each node offers a valuable vantage point from which to observe Internet activity such as congestion, routing instabilities, outages, and much more. One way to think about Seattle nodes then is as sensors. The nodes generate a constant stream of data about what they observe from their vantage point. It is then up to the researcher to collect this data and process it in a meaningful manner. The database project for this measurement use case of Seattle would involve designing and implementing an infrastructure capable of organizing potentially millions of data streams coming from Seattle nodes in a way that allows the researcher to query the node stream data without needing to aggregate all the data across all time in a centralized manner. This may be done by, for example, delegating stream aggregation to Seattle nodes that have more resources at their disposal, and by constructing a tree structure for Seattle nodes in which the sensing nodes are the leaves of the tree and the researcher is at the root of the tree.

    One concrete application of this project is to process information about the capabilities of the individual Seattle nodes. Seattle nodes have heterogeneous resources -- some nodes have little memory, others have lots of CPU, while still others may have small amounts of available bandwidth. Moreover, all these resources are constantly fluctuating which makes it especially challenging to find nodes that are capable of supporting a particular experiment. Using the P2P streaming engine described above, apply it to aggregating information about the resources available on the Seattle nodes.


  * P2P ACID Databases

   A Seattle service may use millions of nodes, but it may also use hundreds of just a dozen of nodes. Distributed Hash Table (DHTs) are typically used to provide data storage to systems with thousands to millions of nodes. However, for systems comprised of just a dozen nodes, it is simpler and much more efficient to use a database. Traditional databases, however, do not cope well with peer-to-peer environments (e.g. such as in the Seattle platform). In this project, your aim will be to explore, design, and implement a data store organization that combines the advantages of databases with the resilience of DHTs. You will design a database that supports ACID properties, but that can also thrive in a peer-to-peer settings in which nodes join and leave the network unpredictably and in which nodes have disparate resources at their disposal.



## Security / Operating Systems Assignments


 * The [wiki:EducationalAssignments/SecurityLayerPartOne Implementing Security Policies] introduces students to constructing a reference monitor.   A student will implement a simple security policy that is meant to restrict access to files on a system.

 * The [wiki:EducationalAssignments/SecurityLayerPartTwo Attacking Security Policies] follows up on the previous assignment by having students attack the security policies implemented in the previous assignment.   Students get practical experience with how an attacker will try to violate security assumptions in a system.


(More to come!)
