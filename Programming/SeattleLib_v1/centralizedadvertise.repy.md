# centralizedadvertise.repy

This module provides a hash table service for nodes. Adds and removes entries to a centralized hash table. This service runs on seattle.cs, which is also known as satya.cs. See CentralizedAdvertiseService for more details.

### Functions



```
centralizedadvertise_announce(key, value, ttlval)
```
   Announce a key / value pair into the CHT.

   Notes:
   * ttlval must be a positive integer that describes the amount of time until the value expires.
   * Network / Timeout exception are raised if there are connection errors.

```
centralizedadvertise_lookup(key, maxvals=100)
```
   Returns the valid values stored by the key in a list.

   Notes:
   * maxvals must be a positive integer that describes how many values to return.
   * Network / Timeout exception are raised if there are connection errors.

### Example Usage

```
#advertize that the current client has started
my_advetisement_info = getmyip() + ":"+ str(mycontext['myport']) + ":" + str(keyinfo)
centralizedadvertise_announce(mycontext['experiment_name'], my_advetisement_info, ADVERTISE_PERSIST)
```

### Includes
[sockettimeout.repy](sockettimeout.repy.md)

[serialize.repy](serialize.repy.md)



