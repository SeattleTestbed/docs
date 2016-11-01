# Understanding Seattle Testbed

The goal of Seattle is to create a platform for networking and distributed 
systems research. This README (and the other pages you see) attempts to 
explain the different parts of Seattle and how they come together to meet 
this goal.

# Repy

Repy is a Python-based sandbox which restricts API calls and limits the 
consumption of resources such as CPU, memory, storage space, and network 
bandwidth. Seattle Testbed experiments are confined to Repy sandboxes.

## The Repy API
Repy has a limited API for accessing system resources. This is in order 
to prevent a malicious user using a bug in the Python libraries to escape 
from the sandbox. The full API is documented 
[here](../Programming/RepyV2API.md).

## Safety Analysis
Repy disallows code that could allow the program direct access to system 
resources. Instead, it only allows calls that are in the Repy API. Because 
Repy is largely a subset of Python, it can leverage the Python interpreter 
to examine the program's abstract syntax tree. If forbidden code is inside 
of the script, Repy refuses to run it.

## Limiting resource consumption
One of the main goals of Repy is to control the usage of certain 
system resources.

Resources can be grouped in a few categories:

Certain resources have an active limit of the maximum amount that can be had 
at a given instant. For example, an instance of Repy is only allowed to use 
a certain amount of disk space. But independent of that, Repy is also not 
allowed to use a large amount of disk i/o within a certain time period, as 
this could also degrade performance for the host. These resources are 
monitored in two ways:

When an activity that requires a resource is attempted Repy checks how much 
of that resource was used, and it will either grant the request, or wait 
until more of that resource is available.

Other resources -- like the CPU and memory usage -- are not able to be 
directly controlled within python. Instead, Repy creates a new process or 
thread (OS dependent) which calls OS-specific functions to determine the 
amount of the CPU and memory used. If the resource renews over time, like 
CPU usage, Repy pauses the process for a short duration. If it does not renew 
itself, like memory usage, Repy will kill the process.

For more detailed information, see [code safety](CodeSafety.md).


# Node Manager

The node manager manages the different sandboxed programs (called vessels 
or VMs) that are running on a computer. The node manager stores information 
about the VMs it controls and allows VMs to be started, stopped, combined, 
split, and changed.

Programmers can then connect to the node manager, send a file, and then run 
that code on the remote VM. The easiest way to do this is with the 
Experiment Manager `seash` (see [code](SeattleTestbed/seash), 
[documentation](SeattleShell.md)).


For more detailed information, see [the nodemanager design doc](NodeManagerDesign.md) 
and the description of [Seattle Components](UnderstandingSeattle/SeattleComponents.md).
