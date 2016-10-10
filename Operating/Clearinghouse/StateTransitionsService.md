# State Transition Daemons

The state transition daemons track node configuration state. Primarily they are responsible for configuring a new Seattle installation for use by the GENI. 

----

----

## Overview
----

Each state transition daemon is a python script that runs **all the time**. These scripts are essential because they configure newly installed Seattle nodes for use by the GENI. Each script ''transitions'' the node from some prior state to a new state. The transition might require sending commands to the node manager, creating new database records, etc. Here are the three state transition scripts that run on seattlegeni.cs:

 * **donation_to_canonical** -- transition a node from a newly installed state (donation state) into the canonical state
 * **canonical_to_onepercentmanyevents** -- transitions a node from the canonical state into the one percent manyevents state in which the node is ready to be used by GENI. If a node fails to get split, it is joined back up so there is only one VM remaining.
 * **onepercentmanyevents_to_onepercentmanyevents** -- transitions a node from the one percent manyevents state back into the one percent manyevents state, updating some time-dependent information about the node in the database



## Configuration
----

The state transition scripts on seattlegeni.cs are deployed in /home/geni/node_state_transitions/



## Deploying the daemons
----


To deploy the state transition scripts into /home/geni/node_state_transitions/ from the Seattle trunk that is assumed to have been checked out in ~/trunk/, do the following (**warning** : the destination directory will be overwritten) :

```
python ./trunk/seattlegeni/deploymentscripts/deploy_seattlegeni.py ./trunk /home/geni/node_state_transitions
```



## Starting/Stopping the daemons
----

The daemons are run from the command line without any arguments. You must run them from within their directory (e.g. /home/geni/node_state_transitions/). Here is the command for running each of the different type of transition scripts:

 * donation_to_canonical:

```
$ python transition_donation_to_canonical.py
```

 * canonical_to_onepercentmanyevents:

```
$ python transition_canonical_to_onepercentmanyevents.py
```

 * onepercentmanyevents_to_onepercentmanyevents:

```
$ python transition_onepercentmanyevents_to_onepercentmanyevents.py
```



## Making sure that the daemons are running
----

To test if these scripts are running, you can run the following command and check that each of the transition scripts listed above appears in the output:

```
$ ps auwx | grep python | grep -v grep
```

Also there is a monitoring script that is set up on seattlegeni.cs.washington.edu and a monitoring script on blackbox.cs.washington.edu which monitors the scripts regularly.