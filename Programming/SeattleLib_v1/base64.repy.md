# base64.repy

Provides a service for encoding data as specified in RFC 3548 (a subset of the python base64 service). See http://docs.python.org/library/base64.html and http://en.wikipedia.org/wiki/Base64 for more information.

### Functions

```
base64_b64encode(s, altchars=None)
```
   Returns an encoded string s using Base64.

   Note: 

   * altchars can be used to describe additional characters into the alphabet.
   * Default altchars uses the standard Base64 alphabet.
   * altchars must be at least 2 characters if not None.

```
base64_b64decode(s, altchars=None)
```
   Returns after decoding a previously encrypted string s.

   Note: 

   * TypeError exception is raised if an error occurs during encoding.
   * Ignored characters not in the standard Base64 alphabet.
   * See the encoding function for altchars parameters.

```
base64_standard_b64encode(s)
```
   Like the above encoding function, but this only uses the standard Base64 alphabet.

```
base64_standard_b64decode(s)
```
   Like the above decoding function, but this only uses the standard Base64 alphabet.

   Note:
   * TypeError exception is raised if an decoding error occurs.

```
base64_urlsafe_b64decode(s)
```
   Decode a Base64 encoded string using a URL-safe alphabet, substituting - instead of + and _ instead of / in the standard Base64 alphabet.

   Note:
   * TypeError exception is raised if an decoding error occurs.
