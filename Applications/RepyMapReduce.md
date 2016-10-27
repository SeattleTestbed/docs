# A MapReduce service
The original MapReduce framework was designed and developed by Google to support large-scale distributed computing on large amounts of closely-networked computers.  The main drive for the MapReduce framework stem from the intrinsic benefits of functional programming, more specifically the map() and reduce() functions.

There are 3 main steps in a MapReduce run.

 1. Map step: data received by the worker is tossed into a map() function that will emit key-value pairs based on each aliquot of data.

 2. Partition (or shuffle) step: The generated key-value pairs from map() are hashed by its key to a particular worked and sent off.  If a key ends up on a particular work at the end of the partition phase, it is required that all other key-value pairs with the same key also be on the same host in order for the reduce step to work properly.

 3. Reduce step: The collected key-value pairs are collected into a key, value_1, value_2, ..., value_n list and can do computation to reduce the expanded data down to a useful conclusion.

This computation can be performed on an arbitrary number of worker machines, making it scalable to nearly all sizes of computing clusters!  MapReduce frameworks often have a primary node delegating tasks to workers, organizing and distributing the initial data, and acting as a mediator in fault situations.

More detail on the use of MapReduce is available from [Google's 2004 OSDI paper](http://research.google.com/archive/mapreduce-osdi04.pdf) or an open-source implementation of MapReduce in Java: [Hadoop](http://hadoop.apache.org/core/).




-----
**These assignments are a work-in-progress, please e-mail our developer list for more information! **





## Stage 1: A simple implementation of MapReduce

To start out, students will make the base framework of a MapReduce application: a primary node that delegates a task to its workers (also called peers), and a single peer that takes the data given to it by the primary, performs a map pass and a reduce pass on the data, and eventually passes that data back to the primary for post-processing.  This assignment will require the need to implement a simple message-passing protocol, and abstract the functionality of the map() and reduce() methods.

Sample Assignment: [wiki:EducationalAssignments/SimpleMapReduce Simple MapReduce Assignment]

## Stage 2: Adding partitioning and support for multiple worker nodes

In the second stage of the project, students will work to increase the number of peers their system supports and will implement the partitioning algorithm to enable map data-passing between the MapReduce peers during the shuffle phase. By implementing the partitioning method, the primary invariant of MapReduce must be maintained at all times: all keys, no matter what their origin node, must be sent to the same reducer during the reducing stage. By adding the partition algorithm to the peers simple parallelism is achieved in this assignment.

## Stage 3: Adding fault tolerance

In large distributed systems failures are common and recovering from failures is a basic necessity. In the final stage of the project students will add fault-tolerance to their systems. The primary node will implement a scoreboard to track all system state by using a regular heartbeat mechanism to query each peer and will perform an action whenever it detects that a job is failing to complete or that connectivity between peers is lost. An action by the primary might be to allocate a new peer to an existing job, or to perform a restart of a job that failed beyond recovery. To accomplish this, students must implement a control protocol that the primary can use to communicate changes to the MapReduce job to the peers whenever failures occur. Additionally, students will implement a distributed failure detector in which the peers will communicate with each other to detect node failures and report these failures to the primary.

[[Image(stage3.PNG)]]


**Figure 1:** Example MapReduce implementation on Repy, showing both control and data flow.