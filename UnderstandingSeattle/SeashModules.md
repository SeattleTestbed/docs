# Seash Modules

This page describes the functionality that is available from each available module within [SeattleShell Seash].





## Clearinghouse
----
The Clearinghouse module contains commands that pertain to acquiring and releasing VMs/vessels.  You must use commands in this module as an identity with both public and private keys loaded.



### Acquiring VMs
You acquire VMs using the ```get``` command.  It takes two parameters:  The number of VMs to acquire, and the condition that the acquired VMs must satisfy.  You can omit the type value.  Valid values for type include: wan, lan, and nat.

```sh
 !> loadkeys guest0
 !> as guest0
guest0@ !> get 3 wan
['129.97.74.14:1224']
Added targets: %1(129.97.74.14:1224:v10), %2(129.97.74.14:1224:v4), %3(129.97.74.14:1224:v6)
Added group 'acquired' with 3 targets
```



### Releasing VMs
You release VMs using the ```release``` command, by specifying the group of the VMs you want to release.  If you omit this value, VMs in the default group is released.

```sh
 !> loadkeys guest0
 !> as guest0
 !> loadkeys guest0
 !> as guest0
guest0@ !> browse
['129.97.74.14:1224']
Added targets: %1(129.97.74.14:1224:v10), %2(129.97.74.14:1224:v4), %3(129.97.74.14:1224:v6)
Added group 'browsegood' with 3 targets
guest0@ !> release browsegood
guest0@ !> on browsegood list
guest0@ !>
```





## GeoIP
----
The GeoIP module contains commands that allow you to obtain geographical information about acquired VMs.  To use this module, you must first have browsed for VMs.  You may use these following commands while in a group:

 * show coordinates - Show the longitude/latitude of each VM.
 * show location - Show the city name (if available) and country of which each VM resides in.

```sh
user@all !> show location
%1(143.215.131.199): Atlanta, GA, United States
%2(129.97.74.14): Waterloo, ON, Canada

user@all !> show coordinates
%1(143.215.131.199): 33.8004, -84.3865
%2(129.97.74.14): 43.4667, -80.5333
```



## Modules
----
This module contains commands that manipulate modules within seash.  You can use commands within this module to enable and disable modules.


### Current Module Information
To view information on all currently installed modules, you can use the ```show modules``` command.
```
user@ !> help show modules
show modules

Shows information on all installed modules.  Modules will be separated into 
two categories: enabled and disabled.  Each entry will be in the following 
format:
  [module name] - [URL where the module was installed from, if available]

The URL will be missing if the module was installed manually.


user@ !> show modules
Enabled Modules:
geoip - https://seattle.poly.edu/plugins/geoip/

Disabled Modules:
selexor - https://seattle.poly.edu/plugins/selexor/  

```


### Module-Level Help
To view information about a particular module, use the ```modulehelp modulename``` command.  This helptext is defined by the module creator.
```
user@ !> modulehelp geoip
GeoIP Module

This module includes commands that provide information regarding VMs' geographical 
locations.  To get started using this module, acquire several VMs through the Seattle
Clearinghouse, use the 'browse' command, and then in any group, run either 'show location' 
or 'show coordinates'.


show location    -- Display location information (countries) for the nodes
show coordinates -- Display the latitude & longitude of the node

```


### Installing/Uninstalling Modules
To install a new module, you can use the ```install``` command.
```
user@ !> help install
install modulename url_to_module

Downloads the specified module as modulename and enables it if possible.  
The module will be automatically updated when you run seash.


user@ !> install selexor https://seattle.poly.edu/plugins/selexor
Module 'selexor' has been successfully installed and enabled.

user@ !> install selexor https://seattle.poly.edu/plugins/selexor
Module 'selexor' already exists.  You can either uninstall it using 'uninstall'
or install it under a different name.

```

To uninstall an existing module, you can use the ```uninstall``` command.

```
user@ !> help uninstall
uninstall modulename

Uninstalls the specified module.  Use with caution, as you cannot undo this action!
You can use 'show modules' to view a list of all installed modules.


user@ !> uninstall selexor
Module 'selexor' has been successfully uninstalled.

user@ !> uninstall selexor
Module 'selexor' is not installed.

```



### Enabling/Disabling Modules
Modules are imported when you initially start seash, but they may not be enabled depending on conflicting modules, you disabled them on a previous run, etc.  To enable a module, use the ```enable``` command:
```
user@ !> help enable
enable modulename

Enables use of the specified module.  You can only enable modules if they do not
contain commands that conflict with existing commands.


user@ !> enable modulename
user@ !> enable modulename
Module 'modulename' is already enabled.

user@ !> enable conflictingmodule
Module 'conflictingmodule' cannot be enabled due to these conflicting commands:
show info (default)
get (selexor)

user@ !>
```

Similarly, you can disable modules using the ```disable``` command.  This is useful if you have modules that have conflicting commands.  You can disable a module you're not currently using and enable the new module to use the conflicting command.
```
user@ !> help disable
disable modulename

Disables the specified module.  You will no longer be able to access the commands 
that were found in the disabled module until the module is re-enabled.


user@ !> disable modulename
user@ !> disable modulename
Module 'modulename' is not enabled.

user@ !> 
```





## Variables
----
This module allows you to define custom user variables.  The values of these variables can then be retrieved later.

To define a variable, use the ```set``` command.  You can then retrieve the value later by prepending $ to the respective variable name.
```
user !> set username myusername
user !> as $username
myusername !>
```

You may also enclose the variable name with $'s if you do not want a space to be appended after the variable's value.  A case when this is useful is when you want to refer to a directory name.
```
 !> set username myusername
 !> loadkeys /home/$username$/mykey as $username
 !> as $username
 myusername !>
```





## Factoids
----
The Factoids module prints random factoid when you run [SeattleShell Seash]. It also contains a command which allows you to see available factoids which is:

 * show factoids [number of factoids]/all - Prints factoids onto the screen. You can specify the number of factoids you want to see or you can specify 'all' to see all available factoids.

```
user@ !> show factoids 2
- You can save seash's current state using 'savestate' command.
- You can load seash's previous state using 'loadstate' command.

user@ !> show factoids all
- You can save seash's current state using 'savestate' command.
- You can load seash's previous state using 'loadstate' command.
- You can set user variables using 'set' command.
- You can press the Tab key to enable tab complete when typing commands.
- You can see available seash factoids using 'show factoids [number of facctoids]/all' command.
- You can list all available seash modules using 'show modules' command.

user@ !>
```