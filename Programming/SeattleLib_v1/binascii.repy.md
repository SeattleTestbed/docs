# binascii.repy

This module contains method of converting from binary to ASCII representations and vice versa.

### Functions

```
binascii_a2b_hex(hexstr)
```
   Returns the binary representation of hexstr.
   Note:

   * TypeError exception is thrown if hexstr has odd length

```
def binascii_b2a_hex(binary_data)
```
   Returns the ASCII repsentation of binary_data.

### Usage

```
name = shurui;
binary_value = binasciia2b_hex(name)
```

