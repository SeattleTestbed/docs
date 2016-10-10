# XML-RPC Server for Protogeni Integration
This page describes the XML-RPC server for the Protogeni Integration.
----

----


## Introduction
This is an XML-RPC interface that integrates the Seattle Clearinghouse project with the ProtoGENI project. You do not need to run your own instance of this code to access Seattle Clearinghouse resources through ProtoGENI.   You can leverage an instance of the software which we run to provide resources to ProtoGENI users. An instance of the XML-RPC server is currently running at https://blackbox.cs.washington.edu/xmlrpc/ (note that this page cannot be viewed in html format, can only be accessed via XML-RPC communication.)

This allows users from different project to acquire resources from the Seattle Clearinghouse project as long as they have the proper credentials. Seattle Clearinghouse has implemented the two api calls: CreateSliver() and DeleteSlice(). These two calls allow users to acquire resources and release resources from the SeattleClearinghouse project. The XML-RPC server is located at !https://blackbox.cs.washington.edu/xmlrpc/ A tarball of the XML-RPC server as well as the components required to set it up is attached at the bottom of this page.

The Seattle Clearinghouse project also has its own XML-RPC server which provides a richer interface to interact with Seattle Clearinghouse resources. A description of the Seattle Clearinghouse XML-RPC server and the various api calls that are available can be found at the [wiki:SeattleGeniApi SeattleGENI API] page.



