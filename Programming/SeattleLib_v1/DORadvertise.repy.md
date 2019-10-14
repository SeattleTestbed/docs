# DORadvertise.repy
Another method of advertising nodes in the Seattle library. This module advertises to the Digital Object Registry run by CNRI.
### Functions
```
DORadvertise_announce(key, value, ttlval, timeout=None)
```
   Adds a (key, value) pair into the DOR.
   Notes:

   * ttlval describes the length of time in seconds the tuple exists in the DOR.
   * Exceptions are raised if there are errors within the XML-RPC client.
   * timeout is the number of seconds spent before the process quits.

```
DORadvertise_lookup(key, maxvals=100, timeout=None)
```
   Looks up a stored value under the key in the DOR.
   Notes:

   * maxvals is the maximum number of values returned.
   * timeout is the number of seconds spent before the process quits.

### Usage

???couldn't find any?

### Include
[SeattleLib/sockettimeout.repy](sockettimeout.repy.md)

[SeattleLib/httpretrieve.repy](httpretrieve.repy.md)

[SeattleLib/xmlparse.repy](xmlparse.repy.md)

[Back to NodeAdvertising](NodeAdvertising.md)
