The demokit packages up a set of tools for Seattle users that allow you to 
 * Access VMs on remote machines, for example such assigned to you by the [Seattle Clearinghouse](https://seattleclearinghouse.poly.edu)
 * Run RepyV2 code on your local machine, using a supplied restrictions file, and thusly
 * Develop and debug Repy programs locally.


# Building the Demokit

Building the demokit is as simple as 
 * Cloning the [demokit repo on GitHub](https://github.com/SeattleTestbed/demokit),  
 * Running `scripts/initialize.py` inside of it, and lastly 
 * Creating an empty target directory, and lastly 
 * Changing directory into `scripts/dist` in order to run `python build.py` with the full path to the target dir as an argument.

See the wiki:BuildInstructions for details about using Seattle's build scripts.

-----

Note for developers: The current demokit build scripts do not yet
 * Copy over `seash` modules to the target directory, nor 
 * Create a tarball out of the target dir. Neither will it 
 * Supply a copy of demo apps to run (as these are currently being ported to RepyV2).
