# Running a GeoIP Server

In order to allow geolocation lookups using the `geoip_client.repy` library, we have provided a GeoIP XML-RPC server for remote procedure call. While an instance of the server is running persistently at !http://geoipserver.poly.edu:12679 and !http://geoipserver2.poly.edu:12679, the server program is available at `geoip_server/geoip_server.py`.

## Usage
```
$ python geoip_server.py /path/to/GeoIP.dat PORT
```

`geoip_server.py` requires the Python library [pygeoip](https://pypi.python.org/pypi/pygeoip/) and a valid MaxMind geolocation database, such as [GeoLite City](http://www.maxmind.com/app/geolitecity). The command-line arguments to geoip_server.py are the path to the GeoIP.dat file and the port on which to host the server.

## To Start the server
Log in to the appropriate GeoIP server machine and make sure you have the latest version of the pygeoip module installed. If not, install it
```
$ sudo pip install pygeoip
```
Now, run the program from the geoipserver account as follows:
```
$ screen -S geoipserver -d -m sh /home/geoipserver/start_geoip_service.sh
```

Once the server is up and running, you can connect to it using the `geoip_client.repy` function `geoip_init_client()`, passing in the address (!http://HOSTNAME:PORT) of the server.

## Documentation
Please refer to [browser:seattle/trunk/geoip_server/geoip_server.py the file itself] for further information.