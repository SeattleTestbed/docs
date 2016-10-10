# Renewing SSL Certificates



## Introduction
This page describes some of the steps that need to be taken in order to renew the SSL certificates for the various machines and servers that we have running for the Seattle projects. We have acquired our certificates for our server from [GoDaddy.com](http://www.godaddy.com/). We have two main servers running for the Seattle project and they will need to be renewed when their expiration date approaches:
 * [Seattle](http://seattle.poly.edu)
 * [Seattle Clearinghouse](http://seattleclearinghouse.poly.edu)

In order to check the current expiration date of the server, go to the site and click on the SSL verified blob right next to the address bar (might be green or blue color). Once you click on it a little dialog should pop up. Click on 'More Information' and another menu should pop up. Under the 'Security' section, click on 'View Certificate' and it should show you the SSL certificate with the expiration date.

## Renewing SSL Certificate
If you do not have access to the GoDaddy account then inform someone who does. If you can log into the account then follow this [Renewal Link](http://help.godaddy.com/article/864) and follow the direction.




## Installing the renwed SSL Certificate
Once you have requested for the renewal of the SSL certificate and it has been approved, then you need to download the new certificates and install them. You can follow the instructions on the [Download Link](http://help.godaddy.com/article/4754) on how to download the certificates. This will download a zip file with two files: the certificate for the server and an intermediate certificate. Both of this are necessary.

You can follow the instructions on [Installation Page](http://help.godaddy.com/topic/752/article/5347) on how to install the new certificates. You should copy over both the server certificate and the intermediate certificate to the /etc/apache2/ssl directory. **Before you copy over the files, make sure to backup the old certificates.** You shouldn't need to modify the conf file if you renamed the certificates to the old certificate name, as it should be already configured properly. If you do need to modify it then the file resides in /etc/apache2/sites-available/default. 

You should then gracefully restart the apache server by running the command:
```
/usr/sbin/apache2ctl graceful
```