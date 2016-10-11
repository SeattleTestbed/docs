# NAT_advertisement.repy

Abstracts the task of looking up and advertising servers and forwarders. Allows for those using NAT_layer to advertise. Utilizes [wiki:Advertise.repy] to achieve this.

### Functions

```
nat_forwarder_advertise(ip, serverport, clientport)
```
   Registers the forwarder.

```
nat_server_advertise(key, forwarderIP, forwarderCltPort)
```
   Advertises the server.

```
nat_stop_server_advertise(key)
```
   Stops advertising the server key.

```
nat_forwarder_list_lookup():
```
   Returns a list of OK NAT forwarders.

```
nat_server_list_lookup(key)
```
   Returns a list of OK NAT servers.

```
nat_toggle_advertisement(enabled, threadRun=True)
```
   Toggles the state of the advertisement.
   Notes: 

   * threadRun controls the advertisement thread.
### Usage

???

### Includes
[wiki:Advertise.repy]