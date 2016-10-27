# Using the remote testing stack.

----

----



## Components
----

The remote testing frame work consists of the following:
 * testingserver.py: This is the server side script which allows for remote tests.
 * server.cfg: This is the configuration file for the testingserver
 * remotetest.py: Runs a remote test on 1 host, or fetches information.
 * remotetestmulti.py: Runs remote tests on multiple hosts concurrently.

These files all use the seattle repy, so they must be used in a directory which has seattle.
**E.g. do python preparetest.py foo/ then put these files in foo, and use them from there.**



## Server side: testingserver.py
----

The testing server is responsible for listening to incoming connections and running the remote tests.
It will read the configuration file to setup initial waitforconns. Then every 60 seconds, it will reload
the list of allowed username/passwords and its hostname for advertisement. It will advertise its IPs
under its host name so that remotetest.py can lookup the host.



## Server side: server.cfg
----

This file stores the configuration for the testingserver. This file should not contain blank lines, and does not support '#' for comments. It takes the following directives:

| Directive | Argument 1 | Argument 2 | Notes |
| hostname | The hostname | N/A | Only 1 hostname directive may be specified. Spaces not allowed in the hostname. This can be **omitted**. This will disable advertisement, but you can still connect using the --ip flag of remotetest.py |
| ip | The IP address | N/A |Multiple ip directives may be specified. The are only loaded initially |
| user | username | password | Multiple user directives may be specified. The are reloaded every 60 seconds. |
| disablestderr | N/A | N/A | Defers sending the stderr of the test to the client until the test terminates. This is **NECESSARY** on windows hosts if you would like any output.  |
| path | Full path to python | N/A | The rest of the line is used as the path. This is optional, and the default is just "python" |
| noshell | N/A | N/A | When launching subprocess.Popen, the shell parameter will be set to False. This is useful if you have provided the full path to python. |



## Client side: remotetest.py
----
This file allows for listing the testbeds, fetching the IP addresses each host will listen on, and launching remote tests.
To list hosts do the following:
```
python remotetest.py --list
```

The output will be like the following:
```
Available testbeds: ['freebsd', 'attu2', 'opensuse', 'EXAMPLE']
```
In this example 4 testbeds are available.

To query for IP address information, use the hostinfo directive:
```
python remotetest.py --hostinfo attu2
```

This will produce:
```
IP Addresses for: attu2 ['127.0.0.1', '128.208.1.138']
```
These are the valid IP's that attu2 will respond 2. Obviously, the first one will only be useful if you are running on attu2.

Lastly, to run a remote test, many arguments are necessary. Below is an example:
```
python remotetest.py --host attu2 --user test --pass password --dir ../test/ --args "run_tests.py"
```
It is important to note that the arguments can be given in any order, it does not matter.
Here is a sample for when arguments is just "repy.py":

```
Configuration: {'ip': None, 'args': 'repy.py', 'host': 'attu2', 'user': 'test', 'pass': 'password', 'dir': '../test/'}
Creating tar file...
Created: files.attu2.1242156611.tgz
Connecting...
Authenticating...
Uploading tar file...
Upload Status: True
Removing tar file: files.attu2.1242156611.tgz
Uploading arguments...
Setup interrupt handler on SIGINT to stop remote test.
Starting to dump result:

Error: Must supply a restrictions file and a program file to execute

Usage: repy.py [options] restrictionsfile.txt program_to_run.py [program args]

Where [options] are some combination of the following:

--simple               : Simple execution mode -- execute and exit
--ip IP                : This flag informs Repy that it is allowed to bind to the given given IP.
                       : This flag may be asserted multiple times.
                       : Repy will attempt to use IP's and interfaces in the order they are given.
--iface interface      : This flag informs Repy that it is allowed to bind to the given interface.
                       : This flag may be asserted multiple times.
--nootherips           : Instructs Repy to only use IP's and interfaces that are explicitly given.
                       : It should be noted that loopback (127.0.0.1) is always permitted.
--logfile filename.txt : Set up a circular log buffer and output to logfilename.txt
--stop filename        : Repy will watch for the creation of this file and abort when it happens
                       : File can have format EXITCODE;EXITMESG. Code 44 is Stopped and is the default.
                       : EXITMESG will be printed prior to exiting if it is non-null.
--status filename.txt  : Write status information into this file
--cwd dir              : Set Current working directory
--servicelog           : Enable usage of the servicelogger for internal errors

Done! Exiting.
```
In this simple test, all that is printed is repy's usage. You can verify this by launching python repy.py on your local machine.

