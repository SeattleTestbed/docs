# Lisping

 * Porting MapReduce
 * Hadoop integration
 * integration with end applications 

# Overview

The [octopy project](http://code.google.com/p/octopy/) aims to produce a very rudimentary implementation of MapReduce in python. Here is a [blog post](http://ebiquity.umbc.edu/blogger/2009/01/02/octopy-quick-and-easy-mapreduce-for-python/) with some more details of the project. Lisping will concentrate on porting this code to Seattle as a user program. The port should be easy to do as octopy is written in python and is a single file of about 700 lines of code. The next steps for Lisping is to work on numerous improvements to this code to make it more fault tolerant and more useful. The ideal is to reproduce a minimal Hadoop-like service in Seattle.

# Work Completed

 * Replica started!

## Meetings
 * Wednesdays 11:30 - 12:30 in CSE 314

## Timeline

Let's make things arbitrary due on the Thursday of each week to help speed me along!

### February 5th
 * Fully complete a primary - replica - primary map-reduce pipeline
  * Start with simplest case (single job, single reducer)
    * Forget about partitioner
  * Come up with complete protocol

### February 12th

 * Fully complete primary - replica-replica-replica-replica - primary map-reduce pipeline
  * Implement partitioning into replicas, involves the following
    * Asynchronous receiving of map data from other replicas
    * Ability for users to define their own hash for partitioning
  * Implement replica/client list for both primary and replica to keep tabs on each node

### February 19th

 * Fault-tolerance work
  * Enable polling of replica/primary state
    * Shore up protocol work, what differentiates a status request from a data transfer?
    * Primary/replicas have heartbeat, primary keeps track of node state
  * Preliminary fault-mitigation
    * Restart a job on another replica (keep pipeline linear, it can become more efficient later)

### February 26th

 * Fault-tolerance work
  * Improve upon past tasks

### March 5th

 * Finish up map-reduce implementation
 * Start coding a sample map-reduce pipeline to complete a unique task
 * Start documentation on how to use mapred.repy

### March 12th (Due Date)

 * Release on Seattle wiki, explanation of code
 * Release sample application of Beraber map-reduce

