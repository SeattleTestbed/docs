# Ideas for Seattle Contributors

This is a list of potential projects for Seattle contributors to work on, originally intended for a past Google Summer of Code.



## Transparent handling of IP address changes
Mobile Internet devices have increased rapidly in popularity to the point where they are almost ubiquitous.   Mobile Internet devices present a new problem for network programmers because their IP addresses change frequently and unexpectedly as the devices move from access point to access point.   We'd like to provide a transparent network library written in the restricted version of Python supported by Seattle.   

One general approach that may solve the problem of locating a mobile device is for each mobile device to register its current IP address in a Distributed Hash Table (a global storage abstraction that has a get / put interface).    The mobile device would put its current IP address into the DHT under its node ID (a unique key that is "the node's identity").   To communicate with a mobile device, a node can get the IP address stored in the DHT under the node's key.   

However, it is also important to make this procedure transparent to the programmer whose application uses the abstraction.   To do this, the transparent network library will reconnect TCP connections and redirect UDP traffic as the mobile device's IP address changes.   The behavior of this must be identical to Seattle's network communication including failure cases and API.

As with all work on the Seattle project, this work will be done in cooperation with other developers on a "Strike Force".   

Networking and Python experience are a plus, but not required.


## IPv6
Seattle currently doesn't support IPv6.   We'd like to be able to support IPv6 in Seattle's version of restricted version Python, the node manager, the software updater, the backend to the Seattle Clearinghouse website, and any other necessary components.   

As with all work on the Seattle project, this work will be done in cooperation with other developers on a "Strike Force".   

Previous IPv6 experience is recommended.   Networking experience or Python experience also a plus, but not required


## Increasing Seattle's portability to mobile devices
Seattle currently runs (to varying degrees) on many different mobile devices such as the Nokia N800, jail broken iPhone, and Windows Mobile.   We'd like to increase our support for these platforms by ensuring the portability and security on these platforms.   We would also like to port the Seattle VM to new mobile platforms, in particular Android.


Mobile development experience is a big plus, but other experience with low level OS concepts (do you know what a system call is?) is an acceptable substitute.   Python experience is helpful but not required.


## Shell improvements (cmd, etc.)
The Seattle shell (Seash) is useful, but lacks many of the features and improvements of other shells.   We'd like tab complete, the ability to safely interrupt commands without exiting, and support for saving the current shell state.

Python experience (in particular with the cmd module) is preferred but not required.


## Graphical shell front end (GUSH)
We'd like to use the GUSH project's graphical front end with the Seattle shell (Seash).   While some features may not translate directly (for example the discovery of approximate latitude and longitude may be impractical for arbitrary Internet computers), we'd like to get as much as possible working.   Ideally we'd also make these changes in conjunction with the GUSH project so that as they evolve GUSH, our support remains.   

Note: the faculty lead of GUSH (Jeannie Albrecht) is aware and supportive of our efforts.

GUSH Project Page:
http://gush.cs.williams.edu/trac/gush

C++ experience required, Perl, Python and XML experience preferred by not required.


## "user level" GFS-like FS for better MapReduce support
Seattle has a MapReduce library to support parallel processing of data.   However, the data must be copied to the individual nodes.   We'd like to build a GFS-like distributed FS for better support of MapReduce and explore its use in other applications.   The implementation must be in the restricted version of Python used by the Seattle project.   

As with all work on the Seattle project, this work will be done in cooperation with other developers on a "Strike Force".   

Networking and Python experience a plus, but not required.


## Dynamic resource reallocation
The Seattle VM provides resource control over the program that execute on it.   This prevents a malicious or erroneous program from using excessive resources.   Right now the resources that may be consumed by a VM are set at VM instantiation and cannot be changed.   We'd like to allow VMs to have their resources altered at any point during VM execution.   This would allow better overall resource control and usability of Seattle.

In addition to control, it's also important for a user to have feedback on how resources are being used.   We'd like to provide a feedback mechanism to the user program, especially in the cases where a resource is constrained.   This would allow a user to understand how resources are utilized by their program.

Python experience a plus, but not required.