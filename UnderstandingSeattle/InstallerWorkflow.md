# Installer Workflow

This document describes how installers work, specifically how the clearinghouse uses the [wiki:Archive/CustomInstallerBuilderTesting custom installer builder] to track and manage user installations.   One thing that is often surprising to people is that the installer the user downloads from a clearinghouse, comes from the custom installer builder (over XMLRPC).   In fact, nowhere in the installer does it explicitly mention the clearinghouse.   The installer is indistinguishable from a user created installer.

Before understanding how this works, it is important to first understand how users can locate VMs that have their public key.   

JAC: the doc needs node state transitions explained.


## Overview
Seattle uses the [wiki:Archive/CustomInstallerBuilderTesting custom installer builder] to generate Seattle installers.  A unique installer is generated dynamically by the CIB every time a user clicks download. A Seattle Clearinghouse frontend specifies which custom installer to use in website/settings.py.

```py
41 # The XML-RPC interface to the Custom Installer Builder.
42 SEATTLECLEARINGHOUSE_INSTALLER_BUILDER_XMLRPC = "https://custombuilder.poly.edu/custom_install/xmlrpc/"
```

 * Unless in the rare case a Clearinghouse instance is running it's own custom installer builder, SEATTLECLEARINGHOUSE_INSTALLER_BUILDER_XMLRPC should be set to the same value as in trunk (like above). 
 * Using the custom installer builder is the only way a Clearinghouse instance should generate installers.
 * The custom installer builder is a web application separate from the Seattle Clearinghouse application.  

## High Level Event Sequence
1. A user clicks on a 'Download Installer for "platform"' link on a Seattle Clearinghouse.
This request is sent to the Custom installer builder server associated with that Clearinghouse.

2.The custom installer builder dynamically creates a installer for this request based on which platform was specified.
This dynamic installer is created by bundling a platform specific base installer (already on the CIB server) with the donation public key of the user sending the request.  This donation public key is transparent to the user.    

3. The custom installer builder sends the URL of the dynamically created installer to the clearinghouse.

4. The user downloads the requested installer from this URL.


## Base Installer
The base installers of the custom installer builder are created by running dist/make_base_installers.py.  This program must be passed in a public and private key.  These keys are used to identify the custom installer builder that the installers are associated with.  These base installers are used to dynamically generate all installers created by the custom installer builder server.

Example of usage on command line:
```sh
$ python ./Seattle/trunk/dist/make_base_installers.py a ./Seattle/trunk/ user.publickey user.privatekey ./Installers/
```

## Custom installer workflow
The custom installer creates a vesselinfo file that is used by the nodemanager upon installation. This vesselinfo file dictates how the vessels are created. A default vesselinfo file is provided, but if you would like more control over how the resources on your machine are split up between your different vessels/VMs, or would like to dedicate specific vessels to specific users, you may also do that through the custom installer builder.

A copy of the base installer is made for each user. The custom installer builder accepts a donation public key and creates a vesselinfo file. After this file is embedded into the installer, the installer is complete and may be distributed to users.
More information can be found at [wiki:BenchmarkCustomInstallerInfo].

## Placeholder
TODO add information about transition scripts and crediting of donations.