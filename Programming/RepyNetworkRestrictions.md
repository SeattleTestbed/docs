# Repy Network Restrictions (IP's and Interfaces)

----

----



## Default Behavior
----
Repy's behavior can be broken down into the semantics of getmyip, and the other network calls (recvmess/sendmess/openconn/waitforconn). By default getmyip will attempt to connect to an external address, and report the local IP that was binded to the socket. This generally means that getmyip will return the OS default IP. The other repy network calls will allow any localip to be specified, but they may fail to bind if the IP does not exist.



## The nootherips flag
----
Repy's default behavior with respect to allowing any local ip can be controlled with the use of the "--nootherips" flag. This flag disables repy's acceptance of 'implicit' IP's, and enforces a strict white list policy for the localip specified to networking calls. If the IP passed to the calls is not allowed through the IP flag, or does not belong to a interface which is allowed, then an exception will be raised to inform the developer. If no local IP is specified, the network calls will fall back onto getmyip to get a localip to bind to. It should be noted that the --nootherips flag always allows the loopback address 127.0.0.1. This IP cannot be denied.



## The IP flag
----
Repy supports specifying preferred / allowed IP's through the use of this flag. IP's will be considered 'preferred' in the order they are specified. If an IP or interface is specified, its associated IP will be returned by getmyip, overriding the default behavior.



## The Iface flag
----
Repy supports specifying preferred / allowed interfaces through the use of this flag. Interfaces will be considered 'preferred' in the order they are specified. If an IP or interface is specified, its associated IP will be returned by getmyip, overriding the default behavior. Interfaces that experience frequent IP changes may be problematic, since the allowed IP cache is updated only on calls to getmyip(). This is a known bug, but is usually a non-issue since DHCP tends to renew existing IP's rather than assign new ones.



## Unit Tests
----
See [UnitTests this page] for more information. Essentially there are unit tests but they are not part of the standard ones run by run_test.py. They must be run separately through the use of the "-network" flag.



