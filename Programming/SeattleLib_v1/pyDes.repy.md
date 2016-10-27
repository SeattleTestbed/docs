# pyDes.repy

This module is a direct port of Todd Whitman's Python DES encryption algorithm. See http://en.wikipedia.org/wiki/Data_Encryption_Standard for more details on the algorithm. This particular page will basically use Todd's documentation. See http://twhiteman.netfirms.com/des.html for his documentation.

```
# This is a pure python implementation of the DES encryption algorithm.
# It's pure python to avoid portability issues, since most DES 
# implementations are programmed in C (for performance reasons).
#
# Triple DES class is also implemented, utilising the DES base. Triple DES
# is either DES-EDE3 with a 24 byte key, or DES-EDE2 with a 16 byte key.
#
# See the README.txt that should come with this python module for the
# implementation methods used.
#
# Thanks to:
#  * David Broadwell for ideas, comments and suggestions.
#  * Mario Wolff for pointing out and debugging some triple des CBC errors.
#  * Santiago Palladino for providing the PKCS5 padding technique.
#  * Shaya for correcting the PAD_PKCS5 triple des CBC errors.
#
"""A pure python implementation of the DES and TRIPLE DES encryption algorithms.

Class initialization
--------------------
pyDes.des(key, [mode], [IV], [pad], [padmode])
pyDes.triple_des(key, [mode], [IV], [pad], [padmode])

key     -> Bytes containing the encryption key. 8 bytes for DES, 16 or 24 bytes
     for Triple DES
mode    -> Optional argument for encryption type, can be either
     pyDes.ECB (Electronic Code Book) or pyDes.CBC (Cypher Block Chaining)
IV      -> Optional Initial Value bytes, must be supplied if using CBC mode.
     Length must be 8 bytes.
pad     -> Optional argument, set the pad character (PAD_NORMAL) to use during
     all encrypt/decrpt operations done with this instance.
padmode -> Optional argument, set the padding mode (PAD_NORMAL or PAD_PKCS5)
     to use during all encrypt/decrpt operations done with this instance.

I recommend to use PAD_PKCS5 padding, as then you never need to worry about any
padding issues, as the padding can be removed unambiguously upon decrypting
data that was encrypted using PAD_PKCS5 padmode.

Common methods
--------------
encrypt(data, [pad], [padmode])
decrypt(data, [pad], [padmode])

data    -> Bytes to be encrypted/decrypted
pad     -> Optional argument. Only when using padmode of PAD_NORMAL. For
     encryption, adds this characters to the end of the data block when
     data is not a multiple of 8 bytes. For decryption, will remove the
     trailing characters that match this pad character from the last 8
     bytes of the unencrypted data block.
padmode -> Optional argument, set the padding mode, must be one of PAD_NORMAL
     or PAD_PKCS5). Defaults to PAD_NORMAL.
    

Example
-------
from pyDes import *

data = "Please encrypt my data"
k = des("DESCRYPT", CBC, "
0
0
0
0
0
0
0
0", pad=None, padmode=PAD_PKCS5)
# For Python3, you'll need to use bytes, i.e.:
#   data = b"Please encrypt my data"
#   k = des(b"DESCRYPT", CBC, b"
0
0
0
0
0
0
0
0", pad=None, padmode=PAD_PKCS5)
d = k.encrypt(data)
print "Encrypted: %r" % d
print "Decrypted: %r" % k.decrypt(d)
assert k.decrypt(d, padmode=PAD_PKCS5) == data


See the module source (pyDes.py) for more examples of use.
You can also run the pyDes.py file without and arguments to see a simple test.

Note: This code was not written for high-end systems needing a fast
      implementation, but rather a handy portable solution with small usage.
```