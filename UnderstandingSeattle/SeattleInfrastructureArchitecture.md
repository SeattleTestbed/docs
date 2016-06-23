# Seattle Infrastructure Architecture
## Overview

This page explains the architecture of the three central _infrastructure_ components for the testbed --- the [Seattle Clearinghouse](https://seattleclearinghouse.poly.edu/html/accounts_help#introduction), the [Custom Installer Builder](https://custombuilder.poly.edu/custom_install/), and the [Software Updater](https://github.com/SeattleTestbed/docs/blob/15f11aa86f3b446844e884c2c6f21ea529cacdb2/Operating/SoftwareUpdaterSetup.wiki). For a discussion of the perspective of people participating in the Seattle Testbed by means of donating resources, planning, and running experiments, please see this [wiki page](https://github.com/SeattleTestbed/docs/blob/master/UnderstandingSeattle/SeattleComponents.wiki).


# Infrastructure Components
## Clearinghouse
The Seattle Testbed consists of a large number of Seattle VMs (virtual machines) running on computing devices provided by volunteers. These donated VMs are made available to registered users through an infrastructure component called the [Seattle Clearinghouse](https://seattleclearinghouse.poly.edu/).

In addition to handing out resources donated to the general public, the Seattle Clearinghouse can also track donations on behalf of registered users. Every donation on their behalf will grant a user a greater number of resources on other machines in return. This _tit-for-tat_ tactic both enables users to run larger experiments, and helps scale the testbed.

The Seattle Clearinghouse relies on identifying data included in each install of the Seattle Testbed software to track and credit resource donations: Depending on the user that should be credited (the general public is also treated as a user in this respect), the install announces a user-specific _public key_ on the Seattle advertise services.

## Custom Installer Builder
The [Custom Installer Builder](https://custombuilder.poly.edu/custom_install/) is the infrastructure component putting together the base Seattle installer with a user's donation-tracking public key. The Seattle installer customized such is provided to users seeking to increase their credit of VMs on the clearinghouse. (The [Seattle Components wiki page](https://github.com/SeattleTestbed/docs/blob/master/UnderstandingSeattle/SeattleComponents.wiki) shows another use case for the Custom Installer Builder).

## Software Update Site
Lastly, every Seattle install contains information which software update site (URL) to contact for downloading the latest Seattle revision when it becomes available, and also a cryptographic key that is used to check the integrity of updates.



# Technical Aspects

The infrastructure components use the following interfaces and configuration between one another:

 1. The software updater public key and URL go into `softwareupdater.py`, part of the _base installer_ packaged by the custom installer builder
 1. The clearinghouse requests packaging of an installer with particular user public keys from the custom installer builder via XML-RPC over HTTPS. The custom installer builder URL used is stored in the clearinghouse configuration.

The consequence of item 1 above is that the custom installer builder only needs to know the software updater server's URL, but is otherwise independent from it (e.g., can run on a different server).

Similarly, from item 2 above, the clearinghouse can use any custom installer builder whose URL it knows and whose base installer package suits it. For example, a Seattle-based testbed might choose to use Seattle's Custom Installer Builder to avoid setting up its own.

This architecture also makes it easy to deploy (or gradually update) new versions of infrastructure components while keeping others unchanged.




# Deployment Paths

The flexibility of where and how to deploy the different components influences the server and service configuration required for your specific deployment.


## Separate Servers
The simplest yet most expensive deployment path is to set up separate servers (or VMs) with distinct hostnames (and HTTPS certificates) for each of the three services. This is also the type of setup assumed for the sample Apache / `mod_wsgi` config files provided with the [Seattle Clearinghouse](https://github.com/SeattleTestbed/docs/blob/master/Operating/Clearinghouse/Installation.md) and [Custom Installer Builder](https://github.com/SeattleTestbed/docs/blob/master/Operating/CustomInstallerBuilder/Installation.md) deployment guides.

It does make sense to keep the contents of the base installers for custominstallerbuilder up-to-date with the what the softwareupdater ships, so combining those two services on one machine is a likely scenario. We'll see below what that means for the configuration.


## One Combined Server

It's often more efficient to run all three services on a single server. In case you still use separate hostnames for the services, this would be a matter of "merging" the three Apache configs per the above to contain each service under a separate `VirtualHost` directive. `mod_wsgi` will cleanly separate the Django instances for the clearinghouse and custominstallerbuilder apps, out of the box ([ref](http://blog.dscpl.com.au/2012/10/requests-running-in-wrong-django.html)).

If only one hostname is available for all services, then they must be demultiplexed using different `WSGIScriptAlias` directives for each sub-URL. If using different-level sub-URLs such as `hostname/` for the clearinghouse and `hostname/cib` for the custominstallerbuilder, the catch is to put the more specific URL first. Otherwise, the first (being a prefix of the other) will match, and the wrong Django app be started. Also, separate Django processes must be started for each app, so that they don't share configuration and environment variable contents. All of this is detailed in the reference above.

Here is an example of a combined clearinghouse / custominstallerbuilder `apache.conf`, with the clearinghouse app at `https://host/` and the custominstallerbuilder at `https://host/cib`.

```
    # Have separate processes for each Django app
WSGIDaemonProcess chdjango user=ch processes=5 threads=10
WSGIDaemonProcess cibdjango user=cib processes=5 threads=10

<VirtualHost *:443>
    # NOTE: Certificate etc. config omitted for brevity.

    # This configures the custominstallerbuilder Django app, 
    # assigns it to its own process group, 
    # and lets it access static content.
    WSGIScriptAlias /cib /home/cib/custominstallerbuilder/wsgi/wsgi.py process-group=cibdjango

    <Directory /home/cib/custominstallerbuilder/wsgi>
        <Files wsgi.py>
        Require all granted
        </Files>
    </Directory>

    Alias /cib/static/ /home/cib/custominstallerbuilder/html/static/
    <Directory /home/cib/custominstallerbuilder/html/static>
        Require all granted
    </Directory>


    # This configures the clearinghouse Django app.
    WSGIScriptAlias / /home/ch/deployment/clearinghouse/wsgi/wsgi.py process-group=chdjango
    <Directory /home/ch/deployment/clearinghouse/wsgi>
        <Files wsgi.py>
        Require all granted
        </Files>
    </Directory>

    # Allow access to the clearinghouse's static images/CSS/JavaScript
    Alias /site_media /home/ch/deployment/clearinghouse/website/html/media
    <Directory /home/ch/deployment/clearinghouse/website/html/media>
        Require all granted
    </Directory>
</VirtualHost>
```




## Tips and Caveats

(**Abhishek's text regarding `chmod`ding files/directories will go here.** Maybe we can figure out how to better set up paths and users so that we don't have problems with users `www-data`/`ch`/`cib` accessing different mutually disallowed parts of the filesystem.)



When running a server with Django apps mounted under sub-URLs, be sure to test those thoroughly. A recurring problem is that `https://host/suburl/` (note the trailing slash) works fine, while `https://host/suburl` results in a 404 error, or breaks the AJAX parts of a page. If running into this, first check your `settings.py` -- the `PROJECT_URL`, `BASE_URL`, etc. must match what a web browser will request from Apache.


If the missing trailing slash is the problem (which you can test using your browser!), add a redirect to the proper URL:

```
RedirectMatch ^/cib$ https://host/cib/
```

This should be done before the `WSGIScriptAlias` directive starting the Django app for `cib`.


<!--
Or maybe fix this in our own `urls.py` if that's possible, https://stackoverflow.com/questions/17156965/trailing-slash-not-added-to-root-url
-->


It's handy to redirect the `http://` version of each page to `https://`. The Django app should never listen for incoming insecure connections because sensitive data is transferred. In the Apache config snippet below, we assume that the Clearinghouse lives under the `ch` sub-URL on the server.

```
<VirtualHost *:80>
    # Redirect requests for the server index to the HTTPS site.
    RedirectMatch ^/$ https://host/ch/html/login
    # You might want to add further redirects pointing to the HTTPS login site,
    # or else the user will see a 404 error page.
    # Example: Redirect full login URL to HTTPS
    # RedirectMatch ^/ch/html/login$ https://host/ch/html/login
</VirtualHost>
```

