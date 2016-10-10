# Seash: The Seattle Shell
Seash is a terminal interface for managing Seattle resources. This page is intended as a short overview of commands that one can run in Seash.



## Starting Seash
Seash can be started from the terminal by running the command ```python seash.py```. Once Seash starts, it will print a line that starts with ```!>```, and will wait for you to issue a command.


## Seash Commands
If you issue the ```help``` command in Seash, you will receive an output that describes all the commands Seash supports. Here's a listing of this output:

```
A target can be either a host:port:VMname, %ID, or a group name.

on target [command]              -- Runs a command on a target (or changes the default)
as keyname [command]             -- Run a command using an identity (or changes the default).
add [target] [to group]          -- Adds a target to a new or existing group 
remove [target] [from group]     -- Removes a target from a group
show                             -- Displays shell state (use 'help show' for more info)
set                              -- Changes the state of the targets (use 'help set')
browse                           -- Find VMs I can control
genkeys fn [len] [as identity]   -- creates new pub / priv keys (default len=1024)
loadkeys fn [as identity]        -- loads filename.publickey and filename.privatekey
list                             -- Update and display information about the VMs
upload localfn (remotefn)        -- Upload a file 
download remotefn (localfn)      -- Download a file 
delete remotefn                  -- Delete a file
run file [args ...]              -- Shortcut for upload a file and start
start file [args ...]            -- Start an experiment
stop                             -- Stop an experiment
split resourcefn                 -- Split another VM off of each vessel
join                             -- Join VMs on the same node
help [help | set | show ]        -- help information 
exit                             -- exits the shell
```



## Using Modules
----
In addition to using built-in Seash commands, additional functionality can be added into Seash by using modules.  More information about specific modules can be found at the [SeashModules Seash Modules page].  Manipulation of modules can be done through the [SeashModules#modules Modules module].



### Input Parsing
Modules may also modify your command line input before they reach the command parser.  An example of this would be the variables module.  When this occurs, the resulting parsed string is displayed underneath your input by default.  This can be toggled by using the ```set showparse``` command:

```
 !> set showparse on
 !> set username myname
 !> loadkeys ..
keys
$username
Parsed as: loadkeys ..
keys
myname
(You can disable displaying parsed input by using 'set showparse')
 !> as $username
Parsed as: as myname

myname@ !> set showparse off
myname@ !> set username myname
myname@ !> loadkeys ..
keys
$username
myname@ !> as $username
myname@ !>
```




## Further Information
----
For more information on how to use Seash in practice, refer to the [EducationalAssignments/TakeHome Take Home Assignment].

For more information on how Seash works, refer to the [SeattleShellBackend backend page].