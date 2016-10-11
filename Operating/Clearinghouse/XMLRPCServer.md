# Production Seattle Clearinghouse XMLRPC Service

The Seattle Clearinghouse XMLRPC service is available at https://seattleclearinghouse.poly.edu/xmlrpc

## Setup Notes

The plain-http server runs locally on port 9001.

It is made available through the secure url with the addition of the following to SSL VirtualHost in /etc/apache2/mods-enabled/000-default

```
    <Location /xmlrpc>
      RewriteEngine on
      RewriteRule .* http://localhost:9001/ [P,L]
    </Location>
```

Note that for the proxy to work, the apache modules ```proxy``` and ```proxy_http``` had to be enabled, which on this debian-based system was done like this:

```
sudo a2enmod proxy
sudo a2enmod proxy_http
```
