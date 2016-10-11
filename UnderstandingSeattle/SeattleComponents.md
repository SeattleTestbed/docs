# How Seattle Works

This guide describes how Seattle works from the perspective of the people who participate in the testbed to install Seattle and use and manage Seattle resources.



## Human Perspective

New resources are added to the Seattle testbed in a three-step process. First a person we call a **planner** [wiki:CustomInstallerBuilder creates a customized installer] which defines how the planner would like to allocate their resources when Seattle is installed on a computer. Then, someone we call a **donor** runs the customized installer on their local system and a small percentage of the resources on their computer are added to the testbed according to the allocations set out by the planner. **Researchers** who are granted resources on the newly added computer will then be able to run experiments or share those resource with other researchers.

[[Image(SeattlePicture1.jpg)]]

# Seattle Components

Seattle is composed of three components: VMs, the node manager, and the experiment manager.

## VM/Vessel
A VM is a programming language virtual machine that runs a user's code (currently the only language supported is RestrictedPython).   VMs prevent the program running in them from performing unsafe actions (like opening the user's credit card information).   VMs also have a specified number of resources they are allowed to consume.   The vessel restricts the program from consuming more than the allowed number of resources.   

## Node Manager
The purpose of the node manager is to manage the VMs on a single machine.   The node manager restricts access to the VMs to only authorized parties.   For example, every VM has an owner and a set of users.   The owner can change the set of users, change ownership to another party, split the VM into multiple VMs, etc. (see the Node Manager API documentation for more information).   Users are allowed to upload files to the VM, start and stop programs, read the VM's log, and other simple operations.   The node manager also ensures that the total amount of consumed resources does not vary as VMs are split and joined.   
 
## Experiment Manager
Researchers who want to run programs on the VMs they control are likely to use an experiment manager (like seash).   An experiment manager locates VMs that the user controls, and interacts with the node manager to control those VMs.   For example, an experiment manager may take a user's command to deploy foo.py everywhere and go to contact all of the VMs the user owns on each of the node manager (saving the user the headache of contacting nodes manually).

[[Image(componentdiagram.gif)]]

In the above example, there are three computers on the top, each of which is running a node manager.   Each node manager is controlling the VMs on its local machine.   At the bottom there are two experiment managers (for different users) that are contacting some collection of the Vms they control to perform actions on behalf of the users.