# sha.repy

This module contains an simple implementation of the SHA-1 algorithm. SHA stands for Secure Hash Algorithm and returns secure 160 bit message digests. See http://en.wikipedia.org/wiki/SHA-1 for more details about this encryption method. This module is primarily based off the Python equivalent. See http://docs.python.org/library/sha.html for more details about the standard version. Seattle's SHA-1 implementation is capable of encrypting and decrypting strings.

Please note that Seattle also has [wiki:SeattleLib/md5py.repy], which is arguably better than this. All the public functions have counterparts in [wiki:SeattleLib/md5py.repy].

### Functions

```
def sha_new(arg=None):
```
   Return a new sha crypto object.


```
def sha_hash(string):
```
   Gives the hash of a string


```
def sha_hexhash(string):
```
   Gives the hash of a string but returns the hash in hex form. This string has a fixed length of 32, contains only hexadecimal digits. This may be used to exchange the value safely in email or other non-binary environments.


