# Using Seattle on the Nokia N800 and N810
This article is comprised of three sections: The first section explains how to install Seattle on the Nokia N800 Internet Tablet. The second section (optional) explains how to run the Seattle unit tests on the Nokia N800 Internet Tablet. The third section describes the modification necessary to run Seattle on the N810.
----

----

## Setting up Seattle


### Tools Required
In order to run Seattle, you will need: Python, and root access to the system in the tablet. These can be obtained through the Application Manager. 


 1. In the top menu, go to Tools -> Application Catalog. 
 1. Select the "maemo extras" entry and Edit. 
 1. Uncheck the "disabled" box. 
 1. Refresh the installable package list, and packages that are required should now show up.




#### Python
For Python, you will need to install the "maemo-python-env" package. This will install Python 2.5 onto the tablet.




#### Root access
This is only required for the installation of Seattle. In particular, root access is required to configure Seattle to run on startup. There are several ways to obtain the root shell access. This article will describe two easy ways by which root shell access can be obtained.

##### rootsh
Find and install the "rootsh" package. The root shell package allows the user to gain root access through a simple command: "sudo gainroot" or simply "root".

##### openssh
Find and install "openssh" package. During installation the first time, you will be prompted for a new password. Enter your password of choice and remember it for later. Root shell access can be obtained using "ssh root@localhost". You will be prompted for the password you entered during installation.




### Installation
 1. Download the Seattle tarball (Installer for Linux) [here](https://betabox.cs.washington.edu/geni/download/tukwila/). 
 1. Next, extract the tarball, and navigate to the Seattle directory. 
 1. Install Seattle.
  1. You will need root access to configure Seattle to run on startup properly during installation. See above on how to gain root access. 
  2. To install, run **./install.sh**. Seattle will be configured to run on startup. In addition, Seattle will be started after installation. 
  3. To check that it is running, run the command
```
ps -f | grep nmmain.py | grep -v grep
```
 1. To stop Seattle, run **./stop_seattle.sh**. Run **./start_seattle.sh** to restart it. You will not need root access for either of these.
 1. Uninstallation:
  1. You will again need root access to uninstall properly. This stops Seattle from running on startup.
  1. Run **./uninstall.sh**.




----
## Running Seattle Unit Tests (Optional)
Note: This part is **optional** and not required for the installation of Seattle.




### Directions
 1. The tarball for the unit tests can be obtained [here](https://seattle.poly.edu/static/nokiadev/seattle_testnokia-r3516.tgz). The tarball contains all of the repy files necessary to run the unit tests as a standalone.
 2. Untar the file by doing the following:
```
tar zxf seattle_testnokia-r3516.tgz 
```
 3. Change into the seattle directory, and run the unit tests by doing:
```
python utf.py -m repytests
```
 4. The unit tests should take about an hour. In the end it will report the number of passes/failures.



----
## Notes for Nokia N810 Tablet
This section describes the difference between the above N800, and the N810 installation.





### Python

For Python, you will need to install the "maemo-python-device-env" package; however, this Python package lacks some important modules which Seattle uses. You must add these modules manually.

For Python 2.5.2, you might not be able to install Seattle due to two missing packages: compiler.py and getpass.py. To overcome this setback:

 1. Visit http://www.python.org/download/releases/2.5.2/ and download the 2.5.2 release for other platforms;
 2. unpack the downloaded file;
 3. locate the files compiler.py and getpass.py and copy them to where maemo-python-device-env was installed on N810 (somewhere on your pythonpath).
 4. Install Seattle as usual.





### N810 Notes:

 1. You will just locate the files you need from the release downloaded from the Python official website and copy them. Do not install the release!

 b. to check where maemo-python-device-env was installed you could use the following lines in Python interactive mode:

```
import sys
print sys.path
```



