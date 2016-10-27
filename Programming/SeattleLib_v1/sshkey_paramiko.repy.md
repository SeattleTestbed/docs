# sshkey_paramiko.repy

This module is to be used by [wiki:SeattleLib/sshkey.repy]. This is not a stand alone module. [wiki:SeattleLib/sshkey.repy] is the wrapper module that developers should use.

Note that much of this module is based off code that has been modified or taken from paramiko. It is licensed under a different license then the rest of the code and to avoid any conflict it has been separated into its own module. All the functions available in this module will be documented here for consistency, but usage details will be left out since all users should be utilizing [wiki:SeattleLib/sshkey.repy] instead.



### Functions

```
Exceptions

class sshkey_paramiko_BERException (Exception):
   This exception indicates that the BER decoding was not recognized

class sshkey_paramiko_SSHException(Exception):
   This exception indicates that the ssh key was unable to be decoded

class sshkey_paramiko_EncryptionException(Exception):
   This exception indicates that the ssh key was unable to be decrypted
```

 
```
class _sshkey_paramiko_BER(object):
    This class performs BER decoding.
```


```
def _sshkey_paramiko_get_bytes(packet, n):
```

```
def _sshkey_paramiko_inflate_long(s, always_positive=False):
```

```
def _sshkey_paramiko_get_string(packet):
```

```
def _sshkey_paramiko_generate_key_bytes(salt, key, nbytes):
```

```
def _sshkey_paramiko_read_public_key(openfile):
```

```
def _sshkey_paramiko_read_private_key(tag, openfile, password=None):
```

```
def _sshkey_paramiko_decode_private_key(tag, file, password=None):
```

### Includes

[wiki:SeattleLib/sshkey.repy]

[wiki:SeattleLibbase64.repy]

[wiki:SeattleLib/md5py.repy]

[wiki:SeattleLib/pyDes.repy]

[wiki:SeattleLibbinascii.repy]
