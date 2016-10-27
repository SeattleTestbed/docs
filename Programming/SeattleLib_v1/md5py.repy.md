# md5py.repy

Encrypts a string of arbitrary length into a 128-bit "fingerprint", creating what is essentially a digital signature. Based on the python version. See http://docs.python.org/library/md5.html and http://en.wikipedia.org/wiki/MD5 for more details.

### Functions
```
update(self, inBuf)
```
   Updates the md5 object with the string inbuf. Repeated calls result in the concatenation of the arguments.


   Notes:
   * self describes the md5 object.

```
digest(self)
```
    Return the digest of the strings passed to the update(self, inBuf) so far. This is a 16-byte string which may contain non-ASCII characters, including null bytes.

```
hexdigest(self)
```
   Similar to digest(self) expect this returns the hexadecimal form of the digest.

```
copy(self)
```
   Return a copy ('clone') of the md5 object. This can be used to efficiently compute the digests of strings that share a common initial substring.

```
md5py_new(arg=None)
```
   Returns a new md5py object.

```
md5py_md5(arg=None)
```
   Same as md5py_new(arg) - necessary for backward compatibility reasons.

### Usage

```
testdigest = binascii_b2a_hex(md5py_new("").digest())
assert(testdigest == 'd41d8cd98f00b204e9800998ecf8427e') 
 
testdigest = binascii_b2a_hex(md5py_new("a").digest())
assert(testdigest == '0cc175b9c0f1b6a831c399e269772661')
```