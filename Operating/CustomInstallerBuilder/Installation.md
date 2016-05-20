# Installing the Seattle Custom Installer Builder

This page outlines how to install the Custom Installer Builder (including its dependencies) on a Linux machine.

------
## Before you begin

We recommend you read up on [SeattleInfrastructureArchitecture](https://github.com/SeattleTestbed/docs/blob/master/UnderstandingSeattle/SeattleInfrastructureArchitecture.wiki)  how the Seattle infrastructure architecture looks like so that you have a good understanding of the components you want to have (and thus need to set up).

Also, there are different deployment paths to get you the functionality you want. Keep those in mind when configuring Apache later.

## Setting up a user account
First of all, on your custominstallerbuilder server or VM, we recommend to set up a new Linux user account specific to the Custom Installer Builder instance you are going to set up. This ensures all of the code, config files, etc. remain isolated from that of other services on the same machine.

The user *should not be granted interactive login* for security reasons. Use `sudo -i -u thenewusername` instead to work in their directory. Needless to say, the user should **not** have root privileges or be able to acquire them.

Any user name will be fine. We'll use `cib` in the instructions.


## Install Dependencies
The Custom Installer Builder requires a few pieces of software to run:
 * [Python](http://www.python.org/) in version 2.5-2.7 -- the language Custom Installer Builder is written in
 * [Apache](http://www.apache.org/) -- the web server
 * [mod_wsgi](http://www.modwsgi.org/)  -- necessary for interfacing with Django code
 * [Django](http://djangoproject.com) -- necessary to run Django code
 * zip -- necessary for packaging window installers and keys 
 * [Git](https://git-scm.com/) -- source code management system, used to install Seattle dependencies
 * [Pip](https://pypi.python.org/pypi/pip/) -- Python package management tool

Python is often available on a typical Linux install. Be sure to check the version though, we need 2.5, 2.6, or 2.7.

To install the other packages, log in as a `sudo`able user and type
```sh
$ sudo apt-get install apache2
$ sudo apt-get install libapache2-mod-wsgi
$ sudo apt-get install ntp
$ sudo apt-get install zip
$ sudo apt-get install git
$ sudo apt-get install python-pip
```

### Consider using virtualenvironments
You maybe want to have a look at the section on [virtualenvs in Seattle Clearinghouse](https://github.com/SeattleTestbed/docs/blob/master/Operating/Clearinghouse/Installation.md#use-virtualenvironment-optional-but-highly-recommended) Insallation guide. 

### Install Django
The Custom Installer Builder requires Django, a Python web framework, in version 1.6.5 or greater, which is available at  [https://www.djangoproject.com/download/](https://www.djangoproject.com/download/) or through a package manager.

```sh
$ sudo pip install django==1.6.7
```

## Download Custom Installer Builder code base
Now *log in as the user who will be hosting the Custom Installer Builder* (in our case that's `cib`). Check out the Custom Installer Builder code base from GitHub:

```sh
$ sudo -i -u cib
[sudo] password for currentuser:
$ git clone https://github.com/aaaaalbert/custominstallerbuilder.git -b django16support
```

In the `custominstallerbuilder` directory created through this, locate and `cd` into `scripts/`, and run the init script:

```sh
$ cd custominstallerbuilder   # The repo just cloned
$ cd scripts   # Part of said repo
$ python initialize.py
```

This goes and clones additional repositories that are required for building installers into the directory `../DEPENDENCIES`.

## Create Repy runtime
The Custom Installer Builder uses Repy for some of its functionality. Create a Repy runtime in `~/repy_runtime` like so:

```sh
$ # While still in the scripts/ directory
$ mkdir ~/repy_runtime
$ python build.py ~/repy_runtime
```

## Done (for now)
That's it! You now have all of the code and config files required for the Custom Installer Builder in place!

Continue to [configuration](https://github.com/SeattleTestbed/docs/blob/master/Operating/CustomInstallerBuilder/Configuration.md), then [customization and build](https://github.com/SeattleTestbed/docs/blob/master/Operating/CustomInstallerBuilder/CustomizationAndBuild.md), [running a test server](https://github.com/SeattleTestbed/docs/blob/master/Operating/CustomInstallerBuilder/Testing.md), and [running a production server](https://github.com/SeattleTestbed/docs/blob/master/Operating/CustomInstallerBuilder/Deployment.md).