Some important notes:
 * Control-C will send an interrupt to the remote host. This allows the remote host to terminate the test and flush any remaining output. On remote windows hosts, it will appear to have locked up for a bit. I don't think this works on Windows clients since they have no concept of a Signal Interrupt.
 * Arguments can be given in any order.
 * You will need a valid username and password
 * If you know your user/pass is valid but you are getting authentication failed, just wait about a minute for the testingserver to reload your user name and password.
 * You can use the --ip flag instead of --host, to force connecting to a special ip.
 * Sometimes if things fail the tgz file will not be delete for you. You should manually delete these.




## Client side: remotetestmulti.py
----

This is a simple wrapper function around remotetest.py. However, it is incredibly convenient for running concurrent tests, since it will inform you when the tests finish on each host independently so that you can check the results immediately.

Its usage is basically the same with a few minor exceptions:
 * Does not take the --list, --hostinfo, or --ip flags
 * Allows for multiple --host flags. It will run remotetest.py with the user/pass/dir/args directive for each host specified.
 * Takes a sample directive to control the sample rate of the sub-tests. This defaults to 60 seconds, but may be too long for short tests.

Output will be saved to host.result.txt. E.g. --host attu will be logged to attu.result.txt.
Here is an example:
```
python remotetestmulti.py --user test --pass password --dir . --args "repy.py" --host EXAMPLE --host freebsd --host attu2 --host opensuse --sample 10
```
The sample directive is used here to check for completion every 10 seconds. 

Sample output:
```
Storing output for EXAMPLE in EXAMPLE.result.txt
Staring test on EXAMPLE
Storing output for freebsd in freebsd.result.txt
Staring test on freebsd
Storing output for attu2 in attu2.result.txt
Staring test on attu2
Storing output for opensuse in opensuse.result.txt
Staring test on opensuse
###
Checking at: 10.0 seconds...
Host: EXAMPLE Done: True
Host: freebsd Done: True
Host: attu2 Done: True
Host: opensuse Done: True
Done running all tests!
```


Here is the output from attu2.result.txt:
```
Configuration: {'ip': None, 'args': 'repy.py', 'host': 'attu2', 'user': 'test', 'pass': 'password', 'dir': '.'}
Creating tar file...
Created: files.attu2.1242157219.tgz
Connecting...
Authenticating...
Uploading tar file...
Upload Status: True
Removing tar file: files.attu2.1242157219.tgz
Uploading arguments...
Setup interrupt handler on SIGINT to stop remote test.
Starting to dump result:

Error: Must supply a restrictions file and a program file to execute

Usage: repy.py [options] restrictionsfile.txt program_to_run.py [program args]

Where [options] are some combination of the following:

--simple               : Simple execution mode -- execute and exit
--ip IP                : This flag informs Repy that it is allowed to bind to the given given IP.
                       : This flag may be asserted multiple times.
                       : Repy will attempt to use IP's and interfaces in the order they are given.
--iface interface      : This flag informs Repy that it is allowed to bind to the given interface.
                       : This flag may be asserted multiple times.
--nootherips           : Instructs Repy to only use IP's and interfaces that are explicitly given.
                       : It should be noted that loopback (127.0.0.1) is always permitted.
--logfile filename.txt : Set up a circular log buffer and output to logfilename.txt
--stop filename        : Repy will watch for the creation of this file and abort when it happens
                       : File can have format EXITCODE;EXITMESG. Code 44 is Stopped and is the default.
                       : EXITMESG will be printed prior to exiting if it is non-null.
--status filename.txt  : Write status information into this file
--cwd dir              : Set Current working directory
--servicelog           : Enable usage of the servicelogger for internal errors

Done! Exiting.
```




