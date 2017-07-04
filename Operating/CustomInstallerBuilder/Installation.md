# Installing the Seattle Custom Installer Builder

This page outlines how to install the Custom Installer Builder (including its dependencies) on a Linux machine. We recommend you read up on [Seattle Infrastructure Architecture](https://github.com/SeattleTestbed/docs/blob/master/UnderstandingSeattle/SeattleInfrastructureArchitecture.wiki) how the Seattle infrastructure architecture looks like so that you have a good understanding of the components you want to have (and thus need to set up).

## Setting up a non-privileged user account
First of all, on your custominstallerbuilder server or VM, we recommend to set up a new Linux user account specific to the Custom Installer Builder instance you are going to set up. This ensures all of the code, config files, etc. remain isolated from that of other services on the same machine.

The user *should not be granted interactive login* for security reasons. Use `sudo -i -u thenewusername` instead to work in their directory. Needless to say, the user should **not** have root privileges or be able to acquire them.

Any user name will be fine. We'll use `cib` in the instructions.

```sh
$ sudo adduser cib
```

## Install Dependencies
The Custom Installer Builder requires a few pieces of software to run:
 * [Python](http://www.python.org/) in version 2.7 -- the language Custom Installer Builder is written in
 * [Pip](https://pypi.python.org/pypi/pip) -- recommended tool for installing python packages.
 * [Apache 2.4](http://www.apache.org/) -- the web server
 * [mod_wsgi](http://www.modwsgi.org/) -- necessary for interfacing with Django code
 * [OpenSSL](http://www.openssl.org/) -- necessary for `https://` support
 * zip -- necessary for packaging window installers and keys 
 * [Django](http://www.djangoproject.com/) in version 1.8.x -- necessary to run Django code


Python is often available on a typical Linux install. Be sure to check the version though, we need 2.7.

To install the other packages, log in as a `sudo`able user and type
```sh
$ sudo apt-get install python-pip
$ sudo apt-get install python-dev
$ sudo apt-get install apache2 libapache2-mod-wsgi
$ sudo apt-get install ntp
$ sudo apt-get install zip
$ sudo apt-get install openssl

```

### Setup python virtualenvironment
A convenient way to isolate your Python installations from each other is to use `virtualenv`, e.g. if you have specific version requirements for one project, but don't want to apply them system-wide or for other projects. [Virtualenv](https://virtualenv.pypa.io/en/latest/index.html) creates a separate environment that has its own installation directory and that doesn’t share libraries with other virtualenv environments. The [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) makes usage of virtualenv even easier. With the following instructions you can install and setup virtualenv and virtualenvwrapper and create a virtualenv called `cib` which can be used to install your Seattle Custom Installer Builder django installation.

```sh
$ # Install virtualenv and virtualenvwrapper
$ sudo pip install virtualenv
$ sudo pip install virtualenvwrapper

$ # Login as user above created
$ sudo -i -u cib

$ # Create a directory in your home folder where all your virtualenvs will live
$ mkdir ~/.virtualenvs
$ # Make the virtualenvwrapper available
$ echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
$ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
$ source ~/.bashrc

$ # Create a new virtualenv called `cib` and immediately switch to it.
$ mkvirtualenv cib
```

In the future you just have to issue the shell command `workon cib` to switch to the environment or `deactivate` if you want to leave it. You know that you are *in* the virtualenv when your shell prompt is prefixed by `(cib)`. **Note: This prefix is omitted in the shell snippets in the remainder of the document.**

### Install Django
The Custom Installer Builder requires Django, a Python web framework, in version 1.8, which is available at  [https://www.djangoproject.com/download/](https://www.djangoproject.com/download/) or through a package manager.

```sh
$ pip install django==1.8.18
```

## Deploying and running Custom Installer Builder

1. Make sure you are logged in with your Custom Installer Builder account: `sudo -i -u cib`
1. Clone the Custom Installer Builder repository into `cib`'s home directory, and let the initialize script fetch dependencies:

```sh
$ cd ~
$ git clone https://github.com/SeattleTestbed/custominstallerbuilder.git
$ cd custominstallerbuilder/scripts
$ python initialize.py
```

1. Create Repy runtime, e.g. in `~/repy_runtime`, which will be needed by the Custom Installer Builder

```sh
$ # While still in the scripts/ directory
$ mkdir ~/repy_runtime
$ python build.py ~/repy_runtime
```
1. Change to the `custominstallerbuilder` directory we checked out earlier and edit `local/settings.py` to match your local configuration:
  * `SECRET_KEY` should be a random string of your own choosing. Do not share it with others! If you are testing locally, using django's built-in webserver, use `http://127.0.0.1:8000/` as `BASE_URL`. This tutorial will show you how to set up a `VirtualHost` using the url `http://cib.loc/`. Of course you can use your own domain as well.

```python
SECRET_KEY = "Don't dare to think using this as your random string"
...
SERVE_STATIC = True
... 
# This tutorial will use cib.loc as BASE_URL 
BASE_URL = 'http://cib.loc/'
...
PROJECT_URL = BASE_URL
```
1. Add the parent directory of your deployed Custom Installer Builder and the Repy runtime directory to your `PYTHONPATH` and make sure `DJANGO_SETTINGS_MODULE` points to your local settings file.

```sh
$ export PYTHONPATH=$PYTHONPATH:/home/cib:/home/cib/repy_runtime
$ export DJANGO_SETTINGS_MODULE='custominstallerbuilder.local.settings'
```
1. *For testing purposes*, start the Django development webserver. This lets you check that your configs etc. have no syntax errors, and the Django app can be started. 

```sh
$ # Still in ~/custominstallerbuilder
$ python manage.py runserver
```
  You should now be able to access your Custom Installer Builder test server at http://127.0.0.1:8000. If you have specified anything else than `http://127.0.0.1:8000` as `BASE_URL` above, you are not going to see any media files (images, CSS, JavaScript). But don't worry, setting up apache will fix this. Also, your Custom Installer Builder isn't very useful at this moment anyways, because you don't have the necessary base installers yet.
1. Before we build the base installers. Create the directories where they will be placed into. The directories need to be accessible by your django app, e.g.:

```sh
$ mkdir -p ~/custominstallerbuilder/html/static/installers/base/
$ mkdir ~/custominstallerbuilder/html/static/installers/old_base_installers/
```

## Building base installers

The Custom Installer Builder needs *base installers* so that it can construct
customized Seattle installers from them. In this section, we first create the
cryptographic key pair that the `softwareupdater` component will use, then
clone the required code to package installers, adapt them to the local CIB,
and then build base installers.


### Generate softwareupdater key pair
You need to generate a key pair, which will be used by both the installer-packaging
scripts and the custom installer builder. This key pair is used to sign every packaged
file. The public key is included in every installer so that a Seattle install can
check for and validate software updates.

Here's how to generate a key pair in the correct format. Change to the `repy_runtime`
directory previously generated, and run the `generatekeys.py` script:
```sh
cd ~/repy_runtime
python generatekeys.py ~/cib 4096
```

This generates a key pair consisting of files `cib.publickey` and `cib.privatekey`
in `cib`'s home directory. 4096 is the minimum recommendable length at the time of writing. 


### Clone the installer packaging repo

Use `installer-packaging` to create the base installers for all platforms. Clone the
repository into your `cib`'s home directory and run the initialization and build scripts:
```sh
$ cd ~
$ git clone https://github.com/SeattleTestbed/installer-packaging
$ cd installer-packaging/scripts
$ python initialize.py
$ python build.py
```

The script that actually creates the base installer tarballs is in `~/installer-packaging/RUNNABLE/rebuild_base_installers.py`. You have to modify some variables before you can run it:

```python
# In ~/installer-packaging/RUNNABLE/rebuild_base_installers.py
software_update_url = 'http://seattle.cs.washington.edu/couvb/updatesite/0.1/'
public_key_file = '~/cib.publickey'
private_key_file = '~/cib.privatekey'

base_installer_directory = '/home/cib/custominstallerbuilder/html/static/installers/base/'
base_installer_archive_dir = '/home/cib/custominstallerbuilder/html/static/installers/old_base_installers/'

user = 'cib'
```

### Set nodemanager version
Edit `~/installer-packaging/RUNNABLE/seattle_repy/nmmain.py` on the line starting with `version = `.

Change the version string to reflect your project/Clearinghouse/Custom Installer Builder name, and also the current build. You will later need this string when launching the build script.

**NOTE: This string will be used as a part of the base installer's file name. Use only printable, non-whitespace, ASCII characters that do not require escaping!** Avoid tabs and spaces, forward and backslashes (`/
`), quotes/ticks of all kinds (`'"`), shell glob characters (`?`, `*`), and other characters with special meanings to the shell (`#&><|()[]{}!$;~` etc.).

A-Z, a-z, 0-9, `.` (period), `-` (dash), `_` (underscore) a re fine.

### Check softwareupdater URL and key pair
In order for your installers to be able to validate updates that you push, the `softwareupdater` component must include your (or your update site's) public key.

Edit `~/installer-packaging/RUNNABLE/seattle_repy/softwareupdater.py`. On the line starting with `softwareupdatepublickey = `, replace the value under the key `'e'` of the dict with the first `int` of your public key, and the value of key `'n'` with the second.

Furthermore, change the line starting with `softwareurl = ` to contain your softwareupdater's URL.
```python
softwareurl = 'http://seattle.cs.washington.edu/couvb/updatesite/0.1/'
```
Done? Great, because that's all of the customization required! Let's build installers now!

```sh
$ cd ~/installer-packaging/RUNNABLE/
$ # VERSION STRING needs to match the one in ~/installer-packaging/RUNNABLE/seattle_repy/nmmain.py
$ python rebuild_base_installers.py <VERSION STRING>
```

**Note:** It is a good idea to make `root` the owner and group-owner of your keys, and move them into the `root` account's home dir, `/root`. You might want to use a user who is in the `sudoers` file for this.

```sh
sudo mv /home/cib/cib.* /root
sudo chown root:root /root/cib.publickey /root/cib.privatekey
sudo chmod 400 /root/cib.publickey /root/cib.privatekey
```

## Configure Apache

**Note:** some of the below steps require `sudo`, so you might want to use a user who is in the `sudoers` file.

### Create a self-signed server certificate.
**Note: If you want to serve custom installers to a clearinghouse while using self-signed server certificates, you are likely to face some issues. Read more on [SSL: CERTIFICATE_VERIFY_FAILED for self-signed certs in Python 2.7.9+](https://github.com/SeattleTestbed/custominstallerbuilder/issues/16)**


1. Generate a server private key:
  ```sh
  $ openssl genrsa -out cib.key 4096
  ```

1. Generate a Certificate Signing request, and sign it yourself using the server key:
  ```sh
  $ openssl req -new -key cib.key -out cib.csr
  # Follow the interactive dialog. For a testing key, you can use default values for all fields.

  $ openssl x509 -req -in cib.csr -signkey cib.key -out cib.crt
  ```

1. Move the certificate and key file into a directory where Apache can find them. We suggest to use `/etc/apache2/ssl`. **Warning:** The key does not have a passphrase! If this is a production key, make sure it's not readable by any user but `root`.
  ```sh
  $ sudo mv /home/cib/cib.* /etc/apache2/ssl/
  $ sudo chown root /etc/apache2/ssl/cib.crt /etc/apache2/ssl/cib.csr /etc/apache2/ssl/cib.key
  $ sudo chmod 600 /etc/apache2/ssl/cib.crt /etc/apache2/ssl/cib.csr /etc/apache2/ssl/cib.key
  ```

Next up, we configure Apache.
-----

This is a minimal exemplary configuration to serve the Custom Installer Builder website from `https://cib.loc/`. Note that in this snippet, the second
VirtualHost entry assumes that you have a server certificate and key file setup, and the `Location` directive assumes that your Custom Installer Builder installation lives in `/home/cib/custominstallerbuilder` and that your Django settings module is `custominstallerbuilder.website.settings`.

Depending on you configuration of Apache, you may want to put below code in a file called `/etc/apache2/sites-available/cib.conf`.

```sh
# In /etc/apache2/sites-available/cib.conf

# HTTP
<VirtualHost *:80>
    ServerName cib.loc
    Redirect / https://cib.loc/
</VirtualHost>

# SSL
<VirtualHost *:443>
    ServerAdmin webmaster@localhost
    ServerName cib.loc

    # Enable SSL
    SSLEngine on
    SSLCertificateFile /etc/apache2/ssl/cib.crt
    SSLCertificateKeyFile /etc/apache2/ssl/cib.key
    # You can add intermediate certificates here.
    #SSLCertificateChainFile ...

    # Allow access to JavaScript/CSS/images not served by Django
    Alias /static/ /home/cib/custominstallerbuilder/html/static/
    <Directory /home/cib/custominstallerbuilder/html/static>
        Require all granted
    </Directory>

    # Run the Django app as the custom installer builder user
    # Use python-path option of the `WSGIDaemonProcess` directiv to tell
    # WSGI where your virtualenv is at
    WSGIDaemonProcess cibdjango user=cib processes=5 threads=10 python-path=/home/cib/custominstallerbuilder:/home/cib/.virtualenvs/cib/lib/python2.7/site-packages
    WSGIProcessGroup cibdjango

    # Point the root URL of this server to the appropriate Django app
    WSGIScriptAlias / /home/cib/custominstallerbuilder/wsgi/wsgi.py

    <Directory /home/cib/custominstallerbuilder/wsgi>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

</VirtualHost>
```


Enable your configuration:
```sh
$ sudo a2ensite cib.conf
```

You maybe want to add `ServerName` to your `/etc/hosts` file:
```sh
# In /etc/hosts add the following line
127.0.0.1       cib.loc
```

Be sure to restart Apache after you are done changing the configuration files.

```sh
$ sudo service apache2 restart
```

## Other configurations
The Custom Installer Builder is a normal Django project. General instructions for [Deploying Django](http://docs.djangoproject.com/en/dev/howto/deployment/) can be found on the Django project website. Make sure that the path to the Repy runtime is within your Python path, regardless of your deployment method.

# Updating the base installers
New base installers should be placed into the `~/custominstallerbuilder/html/static/installers/base` directory. To force pre-built installers to be rebuilt upon next request, execute this command:

```sh
$ python ~/custominstallerbuilder/manage.py cleaninstallers
```

# Done!

This concludes the setup and configuration of your Custom Installer Builder instance. Enjoy!

------

## Testing Your Custom Installer Builder: Integration Tests
The `custominstallerbuilder/tests` directory contains a few integration tests for various aspects of the Custom Installer Builder. These include a stress test, and tests with valid and invalid build specifications. Follow the instructions in the test case scripts to set up and configure a test environment.
