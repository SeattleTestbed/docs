# Seattle Backend
This page describes how Seattle works. It describes the distinct states that each node can be in, as well as describes the transitions between the different states.






## Node States
----
Every node can only be in one state at a time.  Each clearinghouse has a unique set of public keys that are used to mark which state a node is in.  A node advertises to the advertise service underneath a public key to mark itself as being within a specific state.  i.e. if node 12.34.56.78:1224 is in the canonical state, if you perform a lookup to the advertise service using the clearinghouse’s canonical public key, you will find 12.34.56.78:1224.  This is how the Clearinghouse identifies which nodes are in which state.  A list of all the different states are provided below, with a short description of what they mean.



### acceptdonation
This state indicates that the user has just installed Seattle on this node.  The Clearinghouse has not yet contacted this node to insert the node’s data to the clearinghouse database, i.e. credit its donated resources to a user.



### canonical
Canonical is an important state, as nodes in this state are ready to be used, and can now be split into separate VMs.  In case an error occurs, nodes also fall back to this state.



### movingto_canonical
This state is used to identify nodes that are transitioning to the canonical state.



### movingto_twopercent
This state is used to identify nodes that have been split into VMs containing 2% resources each.  Nodes in this state are transitioning to the two percent state.



### twopercent
VMs are ready to be acquired in this state.  The node has been split into VMs, each containing 2% of the node’s resources.  Once a node reaches this state, it will remain in this state regardless if it has been acquired or not.



### user public key
Although it does not quite fit the same definition of “state” as the other keys do, it is used to identify if a node has any VMs for a particular user.  If a node is found advertising under a user’s public key, then the node has a VM that is acquired by the user.  The list of user public keys for a particular Clearinghouse is maintained within the Clearinghouse’s database.



### Unused States
These states were previously used, but are no longer in use since late 2012. For clearinghouses dating back earlier, there is a small chance that it will still find nodes advertising these keys.
 * onepercent
 * onepercentmanyevents
 * movingto_onepercentmanyevents
 * movingtoonepercent





## Normal Node State Transitions
----
The following diagram shows the states that a node should transition between during normal execution.  

[[Image(Node States.svg)]]





## Active Seattle Clearinghouse Components
----
These scripts must be running on the production Clearinghouse at all times.  They should be started as user root in a screen by running 
seattlegeni
deploymentscripts
start_seattlegeni_components.sh
 * lockserver_daemon.py
 * backend_daemon.py
 * check_active_db_nodes.py
 * transition_donation_to_canonical
 * transition_canonical_to_twopercent
 * transition_twopercent_to_twopercent
 * transition_onepercentmanyevents_to_canonical