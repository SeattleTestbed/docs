## Running the Server

To run the V2 server, please use the file advertise_v2.repy located here:

[https://seattle.poly.edu/browser/seattle/branches/repy_v2/seattlelib/advertiseserver_v2.repy] (Download link at bottom of page)

Using the following line from the terminal:

```
python repy.py restrictions.advertiseserver dylink.repy advertise_v2.repy -v
```

Note that you will need to copy the appropriate dependencies from the repy_v2 repository, located here: [https://seattle.poly.edu/browser/seattle/branches/repy_v2]. The seattlelib and repy directories contain the dependencies you will need. This can take up to a minute to execute because dylink.repy is slow.

Additionally, there is an incompatibility with emulfile.repy. It's no big deal, but on line 47 you must change

```
ALLOWED_FILENAME_CHAR_SET = set('abcdefghijklmnopqrstuvwxyz0123456789._-')
```
to read:
```
ALLOWED_FILENAME_CHAR_SET = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-')
```

Alternatively you can make sure none of the server dependencies have capital letters in their names. (Not recommended. This causes imports to fail all over the place.)



## Running the test routine

advertise_test_routine.repy is actually a repy v1 test file that works with the v2 server, because from a client perspective the two servers operate in the same way. It is located in the trunk's seattlelib file, here:

[https://seattle.poly.edu/browser/seattle/trunk/seattlelib/advertise_test_routine.repy]

As with the server, you will need to load dependencies for this, which can be found in the trunk's seattlelib and repy folders.

Before running the software, you will want to make sure the following values have been changed appropriately:

```
if callfunc == 'initialize':
363	  print "Initializing."
364	
365	  servername = '128.208.4.96'
366	  serverport = 10102
367	
368	  # Based on data taken during the week of 8/21/11, 850 entries is a
369	  # reasonable average of server database popualtion.
370	  # test_sequential(850)
371	
372	  test_count = 20
373	  thread_count = 6
374	  test_type = 'PUT'
375	
376	  test_simul(test_count, thread_count, test_type)
```

servername: The IP or hostname of the server you've hosted the v2 server on.

serverport: The port on which the v2 server is listening on.

test_count: The number of times to test the server.

thread_count: The number of queries to send simultaneously per test.

test_type: This can have values of either 'PUT', 'GET', or '*', which uses both PUT and GET queries. This selects the sort of queries that will be sent to the advertise server.  For testing the v2 server, 'PUT' is ideal. However, either can be used*. 





















* '*' has a lower tolerance than 'PUT' or 'GET' for some reason. When sending queries of mixed types, this program develops threading issues even at simultaneous query counts as low as six. This is because the GET queries tend to take longer than 300ms when the server is overloaded. If you stick to 'PUT' queries in your volume testing, this application should remain reliable up to sixteen simultaneous queries.
