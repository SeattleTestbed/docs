# SSH Services


----



## SSH Configuration on *NIX
----

We use the latest version of OpenSSH on our Linux/BSD/OpenSUSE/OSX machines.



## SSH Configuration on Windows
----

We use a free program called [Moba SSH](http://mobassh.mobatek.net/en/) for SSH access on Windows.



### Installation and Configuration
----

 1. **Download:** Grab the install file by visiting the Moba SSH website. Go to the [download link](http://mobassh.mobatek.net/en/index.php?option=com_content&view=article&id=93&Itemid=55) and get the latest version. Currently the machines in Sieg 319 are running MobaSSH Home v1.0.
 1. **Installation:** Create a file in C:
Program Files
 called MobaSSH and save the downloaded file there. Run the exe file and follow the instructions. Once the installation is complete the interactive window should say "MobaSSH service is running" and "Installed version is up to date". In the task manager MobaSSH.exe should be running under the user sshdsvc. All the users should be automatically added and have permission to ssh into the machines. 
 1. **Configuration:** Most likely the windows firewall will be trying to block any incoming connection from other computers, so we will add an exception for this. We are running SSH on port 22 by default so go to the control panel > Windows Firewall. Under the exceptions tab click on 'Add Port'. Name should be SSH and Port Number should be 22. Make sure that its TCP and not UDP. Click OK and make sure that under the exceptions tab SSH is ticked in the 'Programs and Services' window.
 1. **Python and SVN Setup:** Normally if you ssh into the windows machine, python will not work because MobaSSH will not be able to find the Python directory. Therefore to get Python working go to the directory: C:
WINDOWS
system32
bsh
bin or its equivalent. Create a file and name it 'python'. Make sure that the file has no extension (i.e. no .txt extension.) Open up the file and add the two lines:
```/bin/bash
exec /cygdrive/c/Python25/python ${1+"$@"}
``` 
 This will tell the ssh program to look for python.exe in C:
Python25. Note that /cygwin/c corresponds to C:
 so make sure that you put the appropriate address in the file 'python'. Now you should be able to run python programs properly by SSHing into the windows machine. To run the interactive mode of python, type:
```
python -i.
```
 The same thing must be done for SVN. Before the next step, make sure you have the latest version of SVN installed. You can get the latest version from [subversion.tigris page](http://subversion.tigris.org/servlets/ProjectDocumentList?folderID=8100&expandFolder=8100&folderID=91). Create a file called svn without any extension, and add these two lines:
```/bin/bash
exec /cygdrive/c/Program
 Files/Subversion/bin ${1+"$@"}
```
 Now we have to edit the environment variable PATH. Note that even though we added the python and ssh file in C:
WINDOWS
system32
bsh
bin, typing in 'python' or 'svn' will only work in cygwin. Suppose we want to use the 'cmd' command after we ssh into the windows machine and then want to run python program, then we need to edit the PATH variables. To do this we have to edit the file 'profile', which is located at C:
WINDOWS
system32
bsh
etc
profile, or if you are sshing into the machine its located at /etc/profile. Open up the file and the following should be the value of your PATH variable (or its equivalent, depending on where you installed Python and SVN):
```
PATH=.:/cygdrive/c/WINDOWS/system32:/usr/bin:/bin:/usr/sbin:/usr/local/bin:/cygdrive/c/Python25:/cygdrive/c/WINDOWS/system32:/cygdrive/c/Program
 Files/Subversion/bin:$PATH
```
 Note that in the path directory '/' automatically refers to C:
WINDOWS
system32
bsh
, so /usr/bin is equivalent to C:
WINDOWS
system32
bsh
usr
bin. The path directory C:
 is equivalent as /cygdrive/c. So C:
Program Files would essentially be /cygdrive/c/Program
 Files.
 
 **WARNING:** Everytime MobaSSH is restarted, this PATH value gets changed back to its default value. When MobaSSH is restarted, the PATH value must be changed. 
 1. **Final Test:** Go to a different machine and make sure you can use ssh to access the machine. The two windows machine name should be testbed-vista1.cs.washington.edu and testbed-xp2.cs.washington.edu
 1. **Adding New Users:** When you create a new user on the Windows machine, MobaSSH has to be restarted or they do not get SSH access. Remember that everytime MobaSSH is restarted, the PATH value gets changed, so it must be fixed.
 1. **Advanced Configuration:** You can manually choose which users will have ssh access manually. To do this open up the exe file in C:
Program Files
MobaSSH. Hit the Users button on the right side of the panel and click on 'Selected users'. Once you have chosen all the users click on Restart button under the 'MobaSSH Service is running' on the left side of the panel. Any changes you made will not take place until you restart the MobaSSH service.

