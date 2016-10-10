# Security Layer Construction

This page describes how to install Seattle so that it will use custom security layers to impose additional restrictions on API calls.

----



----



## Setting up Seattle
----

First pick which security layers you want to use. One of the layers (probably the last one) should be private_hideprivate_layer.repy, which prevents user programs from accessing files starting with "private_". The node manager will prevent the user from remotely using files starting with "private_", so this creates a protected namespace that can be used for the security layers. The node manager will also preserve files starting with "private_" when a node is reset.

You must create a directory for all files which need to be copied to new VMs. This directory should include private_encasementlib.repy, private_wrapper.repy, the scripts for any security layers, and any other files the layers need to function. All of these files should start will "private_" so that they are not visible to the user.

When installing Seattle, you must include specify the --repy-prepend and --repy-prepend-dir flags. The --repy-prepend directive will be prepended to any repy program run by the user. This should start with "private_encasementlib.repy" and be followed by a list of security layers. You should use --repy-prepend-dir to specify the directory you created for the security layer files.

For example,
```
python seattleinstaller.py --repy-prepend-dir security_layers --repy-prepend "private_encasementlib.repy private_custom_layer private_hideprivate_layer.repy"
```
would install Seattle and cause it to copy all the files in the security_layers directory to new VMs and run user repy programs inside of the security layers. If the user program calls part of the repy API, any file operation will first be sanitized by private_hideprivate_layer.repy to make sure the user can't access to private files, and then any call overridden in private_custom_layer will be passed through that security layer.




## Writing Security Layers
----

To create a custom security layer, [browser:seattle/trunk/seattlelib/private_hideprivate_layer.repy private_hideprivate_layer.repy] is a good starting point for seeing how they are constructed, and the comments in [browser:seattle/trunk/seattlelib/private_wrapper.repy private_wrapper.repy] provide additional information on defining contexts.