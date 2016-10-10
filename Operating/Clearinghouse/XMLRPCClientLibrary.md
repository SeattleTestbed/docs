	= Seattle Clearinghouse XML-RPC Client Library =


The Seattle Clearinghouse XML-RPC Client Library is a Python XMLRPC client for communicating with the Seattle Clearinghouse XML-RPC Interface.

You can download the the client from here: [source:seattle/trunk/seattlegeni/xmlrpc_clients/seattleclearinghouse_xmlrpc.py Seattle Clearinghouse Python XMLRPC Client]. Look for the link to "original format" at the bottom of that page to download the file.



### Usage
  1. Download the client code linked to above (it is a Python module).
  1. In your Python script, import seattleclearinghouse_xmlrpc.

  1. Create an instance (or multiple instances, if desired) of the class seattleclearinghouse_xmlrpc.SeattleClearinghouseClient.

     The following parameters can be passed to the constructor:
     * ''username'': Your username. (Required)
     * ''private_key_string'': Your private key. (Either this or the api_key is required)
     * ''api_key'': Your api_key.
     * ''xmlrpc_url'': The url where the Seattle Clearinghouse XMLRPC server is located. (Defaults is our main Seattle Clearinghouse testbed's xmlrpc url.)
     * ''allow_ssl_insecure'': True/False, if set to True, allows SSL to operate in an INSECURE manner. **Do not use allow_ssl_insecure=True in production code.** (Default is False)
     * ''ca_certs_file'': The location of a file containing your trusted CA certificates. (Default is a file named `cacert.pem` in the same directory that you place `seattleclearinghouse_xmlrpc.py` in.)
  1. Once a client object has been created, simply invoke the object's methods.



### Using Secure SSL
In order to perform secure SSL communication with Seattle Clearinghouse:
  * You must have M2Crypto installed.
  * You must set the value of CA_CERTIFICATES_FILE to the location of a PEM
    file containing CA certificates that you trust. If you don't know where
    this is on your own system, you can download this file from a site you
    trust. One such place to download this file from is: http://curl.haxx.se/ca/cacert.pem
        
If you can't fulfill the above requirements, you can still use this client with
XMLRPC servers that use https but you will be vulnerable to a man-in-the-middle
attack. To enable this insecure mode, include the argument `allow_ssl_insecure=True`
when creating a SeattleClearinghouseClient instance.



### SeattleClearinghouseClient Methods
Please note, these methods are not the same as the XML-RPC API calls.
The clientlib methods are simply convenient wrappers for those calls. 
As such, most methods here have identical return values as the actual XMLRPC calls. Refer to the [wiki:SeattleGeniApi Seattle Clearinghouse XMLRPC API spec] for more info about what these functions return.

Available methods on SeattleClearinghouseClient objects:
  The acquire methods all return a list of acquired resources, following the Seattle Clearinghouse XMLRPC API spec.
  * ''acquire_lan_resources(num)'':  Acquires ''num'' LAN VMs.
  * ''acquire_wan_resources(num)'':  Acquires ''num'' WAN VMs.
  * ''acquire_nat_resources(num)'':  Acquires ''num'' NAT VMs.
  * ''acquire_random_resources(num)'':  Acquires ''num'' random VMs.

  * ''release_resources(handlelist)'':  Release all VMs referenced by handles given in ''handlelist''.

  * ''renew_resources(handlelist)'':  Renew all VMs referenced by handles given in ''handlelist'' (that is, extend their expiration dates to 7 days from the current time).

  * ''get_resource_info()'':  Get a list of dictionaries describing all VMs currently acquired by the account. Each dictionary is of the form {'node_ip':node_ip, 'node_port':node_port, 'vessel_id':vessel_id, 'node_id':node_id, 'handle':handle, 'expires_in_seconds':seconds}

  * ''get_account_info()'':  Get account information. This is a dictionary containing the keys{'user_port', 'user_name', 'max_vessels', 'user_affiliation'}

  * ''get_public_key()'':  Get user's public key.

### Exceptions
The following exceptions can be raised by SeattleClearinghouseClient methods:

  * SeattleClearinghouseError -- Base class for all exceptions raised by the SeattleClearinghouseClient.
  * CommunicationError -- Indicates that XMLRPC communication failed.
  * InternalError -- Indicates an unexpected error occurred, probably either a bug in this
    client or a bug in Seattle Clearinghouse.
  * AuthenticationError -- Indicates an authentication failure (invalid username and/or API key).
  * InvalidRequestError -- Indicates that the request is invalid.
  * NotEnoughCreditsError -- Indicates that the requested operation requires more VM credits to
    be available then the account currently has.
  * UnableToAcquireResourcesError -- Indicates that the requested operation failed because Seattle Clearinghouse was unable
    to acquire the requested resources.

See the comments in the seattleclearinghouse_xmlrpc.py file for details on when each exception is raised.



### Example
Here is an example of how to use the Seattle Clearinghouse XML-RPC Client. This could be a python script which you run.

```python
"""
Example of using the seattleclearinghouse_xmlrpc module's SeattleClearinghouseClient.

This script tries to acquire, renew, and release some VMs and prints out
various information along the way.
"""

# This module must be in your python path (for example, in the same directory
# as the current script is in).
import seattleclearinghouse_xmlrpc


USERNAME = "your_username"

# Only one of either the API key or the private key is needed. If providing
# your API key, be sure to pass the API key to the SeattleClearinghouseClient
# constructor below.
#API_KEY = "your_api_key"
PRIVATE_KEY_STRING = open("your_username.privatekey").read()

# Allowing SSL to be insecure means it will be susceptible to MITM attacks.
# See the instructions in seattleclearinghouse_xmlrpc.py for using SSL securely.
ALLOW_SSL_INSECURE = False


def do_example_acquire_renew_release():
  client = seattleclearinghouse_xmlrpc.SeattleClearinghouseClient(username=USERNAME,
                                                private_key_string=PRIVATE_KEY_STRING,
                                                allow_ssl_insecure=ALLOW_SSL_INSECURE)

  # Obtain general information about the account corresponding to the username
  # and API key.
  account_info = client.get_account_info()
  print("Account info: " + str(account_info))

  # Obtain information on VMs already acquired by this account.
  # The value returned is a list of dictionaries where each dictionary
  # describes a VM.
  already_acquired_vessels = client.get_resource_info()
  print("Vessels already acquired: " + str(already_acquired_vessels))

  print("Number of vessels this account has available to acquire: " +
        str(account_info['max_vessels'] - len(already_acquired_vessels)))

  # Attempt to acquire two VMs on WAN nodes.
  try:
    # This is a list of dictionaries just like the one above.
    newly_acquired_vessels = client.acquire_wan_resources(2)
  except seattleclearinghouse_xmlrpc.NotEnoughCreditsError, err:
    print("Couldn't acquire resources because we don't have enough vessel " +
          "credits: " + str(err))
    return
  except seattleclearinghouse_xmlrpc.UnableToAcquireResourcesError, err:
    print("Couldn't acquire vessels because Seattle Clearinghouse doesn't have enough " +
          "of what we asked for: " + str(err))
    return
  print("Acquired WAN vessel: " + str(newly_acquired_vessels))

  acquired_handle_list = []
  for infodict in newly_acquired_vessels:
    acquired_handle_list.append(infodict['handle'])
 
  # Attempt to renew the two VMs we just acquired. 
  try:
    client.renew_resources(acquired_handle_list)
  except seattleclearinghouse_xmlrpc.NotEnoughCreditsError, err:
    # This is probably not going to happen immediately after acquiring vessels.
    print("Couldn't renew vessels because we are over our vessel credit " +
          "limit: " + str(err))
    return
  print("Renewed the vessel we just acquired.")
  
  print("Summary of all of our acquired vessels:")
  all_vessels_list = client.get_resource_info()
  for vesselinfo in all_vessels_list:
    print("Vessel " + str(vesselinfo["vessel_id"]) +
          " on nodemanager accessible at " + str(vesselinfo["node_ip"]) + ":" +
          str(vesselinfo["node_port"]) + " expires in " +
          str(vesselinfo["expires_in_seconds"]) + " seconds.")

  # Release the two VMs we just acquired.
  client.release_resources(acquired_handle_list)
  print("Released the vessel we just acquired.")



def main():
  try:
    do_example_acquire_renew_release()
  except seattleclearinghouse_xmlrpc.Seattle ClearinghouseError:
    # In a real script, you'd want to handle this. Could be an authentication
    # error, communication error, etc. You can use the fine-grained exceptions
    # rather than the base exception of Seattle ClearinghouseError to do different
    # things based on what the actual problem was.
    raise


if __name__ == "__main__":
  main()
```
