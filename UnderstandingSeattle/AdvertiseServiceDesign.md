# Advertise Service Design Document

This document details the design and implementation of the Advertise Service.  The purpose of the advertise service is to provide the Seattle infrastructure and its users with an easy key-value data store.  Clients can then contact the server to perform lookups on a key, to which the server with respond with the **list of values** that have been advertised to a key.  Each key-value pair is kept until it expires.  This document describes the advertise server design, the advertise interface for interaction with the advertise server, and how to setup additional advertise servers.







## Advertise Server
----

The Advertise server is a key-value data store that anyone can access.  A single advertise server can maintain key-value pairs from a multitude of clients.  A user can advertise a ```(key, value)``` pair with a user defined timeout.  The same key can be used to advertise different values.  Other users can then request a lookup on the same key, and **all values that the key is mapped to will be returned**.  A key will only remain in memory so long as its timeout has not expired.  If a ```(key, value)``` pair already exists, then the later of the two expiration times will be kept.

An example use case for the advertise server is to determine which nodes contain VMs that a user has access to.  For each user that has access to a VM(also known as vessel), the controlling node manager will map the user's public key to the node's IP address, allowing the Clearinghouse and Seash to identify which nodes the user can manipulate.

There can be (and are) multiple advertise servers running.  The advertise repy library (which can be found in seattlelib) provides an API that will contact each server in parallel.  If you are interested in using the advertise service in your client program, it is recommended that you use advertise.repy, as opposed to using the service-specific implementation.  This allows us to set up additional servers transparently without impacting your client program.




## Advertise Interface
----

The advertise server provides an interface to set and retrieve key-value pairs.   Each entry in the advertise server has the following attributes:

    key
        This is an identifier for a particular set of values.  Its type can be any basic python type that is serializable by the repy serialize library.

    value
        A value that is mapped to by the specified key.  Its type can also be any basic python type that is serializable by the repy serialize library.  This value will be part of the list of values that is returned when a user performs a lookup based on a key.

    ttl
      This is a number that controls how long a single ```(key, value)``` pair lives in the advertise server.  This causes the advertise server to designate an expiration time for the ```(key, value)``` pair.  If the same ```(key, value)``` pair is re-advertised, then the expiration time is either extended, or left alone.  It is not possible to make a  ```(key, value)``` pair expire earlier.


The interface is:

    advertise_announce(key, value, ttlval, concurrentevents, graceperiod, timeout)   -- public
        Advertises a ```(key, value)``` pair with a TTL value.

          key (string)
            The key for our advertise dictionary entry.

          value (string)
            The value for our advertise dictionary entry.

          ttlval (int)
            Time in seconds to persist the associated key<->value pair.

          concurrentevents (int) (optional)
            How many services to announce on in parallel.

          graceperiod (float) (optional)
            Amount of time to wait before returning, provided at least one of the
            parallel attempts has finished.

            Note that even when this method returns, parallelized announce attempts may
            still be running. These will terminate in relatively short order, but be
            aware of this. It could be a problem, for example, if you tried to set graceperiod
            very low to send rapid-fire queries to the advertise servers. This would
            probably cause you to exceed your allotted outsockets. (This is only
            possible if your timeout value is greater than your graceperiod value.)

            In short, graceperiod is a "soft" timeout. Provided at least one query has
            been confirmed, the method will return after graceperiod seconds at most.
            If none return, this could run all the way till timeout.

          timeout (int) (optional)
            Absolute allowed time before returning. Provided the method has not
            returned by now, successful or not, it will terminate after timeout seconds.


    advertise_lookup(vesselname)   -- public
        Returns the values that a particular key is mapped to.  This will be a list of all the values that match the key.

          key
            The key used to lookup values.

          maxvals (optional, defaults to 100):
            Maximum number of values to return.

          lookuptype (optional, defaults to the currently supported list of advertise servers.  Refer to the _advertise_all_services constant in advertise.repy for more information):
            Which services to employ looking up values.

          concurrentevents (optional, defaults to 2):
            How many services to lookup on in parallel.

          graceperiod (optional, defaults to 10):
            After this many seconds (can be a float or int type), return the
            results if one service was reached successfully.

          timeout (optional, defaults to 60):
            After this many seconds (can be a float or int type), give up.



## Setting Up New Advertise Servers
----

1. Add an Advertise API.
You need to introduce a new advertise library to provide clients with an API to interact with the new advertise server.  If your advertise server matches the centralized advertise format, then you only need to write wrappers around the centralizedadvertise_base.repy announce and lookup calls.  Remember to provide global variables so that users can change the server IP/port if they need to.  An example of this can be found in centralizedadvertise.repy.

Additionally, if you wish to turn this service to be one of the default advertise services, then you'll have to modify the default advertise server list in advertise.repy.

2. Setup the Advertise Server.
Next, go onto the machine that the server will be deployed on.  Create a new user account for the server, and then deploy the advertise server into that account's home directory.  Do NOT set up a production service in your own home directory.  This will make it difficult for other project members to step in and maintain the service.

In a screen instance, run the advertise server with output redirected:
```
  python advertiseserver.py >> advertiseserver.stdout 2>> advertiseserver.stderr
```


You should now talk to any system administrators to get the relevant ports open, if necessary.



## Deployed Advertise Instances
----
 * Centralized Advertise V1 (TCP, Repy): advertiseserver.poly.edu:10102
 * Centralized Advertise V2 (TCP, Python): advertiseserver_v2.poly.edu:10102
 * Centralized Advertise V3 (TCP, Python): advertiseserver_v3.poly.edu:10102
 * UDP Advertise (UDP, Repy): udpadvertiseserver.poly.edu:10102