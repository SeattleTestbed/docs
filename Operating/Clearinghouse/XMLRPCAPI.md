# Seattle Clearinghouse API


An XML-RPC interface to Seattle Clearinghouse is available, for clients wishing to access Seattle Clearinghouse functionality without going through the Seattle Clearinghouse website. The XML-RPC server is located at the following address: ```https://seattleclearinghouse.poly.edu/xmlrpc/```

For examples on how to use XML-RPC with Seattle Clearinghouse, check out the [wiki:SeattleGeniClientLib Seattle Clearinghouse XML-RPC Client Library].



### Authentication
In order to talk with Seattle Clearinghouse over XML-RPC, authentication is required.

The authentication structure takes the form of the following dictionary:
   ''{'username':'YOUR_USERNAME', 'api_key':'YOUR_API_KEY'}''

The value of ''YOUR_USERNAME'' is the same username you use to login to the Seattle Clearinghouse website. The value of ''YOUR_API_KEY'' is the API key you can find on Seattle Clearinghouse when viewing the profile page for your account.



**This structure is expected as the first argument in every XML-RPC API call (except where otherwise noted).
**
All XML-RPC functions will return an XML-RPC Fault Code 101 if authentication fails.




### XML-RPC Faults
In the event of an exception/error, an XML-RPC Fault will be sent to the client.

The fault code and message contains information about the error that occurred.




### acquire_resources(auth, rspec)
----

Given a resource specification as a dict (rspec), this function acquires resources for the user. There are currently four types of rspecs defined:

''{'rspec_type':'lan', 'number_of_nodes':N}''
  
Acquire N VMs/vessels on nodes all with the same starting three octects of the IP address.


''{'rspec_type':'wan', 'number_of_nodes':N}''
 
Acquire N VMs on nodes all with different starting three octects of the IP address.


''{'rspec_type':'nat', 'number_of_nodes':N}''
 
Acquire N VMs on NAT nodes (nodes which are communicated with through a NAT forwarder).


''{'rspec_type':'random', 'number_of_nodes':N}''

Returns N VMs on any types of nodes, including a combination of different types of nodes.



Returns a list of dictionaries, where each dictionary contains information about an acquired VM. The dictionaries are of the form:
      **{'node_ip':node_ip, 'node_port':node_port, 'vessel_id':vessel_id, 'node_id':node_id, 'handle':handle, 'expires_in_seconds':seconds}**

      ''node_ip'' is a string containing the IP or other identifying information of the node manager.

      ''node_port'' is an integer representing the port used by the node manager.

      ''vessel_id'' is a string which represents the vessel_id for the vessel/VM (such as 'v21').

      ''node_id'' is the node id of the node (a public key string).

      ''handle'' has an undefined type but is used in future calls to release_resources. ''Make no assumptions about the type of this item.''

      ''expires_in_seconds'' is an integer representing the number of seconds until this VM's acquisition will expire.


Raises an XML-RPC Fault Code 1 or 100 if an internal error occurred in Seattle Clearinghouse.

Raises an XML-RPC Fault Code 101 if authentication failed.

Raises an XML-RPC Fault Code 102 if any arguments were invalid.

Raises an XML-RPC Fault Code 103 if the account doesn't have enough credits available to acquire the requested vessels.

Raises an XML-RPC Fault Code 105 if Seattle Clearinghouse could not fulfill the request (e.g. there are not enough vessels of the requested type available).




### acquire_specific_vessels(auth, vesselhandle_list)
----

Acquires specific VMs (VMs of specific names on specific nodes). This will be best effort. Zero or more of the vessels may be acquired.
Requesting VMs that exist but are not available will not result in an exception.

The **vesselhandle_list** is a list of VM handles.

Returns a list of dictionaries like that returned by **acquire_resources**.

Raises an XML-RPC Fault Code 1 or 100 if an internal error occurred in Seattle Clearinghouse.

Raises an XML-RPC Fault Code 101 if authentication failed.

Raises an XML-RPC Fault Code 102 if any arguments were invalid.

