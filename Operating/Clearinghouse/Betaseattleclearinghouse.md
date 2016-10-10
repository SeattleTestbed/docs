# Beta Clearinghouse

The Beta Clearinghouse is the machine that holds the beta version of our public clearinghouse as well as a small beta network where a 
handful of Seattle nodes are deployed for beta testing. Everything that is pushed on to the production must first be deployed on the 
Beta Clearinghouse and tested for bugs and discrepancies before we can safely push it to the production clearinghouse or the production
nodes.
[[br]]

__** Machine Host Name:**__
[[br]]
**[betaseattleclearinghouse.poly.edu](http://betaseattleclearinghouse.poly.edu)** 
[[br]]
__Operating System__: Red Hat 4.4.6-4
----

----

## Services on Betabox
### Clearinghouse
----
The beta clearinghouse is a collection of nodes that runs on the beta testbed. The beta version may have bugs in them as this is where the developers
test out all the latest features of the product. The clearinghouse consists of the main front end webserver which allows users to register or login to
their public testbed account in order to donate or acquire nodes in order to run their experiment. 
[[br]]
The service is run under the user: **geni**
[[br]][[br]]
Instructions on how to deploy a new clearinghouse can be found at this page: [wiki: SeattleGeniInstallation]. If you are moving the clearinghouse from one machine to another, then you may also need to copy over the two databases **keydb** and **seattlegeni** database. Instructions on how to backup and restore mysql databases can be found on this page: [BackupRestoreMySQL](http://www.thegeekstuff.com/2008/09/backup-and-restore-mysql-database-using-mysqldump/). Note that the username and password for each of the databases can be found in the file /home/geni/database_info.txt on the system.

#### Known Issues
While loading the clearinghouse on to the new machine, there were some issues that we needed to get around due to the operating system/default configurations already on the machine.

__Configuring Apache:__
The version of Apache available on RedHat is slightly different then the one available on Ubuntu/Mint or other distros. The installation path is in /etc/httpd/. The configuration file is located at /etc/httpd/conf/httpd.conf. Below are some of the issues that I ran into while configuring the Apache conf file.
[[br]]
 * Load ssl module. The ssl module was initially not installed on the machine. In order to install it, run the command:
```
# yum install mod_ssl
```
 Once installed, open up the httpd.conf file and add this line after all the LoadModule lines:
```
LoadModule ssl_module /modules/mod_ssl.so
```
 * Load python module. The python module was not available from the package manager so I had to manually install this. First retrieve the tarball of the latest version from here: [PythonModule](http://archive.apache.org/dist/httpd/modpython/). In order to install mod-python, you must first also install have apxs installed as well as the python-devel library package installed. Run these commands:
```
# yum install httpd-devel
# yum install python-devel
```
 Once these libraries are installed, and you have downloaded the mod_python tarball, run these commands.
```
# tar xzvf mod_python-3.3.1.tgz
# cd mod_python-3.3.1
# ./configure --with-apxs=/usr/sbin/apxs --with-python=/usr/bin/python2.6
# make 
# make install
```
 **BUG:** The mod_python file that you downloaded may have a bug in it. Please go to this [BugReport](https://bugzilla.redhat.com/show_bug.cgi?id=465246) to apply the patch if running make throws an error.

 * Make sure to listen on the proper ports in the Apace configuration file.
```
Listen 80
Listen 443
```
 * The Python path needs to be set properly.  The Django section in the Apache configuration file should look similar to this:
```
 # Django
    <Location /geni/>
        SetHandler python-program
        PythonHandler django.core.handlers.modpython
        SetEnv DJANGO_SETTINGS_MODULE seattlegeni.website.settings
        PythonOption django.root /geni
        PythonInterpreter geni
        PythonPath "['/home/usr/tmp', '/home/usr/tmp/seattle', '/usr/lib/python2.6/site-packages'] + sys.path"
        PythonDebug On    
    </Location> 
```
   '/home/usr/tmp' is the location of the deployed seattle and seattlegeni folders.
   '/usr/lib/python2.6/site-packages' is the location of Django.

 * Make sure the Apache user has proper permission to access the Seattle Clearinghouse code.   Apache requires read and execute permissions for the seattle and seattlegeni directories. To ensure Apache has the correct permissions, run the following command in your Seattle Clearinghouse directory:
```
# chmod -R o+rx seattle/ seattlegeni/
```
### Custominstaller Builder
### Central Advertise Server V2
### Installer Builder/Software Updater Server
