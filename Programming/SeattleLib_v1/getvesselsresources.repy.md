# getvesselsresources.repy

This module computes the Given a vessel name the functions finds the correct vessel and print out all the resources available.

A client may find this module useful when it is unclear how many resources a vessel is using or if its unclear how much resources one should allocate to a particularly vessel.


### Functions


```
def getvesselresources_portnum(portnum, ipaddr=getmyip(), portval=1224):
```
   Finds all the vessels that have the port number requested and then return a dictionary with all the vessels and their resources that are available.

   Notes:

   * portnum(int) is the port number that the user is looking for
   * ipaddr is the ip address for which to get the vessels for. By default it is local ip address.
   * portval-the port number for which to find vessels. By defaults it is 1224.
   * Throws a ValueError exception if the resource file is not formatted well.
   * Returns a dictionary where the keys are the vessel name and the values are a list of resources. Resources can be accessed by returnresult[vessel_name][resource_name]
   * If the port value or ip address provided is not associated with the resource port number, then an empty dictionary is returned.


```
def getvesselresources_vesselname(vesselname, ipaddr=getmyip(), portval=1224):
```
   Given a vessel name (and maybe ip address and the port value), find all the resources available for that vessel and return a dictionary of the resources for that vessel.
	
   Notes: 

   * vesselname(string) is the vessel that the user wants the resource for
   * ipaddr is the ip address for which to get the vessels for. By default it is local ip address.
   * portval is the port number for which to find vessels. By defaults it is 1224.
   * Throws ValueError exception on an invalide vessel name input.
   * Throws a ValueError exception if the resource file is not formatted well.
   * Returns a dictionary where the keys are the vessel name and the values are a list of resources. Resources can be accessed by returnresult[vessel_name][resource_name]
   * If the port value or ip address provided is not associated with the resource port number, then an empty dictionary is returned.


### Includes


[wiki:SeattleLib/nmclient.repy],
[wiki:SeattleLib/rsa.repy]