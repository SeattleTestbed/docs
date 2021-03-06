# domainnameinfo.repy

This module provides one function - the country which the given hostname is from. The hostname is a string which describes a Seattle user. See below for more details.


### Functions

```
def domainnameinfo_gethostlocation(hostname):
```
   Given a hostname, returns a string that contains the country the hostname is from.
  
   Notes: 

   * hostname is a hostname string that we want information about. For example: 'planetlab-2.di.fc.ul.pt'
   * Raises UnknownHostLocationError: if we don't know the location of the hostname. Only countries with standard abbreviations are recongnized by this module.
   * Raises TypeError if hostname isn't a string.
   * Returns a string which has the country.


### Usage

```
assert(domainnameinfo_gethostlocation('amazon.uk') == 'United Kingdom')
assert(domainnameinfo_gethostlocation('microsoft.us') == 'United States')
```

