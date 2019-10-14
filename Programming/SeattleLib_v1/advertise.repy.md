# advertise.repy

This module allows for different node to be announced via different services (central advertise service, OpenDHT, or both).

### Functions
```
advertise_announce(key, value, ttlval, concurrentevents=2, graceperiod=10, timeout=60)
```
   Adds a value to the OpenDHT, central advertise service, or both.

   Notes:
   * ttlval must be a positive integer that describes the amount of time until the value expires.
   * concurrentevents is how many services to announce in parallel.
   * graceperiod and timeout are both optional parameters.

### Example Usage

```
advertise_lookup(key, maxvals=100, lookuptype=None, concurrentevents=2, graceperiod=10, timeout=60)
```
   Lookup an value stored at the given key in OpenDHT, central advertise service, or both.

   Notes:
   * lookuptype defaults to look in all types.
   * lookuptype, concurrentevents, graceperiod, and timeout are all optional.

### Usage

```
#retrieve node list from advertise_lookup
node_list = advertise_lookup(node_state_pubkey, maxvals = 10*1024*1024, lookuptype=[server_lookup_type])
```

```
#within node manager
advertise_announce(advertisekey, str(my_name), adTTL)
```

### Includes
[SeattleLib/listops.repy](listops.repy.md)

[SeattleLib/openDHTadvertise.repy](openDHTadvertise.repy.md)

[SeattleLibcentralizedadvertise.repy](centralizedadvertise.repy.md)

[SeattleLib/DORadvertise.repy](DORadvertise.repy.md)

[SeattleLib/parallelize.repy](parallelize.repy.md)

[Back to NodeAdvertising](NodeAdvertising.md)