## CreateSliver(argument_dict)
----
CreateSliver is used to acquire resources from the Seattle Clearinghouse project. It takes in a dictionary with three items: slice_urn, rspec and a list of credentials. The dictionary is of the form:
```
   {'slice_urn'   : "urn:publicid:IDN+SeattleGENI+slice+mytestslice",
    'rspec'       : "some_integer", 
    'credentials' : [list_of_credentials]}
```
  1. slice_urn - slice_urn is an urn that describes what slice you want. A description of what urns are can be found [here](http://www.protogeni.net/trac/protogeni/wiki/URNs) 
  1. rspec - rspec is an integer in string form. The integer can be between 1-10. A rspec value of 0 or over 10 will return an unsuccessful result. The rspec is the number of nodes that the user wants to acquire after creating the sliver. An user can acquire a maximum of 10 nodes when creating a sliver. The nodes that are returned are a mix of nodes across the Seattle/MillionNodeGENI.
  1. credentials - credentials is a list of credential that the user can provide. The list for this call should only contain one credential. If more then one credential is provided, then an unsuccessful result is returned. To see what a credential should look like, check below.



## DeleteSlice(argument_dict)
----
DeleteSlice is used to release resources that have already been acquired. By default resources are released after 4 hours due to expiration, however the user can manually release the resources. It takes in a dictionary with two items: slice_urn and a list of credentials. The dictionary is of the form:
```
   {'slice_urn'   : "urn:publicid:IDN+SeattleGENI+slice+mytestslice",
    'credentials' : [list_of_credentials]}
```
  1. slice_urn - slice_urn is an urn that describes what slice you want. A description of what urns are can be found [here](http://www.protogeni.net/trac/protogeni/wiki/URNs) 
  1. credentials - credentials is a list of credential that the user can provide. The list for this call should only contain one credential. If more then one credential is provided, then an unsuccessful result is returned. To see what a credential should look like, check below.



## Credential example for XML-RPC Server
----
In order to access the XML-RPC server for the Protogeni integration. The user needs to have the right credentials and must use it in order to acquire and release resources. Without the correct credentials, an user will receive an error code when they call the two calls CreateSliver() and DeleteSlice(). An example of what the credential will look like is shown below.
```
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
   <signed-credential>
    <credential xml:id="ref1">
     <type>privilege</type>
     <serial>12345</serial>
     <owner_urn>urn:publicid:IDN+emulab.net+user+test_user</owner_urn>
     <target_urn>urn:publicid:IDN+SeattleGENI+slice+mytestslice</target_urn>
     <expires>2010-01-01T00:00:00</expires>
     <privileges>
      <privilege>
       <name>*</name>
       <can_delegate>1</can_delegate>
      </privilege>
     </privileges>
    </credential>
    <signatures>-----BEGIN CERTIFICATE-----
########The emulab certificate for a user.#########
-----END CERTIFICATE-----</signatures>
   </signed-credential>
```

The emulab certificate can be generated through the emulab website, and then copied over from one of the emulab machines.



## Setting up the XML-RPC Server
----
This section describes how to setup the XML-RPC Server. A tarball of the files that are needed to setup and run the XML-RPC server is attached with this page and can be downloaded. There is a README.txt file included in the tarball that also has most of this information included.

Files that are required to setup and run the XML-RPC server:
 * seattlegeni_xmlrpc_server.pl (included)
 * generate_pubkey.py (included)
 * protogeni reference component files.
 * Seattle library files.
 * seattlegeni_xmlrpc.logfile
 * protogeni_user_file.txt
 * protogeni_vessel_handle.txt
 * genica.bundle
 * genicrl.bundle
 * !__lockfile!__
 * seattlegeni_apache.conf
 * prepare_seattlegeni_server.py


### Steps to setup XML-RPC server
----
 1. Create a folder where you want to have the XMLRPC server running from.
 1. Make sure that you have either all the seattle library files in the folder or have the seattle libraries in your PYTHONPATH. If you do not have the Seattle library files you can get it from our svn at https://seattle.poly.edu/svn/seattle/trunk/ Once you have checked out our repository, go into trunk and run the command:
```
$> python preparetest.py /folder/to/copy/seattle_libraries_to
```
 (Note that running this command on a folder will delete any existing file already in that folder. It is best to do this on an empty folder, like in the one created in step 1.)
 1. Download the Reference Component files from the Protogeni site and make sure that all the required libraries are downloaded and installed. Instructions for all of this can be found at: https://www.protogeni.net/trac/protogeni/wiki/ReferenceCM
 1. Run the script prepare_seattlegeni_server.py with the command below where the target folder should be the folder created in step 1. This will copy/create/download the files that are required to run the xmlrpc server.
```
$> python prepare_seattlegeni_server.py target_folder
```
 1. Set up the .conf file for apache. An example of what the .conf file should look like is provided (seattlegeni_apache.conf). A more detailed description on how to edit this file is located at the bottom of this file.
 1. Edit the file protogeni_user_file.txt and add all the Seattle Clearinghnouse users that have been specifically allocated for the protogeni integration. You can acquire Seattle Clearinghouse usernames by registering an username through the Clearinghouse website at: https://seattleclearinghouse.poly.edu . The format of each line in protogeni_user_file.txt is:
```
seattlegeni_username:password_for_user:1:0:0
```
 The last 3 values are set by default to 1:0:0 but this will get changed to some other value after the XMLRPC server has run.
 1. Edit the seattlegeni_xmlrpc_server.pl file to make sure some of the global variables are set correctly if not done so already. The variables that need to be changed if necessary are:
  * $generate_pubkey_path
  * $server_url
  * $protogeni_user_filename
  * $protogeni_vessel_handle_filename
  * $lockfile_path
 1. Edit the generate_pubkey.py file to make sure that the correct path has been set for the Seattle library files. The directory path for the Seattle library files is the same path as the directory where Seattle files were extracted to in Step 2.



### Configuring the seattlegeni_apache.conf file
----
This is a just a very simple description of how to configure the .conf file. More complicated
configuration could be done if necessary. In order to configure the .conf file properly, the
following variables must be modified:

 * The path of the log files must be set correctly. So any errors and access logs are recorded properly.
 * You must have a valid SSL Certificate and set the path to the Certificate file (Line 42)
 * The path for SSLCACertificateFile and SSLCARevocationFile must be set in line 45-46. When the prepare_seattlegeni_server.py file was ran in Step 4, the two files genica.bundle and genicrl.bundle should have been downloaded to the target_folder. Use the file path of these two files as the path for SSLCACertificateFile and SSLCARevocationFile. If the two files were not downloaded, then they could be downloaded here:
   * https://www.emulab.net/genica.bundle
   * https://www.emulab.net/genicrl.bundle
 These files are used to grant access to emulab users.
 * The path to the seattlegeni_xmlrpc_server.pl should be set for the variable ScriptAlias in line 49.
 * The directory where the  XMLRPC server resides should be set at line 51 as the directory path.
 * The location of the Seattle library files that were extracted in Step 2, should be added to the pythonpath in line 61 of the .conf file.

More tutorials on how to configure apache files can be found at the apache website at
http://httpd.apache.org/ under the documentation section.



### Testing the XML-RPC Server
----
We have provided the a test file that tests the two api calls. In order to run it successfully, you will need a valid emulab certificate (emulab.pem) and must have it in the same folder as the test file. The test file must also be modified slightly to include the right certificate and the right filepath for certificate.