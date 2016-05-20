# Seattle Clearinghouse Installation How-To

This document explains how to do a fresh install of the Seattle Clearinghouse portal on
a machine that is running a Debian-like Linux operating system such as Ubuntu.

You might want to take a look at the [Seattle Infrastructure Architecture](https://seattle.poly.edu/wiki/UnderstandingSeattle/SeattleInfrastructureArchitecture) documentation before proceeding. This also mentions the other two infrastructure components of Seattle Testbed, the Custom Installer Builder and the software update server, and talk about their interfacing with the Clearinghouse. ~~Also note there are different [deployment paths](https://seattle.poly.edu/wiki/UnderstandingSeattle/SeattleInfrastructureArchitecture#DeploymentPaths) to the functionality you want.~~

## Setting up a non-privileged user account
First of all, on the server or VM you will be using for the clearinghouse, we recommend to set up a user account specific to the Clearinghouse instance you are going to set up. This ensures all of the code, config files, etc. remain isolated from that of other services on the same machine.

The user *should not be granted interactive login* for security reasons. Use `sudo -i -u theusername` instead to work in their directory. Needless to say, the user *should not have root privileges* or be able to acquire them.

Any user name will be fine. We'll use `ch` in the instructions:

```sh
$ sudo adduser ch
```


## Install Dependencies

Clearinghouse requires at least the following software to be installed:
 * [Python](http://www.python.org/) in version 2.6, or 2.7 -- the language Seattle Clearinghouse is written in
 * [Pip](https://pypi.python.org/pypi/pip) -- Recommended tool for installing python packages.
 * [mysqlclient](https://pypi.python.org/pypi/mysqlclient) -- the python mysql interface
 * [MySQL](http://www.mysql.com/) -- the database
 * [Apache 2.4](http://www.apache.org/) -- the web server
 * [mod_wsgi](http://www.modwsgi.org/) -- necessary for interfacing with Django code
 * [OpenSSL](http://www.openssl.org/) -- necessary for `https://` support
 * [Django](http://www.djangoproject.com/) in version 1.6.x -- necessary to run Django code
 * [Django Social Auth](https://github.com/omab/django-social-auth) -- for OpenID and Oauth support.


Most of these can be installed through a package manager. For example, on a Debian-based system:

```sh
$ sudo apt-get install python-pip
$ sudo apt-get install python-dev
$ sudo apt-get install apache2 libapache2-mod-wsgi
$ sudo apt-get install mysql-server mysql-client
$ # MySQL will prompt you to set a root database password, which you should do.
$ sudo apt-get install ntp
$ sudo apt-get install openssl
```

### Setup python virtualenvironment
A convenient way to isolate your Python installations from each other is to use `virtualenv`, e.g. if you have specific version requirements for one project, but don't want to apply them system-wide or for other projects. [Virtualenv](https://virtualenv.pypa.io/en/latest/index.html) creates a separate environment that has its own installation directory and that doesn’t share libraries with other virtualenv environments. The [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) makes usage of virtualenv even easier. With the following instructions you can install and setup virtualenv and virtualenvwrapper and create a virtualenv called `ch` which can be used to install your Seattle Clearinghouse django installation.

```sh
$ # Install virtualenv and virtualenvwrapper
$ sudo pip install virtualenv
$ sudo pip install virtualenvwrapper

$ # Login as user above created
$ sudo -i -u ch

$ # Create a directory in your home folder where all your virtualenvs will live
$ mkdir ~/.virtualenvs
$ # Make the virtualenvwrapper available
$ echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
$ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
$ source ~/.bashrc

$ # Create a new virtualenv called `ch` and immediately switch to it.
$ mkvirtualenv ch
```


In the future you just have to issue the shell command `workon ch` to switch to the environment or `deactivate` if you want to leave it. You know that you are *in* the virtualenv when your shell prompt is prefixed by `(ch)`. **Note: This prefix is omitted in the shell snippets in the remainder of the document.**

### Install Django
Django, the web framework the clearinghouse uses, is available at https://www.djangoproject.com/download/ or through a package manager. Please note that [SeattleTestbed/clearinghouse:master](https://github.com/seattletestbed/clearinghouse/tree/master) currently supports the 1.6 versions of Django only.
```sh
$ pip install django==1.6
```
Depending on your actual OS and setup, this command might require `sudo` privileges.

DJANGO 1.8 EXPERIMENTAL - If and only if you are using the experimental branch supporting Django 1.8, execute this instead:
```sh
$ pip install django==1.8.3
```

### Install Mysqlclient
[Mysqlclient](https://pypi.python.org/pypi/mysqlclient) is the [recommended](https://docs.djangoproject.com/en/1.9/ref/databases/#mysql-db-api-drivers) choice for using MySQL with Django.

```sh
$ pip install mysqlclient
```

### Install Django Social Auth
Note that even if you don't enable OpenID and OAuth, Clearinghouse requires this specific Django package installed:

```sh
$ pip install django-social-auth
```

## Setup OpenID and OAuth (optional)
If you would like your Clearinghouse to support login not only through user accounts it manages itself, but ID/authentication services like OpenID and OAuth, or web services like Google, Facebook, or GitHub, take a look at the [social auth support instructions page](https://seattle.poly.edu/wiki/ClearinghouseSocialAuth).

## Create MySQL databases

You need two mysql databases and seperate users with access to each.
  * First database name: `clearinghouse`
  * Second database name: `keydb`

For simplicity, make the database usernames correspond to the database names.

Here's an example of creating a database and a user:

```sh
$ mysql -u root -p
$ # This requires entering the database root password set during install!
```
```sql
mysql> create database clearinghouse;

mysql> GRANT ALL PRIVILEGES 
ON clearinghouse.* 
TO 'clearinghouse'@'localhost'
IDENTIFIED BY 'desired password for clearinghouse';

mysql> create database keydb;

mysql> GRANT ALL PRIVILEGES 
ON keydb.* 
TO 'keydb'@'localhost'
IDENTIFIED BY 'desired password for keydb';

mysql> \q
```
where you would replace the password strings with suitable ones.

## Deploying and running Clearinghouse
In this section, we will deploy and run a copy of the Clearinghouse from your current user account in a temporary directory. This is mainly useful for testing. For an actual deployment, we recommend setting up a separate user account, and following the steps below as this user.

<!-- * **Initial preparation** -->
1. Make sure you are logged in with your clearinghouse account: `sudo -i -u ch`
1. Clone the Clearinghouse repository into `ch`'s home directory, and let the initialize script fetch dependencies:

    ```sh
    $ cd ~
    $ git clone https://github.com/SeattleTestbed/clearinghouse.git
    $ cd clearinghouse/scripts
    $ python initialize.py
    ```
1. Deploy all necessary files to a directory of your choice. We'll use `~/deployment` (a directory called `deployment` under the clearinghouse user's account) in these instructions. You'll need to give two arguments to the deployment script: The parent directory of the `clearinghouse` repo you checked out, and a directory you want to deploy to.

    ```sh
    $ python ~/clearinghouse/deploymentscripts/deploy_clearinghouse.py ~ ~/deployment
    ```
1. Deploy the Repy runtime. Create a `seattle` directory within `deployment`, and run the build script.

    ```sh
    $ mkdir ~/deployment/seattle
    $ cd ~/clearinghouse/scripts
    $ python build.py ~/deployment/seattle
    ```
1. The Seattle [backend scripts](https://seattle.poly.edu/wiki/SeattleBackend) require a set of public keys (called ''state keys'') to work. From the `seattle` runtime directory, make key generate script executable and run it:

    ```sh
    $ cd ~/deployment/seattle
    $ chmod +x generate_state_keys.sh
    # Work around https://github.com/SeattleTestbed/clearinghouse/issues/149
    $ mkdir ../clearinghouse/node_state_transitions/statekeys   
    $ ./generate_state_keys.sh ../clearinghouse/node_state_transitions/statekeys
    ```
    * Note that only the `*.publickey` files are required for the clearinghouse. You can safely remove the `*.privatekey`s from `~/deployment/clearinghouse/node_state_transitions/statekeys`.
1. If it does not already exist, create a logs directory for the clearinghouse component to write to:

    ```sh
    $ cd ~/deployment/clearinghouse
    $ mkdir logs
    ```
1. Edit the django settings file in `~/deployment/clearinghouse/website/settings.py`
  * Add clearinghouse database name and credentials in the `DATABASES` dict (Be sure you've already created a MySQL database for the clearinghouse, e.g. `clearinghouse`)

  ```python
  # Database
  # https://docs.djangoproject.com/en/1.6/ref/settings/#databases
  DATABASES = {
      'default': {
          # you can use django.db.backends.sqlite3 instead of mysql. If you
          # decide to do so, you can leave the other fields empty
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'clearinghouse',
          'USER': 'clearinghouse',
          'PASSWORD': '<db user password>',
          'HOST': '',
          'PORT': '',
      }
  }
  ```
  * Set `SECRET_KEY` to a long, random string.
  * If this is a production launch, also set `DEBUG` to False, and uncomment and change the fields for sending `ADMINS` email.
  * If your clearinghouse is supposed to provide installers other than the stock Seattle ones, you need to [set up a Custom Installer Builder](https://seattle.poly.edu/wiki/CustomInstallerBuilderInstallation) and point `SEATTLECLEARINGHOUSE_INSTALLER_BUILDER_XMLRPC` to that URL. Currently, there are two existing Custom Installer Builders you can choose from:
    * Default CIB, currently providing no repy_v2 compatibility (only repy_v1). This means that, among other things, the seattle installation will not provide NAT traversal, and so you may run into issues if you're testing things on a machine that's behind a router (say).

        ```python
        SEATTLECLEARINGHOUSE_INSTALLER_BUILDER_XMLRPC = "https://custombuilder.poly.edu/custom_install/xmlrpc/
        ```
    * The current SensibilityTestbed CIB, which does provide repy_v2 compatibility.

        ```python
        SEATTLECLEARINGHOUSE_INSTALLER_BUILDER_XMLRPC = "https://sensibilityclearinghouse.poly.edu/custominstallerbuilder/xmlrpc/"
        ```
  * You can also adapt the clearinghouse `TIME_ZONE`
1. Add `clearinghouse` and `seattle` to the `PYTHONPATH` to ensure that the django app and the Repy runtime work. Also create an environment variable pointing at the django setting file, which will be needed in the WSGI script:

  ```sh
  $ echo "export PYTHONPATH=$PYTHONPATH:/home/ch/deployment:/home/ch/deployment/seattle" >> ~/.bashrc
  $ echo "export DJANGO_SETTINGS_MODULE='clearinghouse.website.settings'" >> ~/.bashrc
  $ source ~/.bashrc
  $ # Sourcing .bashrc kicks you out of your virtualenv, so you have to re-actiavte
  $ workon ch
  ```
1. Create the database structure. You may want to create a Django administrator account when asked (but you don't have to). Note that this user will be able to log in over the web using the Django `admin` page. Use a *strong password*, and update it frequently! (The password can be changed on the command line using `manage.py changepassword` followed by the user account name). You may get an `OperationalError` from django about being unable to create a table and may need to run this command twice.

  ```sh
  $ cd ~/deployment/clearinghouse
  $ python website/manage.py syncdb
  ```
  * (Please note that Django 1.7+ has migrated to a migration-based model from start to finish, and that syncdb is deprecated entirely and will be removed in Django 1.9. For Django 1.7 and 1.8, syncdb for initial setup may still work, but should really be replaced by the following. You may need to run migrate twice if an error occurs the first time.

  ```sh
  cd ~/deployment/clearinghouse
  python website/manage.py makemigrations
  python website/manage.py migrate
  ```
1. *For testing purposes*, start the Django development webserver. This lets you check that your configs etc. have no syntax errors, and the Django app can be started. **Note: To be able to further interact with the Clearinghouse (e.g. create user accounts and log in), you must set up Apache web server.**

  ```sh
  $ # Use this for running on localhost only:
  $ python website/manage.py runserver 8000

  $ # Use this for listening on every interface:
  $ python website/manage.py runserver 0.0.0.0:8000
  ```
  You will now have a local development server running on port 8000, `http://localhost:8000/html/login`. This is convenient for development and testing your Clearinghouse instance (but should not be used in production.)

  *Hint: In case you don't have a browser on your server, but have `ssh` access, you can use port forwarding to make the development server available for testing on your local machine: `ssh -L SOME_LOCAL_PORT:127.0.0.1:8000 YOUR_CLEARINGHOUSE_SERVER`. Then, open `http://localhost:SOME_LOCAL_PORT/html/login` in your local browser and interact with your install.*

1. *For production purpose*, run the site through an Apache web server. Instructions are available below. Before the clearinghouse is ready for production use, we will set up the backend database and scripts.

  * Make sure have a MySQL database to use for the key database. We suggested above to call it `keydb`.
  * Edit the file `~/deployment/clearinghouse/keydb/config.py` and set the database information for the key database, e.g.:

    ```python
    # Fill these in with the information needed to use the key database.
    dbuser = "keydb"
    dbpass = "desired password for keydb"
    dbname = "keydb"
    dbhost = "localhost"
    ```
  * Create the key database structure by executing the contents of the file `keydb/schema.sql` on the new key database you created. If set up as suggested with both the user and databse names `keydb`:

    ```sh  
    $ mysql -ukeydb -p --database=keydb < ~/deployment/clearinghouse/keydb/schema.sql
    # This will prompt for the keydb database password!
    ```
  * Edit the file `~/deployment/clearinghouse/backend/config.py` and set a value for `authcode`.
  * Make sure that the files `keydb/config.py` and `backend/config.py` are not readable by the user the web server will be running as, i.e. they are only user-readable (but neither group- nor world-readable), owned by the clearinghouse user, and the web server is not in the user group the file belongs to.
  * The backend scripts can be started with a script `start_clearinghouse_components.sh`. Before we can do that, Apache needs to be set up.


## Configure Apache

To provide encryption and keep passwords etc. safe in transit between a user's web browser and the Clearinghouse, it relies on SSL. Therefore you will need to set up one `VirtualHost` entry for connections to port 443 (SSL) at the minimum.

For a production launch, follow the instructions at [this page](http://slacksite.com/apache/certificate.php) to understand Certificate Signing Requests and dealing with Certificate Authorities in greater detail. For testing purposes, you will want to generate a temporary self-signed certificate. Here's how (we'll assume `openssl` is available on your clearinghouse machine).
**Note:** some of the below steps require `sudo`, so you might want to use a user who is in the `sudoers` file.

1. Generate a server private key:
  ```sh
  $ openssl genrsa -out ch.key 4096
  ```

1. Generate a Certificate Signing request, and sign it yourself using the server key:
  ```sh
  $ openssl req -new -key ch.key -out ch.csr
  # Follow the interactive dialog. For a testing key, you can use default values for all fields.

  $ openssl x509 -req -in ch.csr -signkey ch.key -out ch.crt
  ```

1. Move the certificate and key file into a directory where Apache can find them. We suggest to use `/etc/apache2/ssl`. **Warning:** The key does not have a passphrase! If this is a production key, make sure it's not readable by any user but `root`.
  ```sh
  $ sudo mv /home/ch/ch.* /etc/apache2/ssl/
  $ sudo chown root /etc/apache2/ssl/ch.crt /etc/apache2/ssl/ch.csr /etc/apache2/ssl/ch.key
  $ sudo chmod 600 /etc/apache2/ssl/ch.crt /etc/apache2/ssl/ch.csr /etc/apache2/ssl/ch.key
  ```

Next up, we configure Apache.
-----

This is a minimal exemplary configuration to serve the Clearinghouse website from `https://ch.loc/`. Note that in this snippet, the second
VirtualHost entry assumes that you have a server certificate and key file setup, and the `Location` directive assumes that your Clearinghouse
installation lives in `/home/ch/deployment/clearinghouse` and that your Django settings module is `clearinghouse.website.settings`.

Depending on you configuration of Apache, you may want to put below code in a file called `/etc/apache2/sites-available/ch.conf`.

```sh
# In /etc/apache2/sites-available/ch.conf
# Run the Django app as the clearinghouse user
# Use python-path option of the `WSGIDaemonProcess` directiv to tell
# WSGI where your virtualenv is at

WSGIDaemonProcess chdjango user=ch processes=5 threads=10 python-path=/home/ch/deployment/clearinghouse:/home/ch/.virtualenvs/ch/lib/python2.7/site-packages
WSGIProcessGroup chdjango

# HTTP
<VirtualHost *:80>
    ServerName ch.loc
    Redirect / https://ch.loc/
</VirtualHost>


# SSL
<VirtualHost *:443>
    ServerAdmin webmaster@localhost

    # Enable SSL
    SSLEngine on
    SSLCertificateFile /etc/apache2/ssl/ch.crt
    SSLCertificateKeyFile /etc/apache2/ssl/ch.key
    # You can add intermediate certificates here.

    # Point Apache to the clearinghouse's static image:wqZZs/CSS/JavaScript
    Alias /site_media /home/ch/deployment/clearinghouse/website/html/media
    <Directory /home/ch/deployment/clearinghouse/website/html/media>
        Require all granted
    </Directory>

    # XXX We should configure the Django admin page static files too!
    # XXX See https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/modwsgi/

    # Point the URL https://ch.loc/ to the Django app
    WSGIScriptAlias / /home/ch/deployment/clearinghouse/wsgi/wsgi.py

    <Directory /home/ch/deployment/clearinghouse/wsgi>
        <Files wsgi.py>
        Require all granted
        </Files>
    </Directory>

</VirtualHost>
```


Enable your clearinghouse configuration:
```sh
$ sudo a2ensite ch.conf
```

You maybe want to add `ServerName` to your `/etc/hosts` file:
```sh
# In /etc/hosts add the following line
127.0.0.1       ch.loc
```

To use this configuration for your Seattle Clearinghouse installation, change
* `ch.loc` to your domain name (or IP address in case you performing tests),
* `/home/ch/deployment/` in the site media location, and
* `WSGIScriptAlias` directive to the directory where you deployed Seattle Clearinghouse;
*  also, make sure `"/admin_media"` is aliased to a valid directory, as the exact location will vary depending on the version of Python installed and how you installed Django.


To configure SSL you will probably need to install openssl to generate a private key/CSR
(Certificate Signing Request), and then possibly purchase a certificate for your site.
For more information see [this page](http://slacksite.com/apache/certificate.php). Put your
SSL key and certificate in a directory named `/etc/apache2/ssl` (or change the configuration
to correctly reference them). If you generate your own certificate instead of buying one,
remove the line for `"SSLCertificateChainFile"`.

Be sure to restart Apache after you are done changing the configuration files.

```sh
$ sudo service apache2 restart
```
If Apache gives the error:
```
Invalid command 'SSLEngine', perhaps misspelled or defined by a module not included in the server configuration
```

then you need to enable SSL by running:
```sh
$ sudo a2enmod ssl
```

If you try to access your Seattle Clearinghouse installation's website now, then creating user accounts, logging in etc. will not function correctly. These tasks require a few management scripts to run in the background. We will start them in the next section.


## Running start_clearinghouse_components.sh

The Seattle Clearinghouse includes a scripts that automatically search for, contact, and set up newly installed Seattle nodes. The relevant backend architecture is described [here](https://seattle.poly.edu/wiki/SeattleBackend). If you have all the components of Seattle Clearinghouse (including Apache) configured, the script `/home/ch/deployment/clearinghouse/deploymentscripts/start_clearinghouse_components.sh` will start up all the individual
components in the correct order, and also start Apache.

**Note to developers: If you are modfifying the Clearinghouse code, you might want to start its individual components manually. See the [ Deleopers' Notes](https://seattle.poly.edu/wiki/ClearinghouseDevelopersNotes) for details.**

Before running the script, make sure to edit the start script and change `CLEARINGHOUSE_USER`, `CLEARINGHOUSE_DIR`, `PYTHONPATH`,
and `LOG_DIR` to the correct locations for your deployment. Also, create `LOG_DIR` if it doesn't already exist.

```sh
# In /home/ch/deployment/clearinghouse/deploymentscripts/start_clearinghouse_components.sh
CLEARINGHOUSE_USER=ch
...
CLEARINGHOUSE_DIR="/home/ch/deployment/clearinghouse"
...
export PYTHONPATH="$CLEARINGHOUSE_DIR/..:$REPY_RUNTIME_DIR:/home/ch/.virtualenvs/ch/lib/python2.7/site-packages"
...
export DJANGO_SETTINGS_MODULE="clearinghouse.website.settings"
...
```

If one or more of the backend scripts (called `transition_STATEX_to_STATEY.py` for different state names) are already running, kill them before running `start_clearinghouse_components.sh`. 

To run the script, run the following commands with the correct directory substituted for your deployment directory. This will start the script in a new `screen` session running as root.
```sh
$ sudo -i
$ screen
$ cd /home/ch/deployment/clearinghouse/deploymentscripts
$ ./start_clearinghouse_components.sh
```

Hit CTRL-A followed by D to detach the screen session.

To later reattach to the session in order to stop or restart `start_clearinghouse_components.sh`:
```sh
$ sudo -i
$ screen -r
```

## Done! (Almost)

Congratulations! You should now have a fully operational Seattle Clearinghouse
installation that you can access at https://ch.loc

## Monitoring

## Log rotation