Raises an XML-RPC Fault Code 103 if the account doesn't have enough credits available to acquire the requested VMs.




### release_resources(auth, list_of_handles)
----

Release resources (VMs) previously acquired by the account.  The handles in **list_of_handles** indicate the VMs to be released.

Raises an XML-RPC Fault Code 1 or 100 if an internal error occurred in Seattle Clearinghouse.

Raises an XML-RPC Fault Code 101 if authentication failed.

Raises an XML-RPC Fault Code 102 if any arguments were invalid.




### renew_resources(auth, list_of_handles)
----

Renew resources (VMs) previously acquired by the account.  The handles in **list_of_handles** indicate the VMs to be renewed. VMs are renewed for 7 days.

Raises an XML-RPC Fault Code 1 or 100 if an internal error occurred in Seattle Clearinghouse.

Raises an XML-RPC Fault Code 101 if authentication failed.

Raises an XML-RPC Fault Code 102 if any arguments were invalid.

Raises an XML-RPC Fault Code 103 if the account doesn't have enough credits available to renew any of its acquired VMs. This can happen, for example, if the account acquired VMs based on donations that have since gone offline resulting in the account being over its VM credit limit.




### get_resource_info(auth)
----

Returns a list of resources (VMs) currently acquired by the user.

The return list is of the same form as returned by acquire_resources.

Raises an XML-RPC Fault Code 1 or 100 if an internal error occurred in Seattle Clearinghouse.

Raises an XML-RPC Fault Code 101 if authentication failed.

Raises an XML-RPC Fault Code 102 if any arguments were invalid.




### get_account_info(auth)
----

Returns a dictionary of account information for the account. This includes the user's port number, name, total number VMs that can be acquired, and the user's affiliation.

Returns a dictionary of the form:
      **{'user_port':user_port, 'user_name':user_name, 'urlinstaller':urlinstaller, 'private_key_exists':private_key_exists, 'max_vessel':max_vessel, 'user_affiliation':user_affiliation}**

      ''user_port'' is an integer, indicating a port number that by default will be available for TCP / UDP on all of the user's VMs.

      ''user_name'' is a string containing the username.

      ''max_vessel'' is an integer, indicating the total VMs allowed.   This may vary as donations are credited to the user or go offline.   

      ''user_affiliation'' is a string and represents the affiliation provided by the user when registering for an account.   This field is not validated so should not be trusted.


Raises an XML-RPC Fault Code 1 or 100 if an internal error occurred in Seattle Clearinghouse.

Raises an XML-RPC Fault Code 101 if authentication failed.

Raises an XML-RPC Fault Code 102 if any arguments were invalid.




### get_public_key(auth)
----

Returns the user's public key as a string.

Raises an XML-RPC Fault Code 1 or 100 if an internal error occurred in Seattle Clearinghouse.

Raises an XML-RPC Fault Code 101 if authentication failed.

Raises an XML-RPC Fault Code 102 if any arguments were invalid.


----
# Calls that do not require authentication



### get_encrypted_api_key(username)
----

Returns the user's api key encrypted with the user's public key.

Raises an XML-RPC Fault Code 1 or 100 if an internal error occurred in Seattle Clearinghouse.

Raises an XML-RPC Fault Code 102 if any arguments were invalid.


----
# Calls requiring the account password

The calls below take a pwauth structure
instead of the auth structure used in the rest of the api. The difference is that the pwauth
structure contains a password instead of an api key. Thus, the structure is:
   **{'username':'YOUR_USERNAME', 'password':'YOUR_PASSWORD'}**




### regenerate_api_key(pwauth)
----

Generates a new api key for the user and returns the new api key.

Raises an XML-RPC Fault Code 1 or 100 if an internal error occurred in Seattle Clearinghouse.

Raises an XML-RPC Fault Code 102 if any arguments were invalid.




### set_public_key(pwauth, pubkeystring)
----

Sets the user's public key.

Raises an XML-RPC Fault Code 1 or 100 if an internal error occurred in Seattle Clearinghouse.

Raises an XML-RPC Fault Code 102 if any arguments were invalid.
