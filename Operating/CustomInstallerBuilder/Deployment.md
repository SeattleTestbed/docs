# Deploying the Custom Installer Builder
This page outlines how to deploy the [Custom Installer Builder](https://seattle.poly.edu/wiki/CustomInstallerBuilder) using common Apache configurations. See also our instructions on [installing](https://github.com/SeattleTestbed/docs/blob/master/Operating/CustomInstallerBuilder/Installation.md), [configuring](https://github.com/SeattleTestbed/docs/blob/master/Operating/CustomInstallerBuilder/Configuration.md), [customizing](https://github.com/SeattleTestbed/docs/blob/master/Operating/CustomInstallerBuilder/CustomizeAndBuild.md), and [testing](https://github.com/SeattleTestbed/docs/blob/master/Operating/CustomInstallerBuilder/Testing.md) your Custom Installer Builder site.

----

## Configuring Apache + mod_wsgi
As noted in the [installation instructions](https://github.com/SeattleTestbed/docs/blob/master/Operating/CustomInstallerBuilder/Installation.md), we will use Apache as the front-end web server to our Custom Installer Builder.

Insert the following text into the appropriate area of your Apache configuration file. For simple deployments, the text may be added to the end of the `httpd.conf` file. The configuration will also work within a `VirtualHost` directive, for example. (Check out [this overview of deployment paths](https://seattle.poly.edu/wiki/UnderstandingSeattle/SeattleInfrastructureArchitecture#DeploymentPaths) for alternative configs.)


As always, remember to disable debugging once you have successfully deployed the Custom Installer Builder.

```sh
# Let the custominstallerbuilder Django app run in a separate process
WSGIDaemonProcess cibdjango user=cib processes=5 threads=10
#WSGIDaemonProcess cibdjango user=cib processes=5 threads=10 python-path=/home/cib/custominstallerbuilder:/home/cib/.virtualenvs/cib/lib/python2.7/site-packages
WSGIProcessGroup chdjango

# Allow access to JavaScript/CSS/images not served by Django
Alias /static/ /home/cib/custominstallerbuilder/html/static/
<Directory /home/cib/custominstallerbuilder/html/static>
    Require all granted
</Directory>

# Point the root URL of this server to the appropriate Django app
WSGIScriptAlias / /home/cib/custominstallerbuilder/wsgi/wsgi.py process-group=cibdjango

# Allow access to the WSGI wrapper script
<Directory /home/cib/custominstallerbuilder/wsgi>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>

```
## Virtualenvironment and Python path

If you are using virtualenvironments (e.g. in a directory `~/.virtualenvs/cib`), tell WSGI where to find the libraries installed to your virtualenvironment by using the python-path option of the WSGIDaemonProcess directive (see comment below first `WSGIDaemonProcess` in snippet above).

## Other configurations
The Custom Installer Builder is a normal Django project. General instructions for [Deploying Django](http://docs.djangoproject.com/en/dev/howto/deployment/) can be found on the Django project website. Make sure that the path to the Repy runtime is within your Python path, regardless of your deployment method.

# Updating the base installers
New base installers should be placed into the `~/custominstallerbuilder/html/static/installers/base` directory. To force pre-built installers to be rebuilt upon next request, execute this command:

```sh
$ python /path/to/custominstallerbuilder/manage.py cleaninstallers
```

# Done!

This concludes the setup and configuration of your Custom Installer Builder instance. Enjoy!

------

## Testing Your Custom Installer Builder: Integration Tests
The `custominstallerbuilder/tests` directory contains a few integration tests for various aspects of the Custom Installer Builder. These include a stress test, and tests with valid and invalid build specifications. Follow the instructions in the test case scripts to set up and configure a test environment.