## Full Example: Repy and NM unit tests
----
First it is necessary to prepare all the files. This is how I prefer to do it:
 1. cd seattle/trunk/
 2. mkdir test minimal
 3. python preparetest.py minimal
 4. python preparetest.py -t test 
 5. cp integrationtests/* minimal/

Now test has all the files needed to run the tests, and minimal contains everything we need for remote testing.
Assuming you want to run the testing server on a remote machine, you could to the following:
 1. cd minimal
 2. scp * user@machine:'~/server/'
 3. ssh user@machine
 4. machine$ cd server
 5. machine$ python testingserver.py >output.txt &
 6. machine$ exit

This will start the testing server with the default server.cfg. Of couse, you should probably edit this.

Now we are back inside minimal/ Lets say we want to run the repy unit tests, on EXAMPLE and attu2.
```
python remotetestmulti.py --user username --pass password --dir ../test/ --args "run_tests.py" --host EXAMPLE --host attu2
```
This will begin running the tests on the two hosts. attu2 is a relatively fast machine, and usually finishes the repy tests around the 180 second mark. When finished, you can check EXAMPLE.result.txt and attu2.result.txt for the results.

Running the NM tests is slightly more complicated but possible. This procedure has only been tested using remotetest.py, but might work with remotetestmulti.py. First we need to prepare to run the NM.

 1. cd ../test/
 2. python nminit,py
 3. cd ../minimal/

Now we are ready to start the NM. We will use attu2.
```
python remotetest.py --user username --pass password --dir ../test/ --args "nmmain.py" --host attu2
```
This will launch the NM on attu. Now open a new shell. Go back to the minimal directory.

Then, execute:
```
python remotetest.py --user username --pass password --dir ../test/ --args "run_tests.py -n" --host attu2
```
This will start the NM tests, and the results will be streamed to you. Be patient, as it may take some time before you receive any output.

After, the NM can be stopped either by waiting for 10 minutes, at which point the testingserver will terminate the NM, or by sending an interrupt to the testing server, using Control-C or 
```
kill -2 PIDOFREMOTETEST.PY
```



## Security, and other important notes
----
 * Usernames and Passwords are transmitted in clear text to the testing server.
 * Usernames and Passwords are stored in clear text in the server.cfg file. ** Please set file permissions to 600 (rw-------). **
 * This tool is designed for people who know what they are doing, it is not designed to be fool proof. Yes, giving it the wrong parameters or junk will break it.
 * Windows hosts and clients are not as optimized as NIX. This is not my fault, Windows cannot use select() on file descriptors, it has no notion of signals, and CMD.exe sucks.
 * The listening port is fixed at 50000
 * The advertisement is always done on SEATTLE_TESTBEDS and SEATTLE_TESTBED_host e.g. SEATTLE_TESTBED_attu2
 * There may be a ceiling on the size of the tgz file that can be uploaded, due to my implementation. This can be fixed if it becomes a problem. (For more info, see remotetest.py for send_mess() ).
 * The files are gzipped to save bandwidth, but this comes at the cost of CPU usage. However in most cases CPU > Bandwidth. My Atom CPU can do this, so don't complain.



## Running the testingserver.py on Windows, while being useful.
----

So Windows doesn't really have much in the way of job control, so you cannot do testingserver.py & and have it run in the background, because it will be killed when you log off. The solution to this is somewhat convoluted, as you need to setup a service to run python.

 * Search for 2 files, instsrv.exe and srvany.exe, They are available from Microsoft (something about a Windows 2K service kit...)
 * Store a copy of the "minimal" directory somewhere, e.g. C:
minimal. Put srvany inside this folder.
 * Lock down the permissions of server.cfg. For users, disable all access.
 * Then go to where you have instsrv.exe. Do instsrv.exe TestService "C:
minimal
srvany.exe"
 * Then open regedit. Go to HKey_Local_Machine
SYSTEM
CurrentControlSet
Services
TestService
 * Make a sub-folder call Parameters
 * In side Parameters, make 3 entries,  Application, AppDirectory, and AppParameters
 * Set Application to "C:
Python26
pythonw.exe" or wherever python is.
 * Set AppDirectory to "C:
minimal
"
 * Set AppParameters to "C:
minimal
testingserver.py"
 * Open services.msc, then go to TestService. Open its properties.
 * Set it to start automatically. On the credential tab, lower its permissions from SYSTEM, in case somebody is malicious. In the Error tab, set it to restart automatically on the first and second failures. Just in case.
 * You can reboot, or manually start the service now. Then check using remotetest.py --list if the computer is auto advertising.

For more information, see this URL: http://www.tacktech.com/display.cfm?ttid=197. This gives a nice overview of the process, and has a link for the required files.
 





