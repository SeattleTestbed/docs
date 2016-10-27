# Benchmark and Custom Installer Info





## Necessary files
Before the installer can run, the client must performing benchmarking and set the initial VM state. The following files are critical to this process, which is conducted by benchmark_resources.py.

Files common to all distributions (without modification):
 * vessel.restrictions
 * resources.offcut

Files customized for each distribution:
 * vesselinfo — Partitions system resources into VMs, each with an owner and several users. Owners and users are identified by a public key.

Python modules:
 * seattleinstaller.py
 * benchmark_resources.py — Manages and runs the benchmark scripts as well as operating the create_installer_state module.
 * create_installer_state.py — Responsible for reading the vesselinfo file and taking the resource information to initialize the VMs.
 * Win_WinCE_resources.py — Performs resource benchmarking for Windows and Windows CE platforms.
 * Mac_BSD_resources.py — Performs resource benchmarking for Mac OS X and BSD platforms.
 * Linux_resources.py — Performs resource benchmarking for Linux.
 * measuredisk.py — A tool used by the above benchmarking scripts.
 * measure_random.py — A tool used by the above benchmarking scripts.




## ''vesselinfo'' formatting

### Example
The following is a sample ''vesselinfo'' file. Actual owner/user public keys will be much longer.

```
Percent 40
Owner 123456789123 123456789123456789123456789
User 23456789123 23456789123456789123456789
Percent 20
Owner 3456789123 3456789123456789123456789
Percent 20
Owner 456789123 456789123456789123456789
```

### Format requirements
Restrictions on vesselinfo (failure in any of these results in a completely failed install):

 * Percentages must have integer values.
 * There can be no empty lines.
 * The sum of all percentages must be 100.
 * The labels "Percent", "Owner", and "User" are case sensitive.
 * The values for Owner and User should be public key strings that can be read by rsa_string_to_publickey. Do not provide file names.
 * The ''vesselinfo'' file must be in the same directory as seattleinstaller.py.




## Build steps
 1. The server collects the necessary information to create a ''vesselinfo'' file and places it into the base installers. Donors download these customized installers.
 1. The donor starts installation. By default, 10% of his computing resources are made available for VMs, but a custom value can be passed as an argument to the installer.
 1. The installer conducts several important checks and performs benchmarking by calling ''benchmark_resources.main''
   1. A temporary file is open/appended for logging, because service logger cannot be used until the VMs have been created (specifically vessel directory v2). Information about the benchmark and any exceptions will be logged here.
   1. The ''vesselinfo'' file is transformed into a list by ''create_installer_state.read_vessel_info_from_file''. Any errors in the ''vesselinfo'' file will result in the install stopping completely. This is not recoverable and the errors will be logged.
   a. ''run_benchmark'' is called to get a dictionary containing the maximum available resources.
     i. The scripts Linux_resources.py, Mac_BSD_resources.py, Win_WinCE_resources.py, measuredisk.py, and measure_random.py will be used to generate this dictionary, and resources that are not measured by the scripts will be set as None.
     i. The result from the scripts will be checked, to ensure that values are valid, non-negative, and not None. Bad values are logged and default values will be used.
   a. ''get_donated_from_maxresources'' uses the maximum available resources and the percentage defined by the user to create a dictionary with the total donated resources.
   1. the number of VMs is determined and the required offcut resources are removed from the donatedresources.
     * This is done to here instead of during construction of individual VM resources to simplify the process.
     * offcut resources are the cost of an individual VM, even though we do not technically "split" vessels in this code, we must still account for the overhead of creating multiple vessels. 
   1. the donated resources are now chopped down by ''get_tenpercent_of_donated'' to get ten percent of the donated resources (this is ten percent because the VMs are given resources from the donated resources in increments of 10%).
   a. ''create_installer_state.main'' takes the vesselcreationlist, tenpercentdict, and the target directory and initializes the VM states.
 1. If the installation worked correctly the service logger is initialized and the log file used during the benchmark and creation of VMs is transfered and the file is removed. The installation continues as normal in seattleinstaller.py
