## Adding Support for NAT Nodes:

The Controlled Node Communication feature (CNC) is not currently compatible with NAT nodes. Currently, if a machine registers to receive Seattle traffic, a Seattle node sharing one or more user keys can send traffic to that machine on any port. The question we are trying to address is: Do we want to treat NAT nodes as exceptions and implement a special type of registration where the intermediate node can register to receive traffic on specific ports? Or do we want to change the current registration model to require all machines that wish to receive Seattle traffic to register each port they wish to receive Seattle traffic on?

Case 1: We change the current registration model to require all machines that wish to receive Seattle traffic to register each port they wish to receive Seattle traffic on.
This option is more secure but will have severe performance consequences. Each Seattle node will likely want to receive Seattle traffic on multiple ports and will have to periodically register each port separately. Nodes will also need to store a lot more address information in their caches.
The following attack will still be possible however.
The hostile party registers a machine behind a NAT through the forwarder. The forwarder needs the machine behind the NAT to send it UDP messages to keep the port mapping active in the NAT. If the client stops sending over a long period, the mapping will be removed, then the port gets reassigned to another computer by the NAT.  The forwarder would then forward UDP messages to the wrong client.
The risk of this occurring can be minimized by requiring more frequent registration renewal and having data stored in the node caches expire after a shorter period of time.

Case 2: We treat NAT nodes as exceptions and implement a special type of registration where the intermediate node can register to receive traffic on specific ports.
The advantage of this approach is that the performance will be minimally impacted. The machines behind a NAT will not register directly, but rather the forwarder will register a single port for each. Each registration maintained by the server will correspond to a different machine.

However, this is opens the system to the following attack:
Consider several machines behind a NAT. One is malicious and registers directly with the server as a regular node (instead of registering through the intermediate node as a NAT node). The NAT IP address can now be contacted by any node that shares registration user keys, so a DOS attack can occur where a large number of repy nodes flood the IP address of the NAT at randomly chosen ports with traffic. Some traffic may get though to machines that are not opted in. 

The attack discussed in case 1 can also be conducted in case 2.

Conclusion and Questions:
I would appreciate any feedback on this. Which case is the best option or is there another solution we should consider? In my opinion 2 is preferable because of the significant performance difference.
Are there any other security vulnerabilities we should be aware of? Are either of the attacks discussed of serious concern, or should we not worry about them?
