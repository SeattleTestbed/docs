# Using Social Auth for Clearinghouse
In addition to its own user management, Clearinghouse can optionally handle OpenID and Oauth. This page describes how to set that up.

----

----

## Setup OpenID and OAuth
For OpenID and OAuth, Clearinghouse requires [Django Social Auth](https://github.com/omab/django-social-auth).  This application depends on:
 * [python-openid ](http://pypi.python.org/pypi/python-openid/)
 * [python-oauth2 ](https://github.com/simplegeo/python-oauth2/)

Using something like `easy_install` will install these for you.
```sh
$ easy_install django-social-auth
```
  

By default Gmail and Yahoo login are enabled.  If desired Windows Live, Github and Facebook login can be enabled with some additional steps.

 **Facebook**
  * Register a new application at [Facebook App Creation ](http://developers.facebook.com/setup/)
  * set App Domains in Facebook edit App page
``` 
yoursite.com
```
  * click the Website with Facebook Login checkmark and set site URL
```
https://yoursite.com
```
  * Uncomment and fill out ```App ID``` and ```App Secret``` values in settings.py
```python
FACEBOOK_APP_ID                   = ' your appid'
FACEBOOK_API_SECRET               = ' your api secret key'
```


 **Windows Live**
 * Register a new application at [Live Connect Developer Center ](https://manage.dev.live.com/Applications/Index)
 * Set redirect domain 
``` 
https://yoursite.com
```
 * Uncomment and fill out ```LIVE_CLIENT_ID``` and ```LIVE_CLIENT_SECRET``` values in settings.py
```python
LIVE_CLIENT_ID                  = ' your appid'
LIVE_CLIENT_SECRET              = ' your api secret key'
```



 **Github**
 * Register a new application at [Live GitHub Developers ](https://github.com/settings/applications/new)
 * Set URL and callback URL
``` 
https://yoursite.com
```
 * Uncomment and fill out ```GITHUB_APP_ID``` and ```GITHUB_API_SECRET``` values in settings.py
```python
GITHUB_APP_ID                  = ' your appid'
GITHUB_API_SECRET              = ' your api secret key'
```



## Updating an existing Clearinghouse

If you already have a working copy of the Clearinghouse and you are updating to allow OpenID and OAuth support you will need to add the Django Social Auth db tables. This is done automatically by:
```sh
$ python website/manage.py syncdb
```
