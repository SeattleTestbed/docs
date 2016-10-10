# Important tasks
----



----



## ~~NAT traversal in production   --- Justin      (**Eric**)   ---   3 tokens~~
----
(Tickets #227, #228, #274, #299, Ticket #228 related to "remote deployment repy")

We need to deploy the forwarder on a selection of nodes. It makes sense to get code / help from others in several areas:

Alper has experience with running code in parallel to check on the status of Seattle nodes. You'll want to check through the node manager not by sshing to nodes.
To get the original resources, Ivan or I can help with that when you're ready for real resources. To test, get resources from seattlegeni.

The Current Forwarder limits the number of servers that can connect by simply closing any connections that occur after the limit has been reached (until some servers disconnect)
Instead the forwarder should do a stopcomm and stop advertising until there is room for additional servers.

Update seash and the node manager so that they use the NAT traversal layer.

The forwarder needs to be integrated with the newest advertisement layer. Ensure that the forwarder does not advertise itself when it is busy and cannot receive new connections




## Node Manager detects IP changes    ---   Justin   ---   1 token
----
No ticket

The node manager should detect and log if its IP address changes.   Ideally it won't die horribly without telling us or advertise the wrong IP address.




## ~~Build demokit from SVN   ---   Ivan (**Richard**)   ---   1 token~~
----
No ticket

We should be able to build the demokit from SVN.   This should include only the files that are needed.

See r1968.  I moved some of the old demokit to trunk/repy/apps/old_demokit.  The upd* files where nowhere else in the svn.




## ~~Find out where we are with Windows Mobile    ---   Justin   (**Armon**)   1 token~~
----
Ticket #259

We need a precise reason (not an exception listing) why the tests fail on Windows Mobile. I.e. "the selectorstop test fails because the threading library on mobile does not accurately return the number of active threads"




## ~~XMLRPC web backend   --- Ivan (**Jason**) ----  3 tokens ~~
----

Ticket #255
Appropriate the AJAX functions that are used to access the GENI portal and add new XMLRPC functions to expose as much of the web back-end as possible via XMLRPC. We can then use this new interface to (1) test the GENI portal (2) consider a remote API to GENI portal that can be used by users from seash, etc.
This will involve understanding much of the functionality inside of the GENI portal. Cleaning up code so that the pieces that are independent of protocol can be execute by both the HTTP handlers, as well as the XMLRPC and AJAX handlers. Also, this will involve writing a test program for every XMLRPC call exposed in GENI. 



== ~~GENI bug squashers / testing   ---   Justin   ----  squishy ~~==
---- 
Tickets #254, #165, #189, etc
The GENI portal has numerous outstanding tickets having to do with everything from user-interface bugs (#254) to complex resource and database management issues (#165, #278). Additionally, most of the GENI code is untested and requires thorough integration tests to be written to test that the database is always in a consistent state, and is modified accordingly. The testing part of this task will involve understanding the XMLRPC web backend (see above).



## ~~ Custom installer creator port to Django --- Ivan (**Sean**) --- 1 tokens ~~
----

Tickets #312, #76, #78, #90, #91, #92, #93, #73 ..

The current custom installer creator is written in PHP, and has numerous problems. It lacks documentation, it is not consistent in its use of installer scripts, and is in general in a messy state. This task involves porting the custom installer to Django, and integrating it with the look/style/feel of the GENI portal.




## ~~ Remote installer builder service with XMLRPC interface --- Ivan ---  2 tokens  ~~
----

No ticket

Currently we create/customize installers in the custom installer creator, and in GENI. It is likely that we will have other services that need to create/customize installers in the future. We need a common service that provides this functionality so that the same functionality is not implemented multiple times and there is a common point where Seattle installers are distributed.

This task will involve (1) reviewing the existing prototype for creating remote installers, and working on it until its ready for production use, (2) writing integration tests for the service, and (3) converting of existing services that create/customize installers to use the newly built service (e.g. GENI, and custom installer creator).




## ~~Installers    ---    Justin (**Zachary**)   ---   3 tokens~~
----
(No direct ticket, related tickets #219)

Clean up the installer scripts so that they meet the style guidelines and are well tested.   In particular, ensure they will "do no harm" on any reasonable configuration.  

Right now, stop_seattle does the proper thing and calls seattlestopper.py, but start_seattle is for something completely different (and behaves differently than the documentation suggests). They should behave more intuitively.




## ~~ Software updater integration test   ---       ---   1 token  ~~
----
(No ticket)

Write a series of black box integration tests for the software updater.   This should test everything from the website to the fact that the node manager and software updater actually restart.



## Test framework for Python   ---   ???   ---   2 tokens
----
Compare and contrast different Python testing frameworks.   Write a small amount of test code in each and put it up for a vote.



## ~~Remote deployment for repy   ---   Justin (Eric)   --- 1 token~~
----
Related to ticket #228

Build a framework that deploys and monitors a simple repy service.   It should get VMs for the service, run the code, and when instances die, log information and restart them on new nodes.



## ~~Remote deployment Seattle   ---   Justin (**Kon**)   ---   3 tokens (ongoing)~~
----

Build scripts to deploy Seattle and keep it deployed.   We should use XMLRPC to get node lists from PlanetLab APIs, ensure our slice is on all nodes, and then deploy on them.   For CS machines, we will need to be able to load on them.   This interacts with monitoring.  



## ~~Installer builder cleanup   ---   Justin (**Zachary**)   ---   squishy ~5 tokens~~
----

Related tickets (#59, #57, #61, #302, #153, #155, #288, #72)

Fix the installer builder scripts so that they meet the style guidelines, don't have bugs, and are easy to debug / change.  **This task is not to be underestimated!**

pyc files should not be packaged in installers.   the meta info file should not be part of the installers

Make sure the node manager runs after install.   It doesn't look like it started when we ran it during the coding sprint.

There seem to be several unnecessary files in the installer (which is what clean_folder.py is for, just make sure we're using it effectively).

We need to add our license to the installers and demokit. This is the GENI Public License (which is textually equal to the MIT license).

All the warnings in the installer builder scripts should be dealt with. For the files that are being warned about, see if they ought to be there. If they are, tell the cleaner script that they are required. If they should not be there, tell the cleaner script to delete them.

Changes in the way the servers are set up require that some of the deployment process be done by hand, at least for now. The instructions on the wiki page need to be updated to include all the new steps (copying the installers over to seattlegeni.cs.wa..., deleting old installers on seattlegeni).

Make base installers sometimes fails.  

The specific exception on one computer was:

Error: required file timeutil
.py not found
Traceback (most recent call last):
 File "/home/cosminb/rscom/trunk/dist/make_base_installers.py", line 495, in <module>
 main()
 File "/home/cosminb/rscom/trunk/dist/make_base_installers.py", line 492, in main
 build(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
 File "/home/cosminb/rscom/trunk/dist/make_base_installers.py", line 427, in build
 prepare_initial_files(trunk_location, include_tests, pubkey, privkey, install_dir)
 File "/home/cosminb/rscom/trunk/dist/make_base_installers.py", line 152, in prepare_initial_files
 writemetainfo = imp.load_source("writemetainfo", "writemetainfo.py")
 File "writemetainfo.py", line 14, in <module>
 from repyportability import *
ImportError: No module named repyportability

It's most likely an error with how imp.load_source is being used - this probably isn't the best way to import something.

The name of the build_installers.py should be something like installer_utils. Ivan needs to be notified first so he can update the installer customizer.




## ~~Monitor nodes we can log into, get VM logs from nodes, work with database, state of node should be logged    ---   Justin (Kon)   ---   4 tokens~~
----

We want a monitoring program to go and check the status of nodes.   We have scripts that can be run on nodes that we can ssh to that provides detailed information.  

We also should go and pull the logs from the service VMs.

Grab information from the GENI database and check its accuracy.

Log information into a database with a very, very simple web front end.




## Test Seattle on different platforms   ---   Justin?   ---   5 tokens
----
Build a test framework that allows us to easily run our code (including whitebox and blackbox tests) on different platforms.   Developers should be able to "queue" test runs by running a command from an instance of SVN that will then deploy and test their code on different architectures.



## ~~Repy / Node Manager rapid response team   ---   Justin (**Cosmin, Armon**)     ---   squishy   1/2 token per bug?~~
----

Fix bugs as they arise with Repy and the node manager.   Requires good overall understanding of the project, attention to detail, and on some occasions requires speed.



## ~~ Autograder (usable but rigid)   ---   Ivan (**Jenn**) --- 3 tokens ~~
----
We want a version of the autograder that is usable by instructors.   It does not need to support instructors uploading NS files or test cases.   It is okay for it only to work with the NS files and test files we ourselves upload.




## ~~Reasonable number of events    ---     Justin    (**Armon**)   ---   1 token~~
----
(Ticket #256)

From what we can tell, there isn't a logical and portable way to determine how many threads a system can actually support. The number reported by the OS is way too high and the system will die long before that. The number in use is way too low.
The plan is to try to determine if we're on a "thread limited" platform (like a phone) and if not, take X events. (please add a comment saying how many) If we're on a phone it will be many fewer perhaps Y events.




## Bi-directional Bandwidth measurement    ---    Justin    (**Anthony**)   ---   2 tokens
----
(Ticket #161)

The bandwidth code right now is specific to client or server, and only allows a client to check upload speed. We want to have one set of code, written in repy, that would allow one to check both upload and download speed.




## ~~ Actually getting 10% (installer updates, determining offcut size)   ---   Justin   (**Anthony**)     ---   3 tokens  ~~
----
(Tickets #257, #258)

There needs to be a way to determine the offcut resources size on an arbitrary platform. This will vary a lot from system to system and so needs to be determined at install time.

We need to make the installers and custom installer creator work together to deal with the 10% resource changes. The end result is that the installer will work based upon percentages. The total resources will be determined by the benchmarking scripts and the appropriate percentages will be assigned to each of the VMs.





## TCUP demo / see if there is Tor interest   ---   Ivan (**Richard**) ---   ~3 tokens
----

Tickets #205, #301

We need to communicate with Tor folks to understand their requirements more, and to come up with a TCUP version that will entice them if possible. We also need to get TCUP to a state where its usable out of the box with a solidly working congestion control. This will involve performing numerous benchmarks of TCUP over the wide area, and comparing its performance to repy TCP and python TCP.




## Exception Hierarchy   ---   Justin?   ---   1 token
----
Determine if the currently proposed exception hierarchy can be made palatable to our developers.   Get some sort of yes / no resolution to decide if the current direction is a good one or if we need to move in an entirely different direction.   This requires talking a lot with the other developers.






## ~~ Formal specification of call behavior   ---   Justin (**Eric**)  ---   2 tokens  ~~
----
Specify the behavior of our API calls in a formal way.   I.e. lay out what should happen when calls are performed in parallel or sequence.   There are a lot of behaviors that currently are "loosely defined" such as whether "A" and "a" are different files on all oses, how sending from a closed socket should behave, how the system should respond to failed attempts to reuse a socket, what should happen if the OS doesn't support appending to a file, etc.




## Implement the new exception hierarchy   ---   Justin   ---   squishy ~6 tokens
----
After we have decided as a group on what our hierarchy of exceptions should look like, we need to adapt repy to support it.   This should be done after the formal specification of call behavior for our system calls.   The call behavior specification should be a useful guide that helps us create test cases for this.  



## ~~ Portability Strike Force   ---   Justin (**Armon** and **Conrad**)  ---   squishy ~6 tokens ~~
----
We need to ensure that the calls behave the same on every OS.   This currently isn't true for many calls.   This task is very detail oriented and will involve trying to find clever workarounds to mitigate the effect of OS weirdness.





== ~~RSA integration with production code ---   Justin (**Anthony**) --- 2 tokens ~~==
----

No ticket

Ensure we have a backwards-compatible way to use the new RSA routines with the old ones.   Update all of the production code to use this.




## Lisping clean up   ---   Ivan   (**Alper**)   ---   2 tokens
----

Ticket #263

Clean up the map-reduce code -- i.e. make sure that all files are well commented and ready to be used by an instructor as an example solution. Write up a 3-4 step assignment that outlines how to code map-reduce in repy. This is **not** intended to add any new features to the existing map-reduce implementation. We are trying to tie off loose ends.




## CNC   ---   Justin   (**Cosmin**)   ---   squishy 3 tokens
----

Cosmin's thesis.   If you're not him, this isn't for you!




## Service composition scaffolding   ---   Justin   (**Eric**)   ---   squishy 3 tokens
----
Eric's thesis.   If you're not him, this isn't for you!




== ~~Sysadmin strike force: backups, accounts, pinging   ---   Justin (Monzur)  ---   ??? tokens ~~==
----
(Tickets #267, #306, #307, #308, #309, #310 but this is the tip of the iceberg)

Our project is growing and developing more and more complex code. As a result, we need relevant system and technical support to maintain our operations. This includes (1) making regular backups of essential data (2) maintaining accounts across our systems/wiki (3) documenting our setup so that its easy to reproduce/setup a version of seattle.poly.edu from scratch (e.g. in case of crash) (4) adding robustness to our services by creating availability ping tests (5) running simple tests for essential services -- e.g. does the website work?, is mysql running?, etc (6) creating proper daemon scripts for daemons that we currently run as users by hand, etc.



## ~~  Tutorial / TakeHomeAssignment clean up --- Justin (Justin) --- 2 tokens ~~
----

We need an experienced developer (with a good grasp of the English language) to go through our tutorials and the TakeHomeAssignment and vet them for bugs.   There are likely little mistakes throughout these and we'd like to catch them.




# Possibly inactive tasks
----

## X    Working Windows Mobile port
----

## X    Working Nokia N800
----

## X    Working Jailbroken iPhone


## X   Real installers

(Tickets #63, #64)

Mainly, we need to set up the server so that it will build the NSIS installer when the installers are customized.



## X    Autograder (production)   ---   Ivan ---   squishy
----

We want a general autograder that allows instructors to upload NS files and / or test cases.   There are a lot of security and usability questions to doing this which we have no answer for.



## ?   Documentation clean up
----

## ~~  ?   Building a small number of services for service composition ~~
----

## ~~  ?   Allow ssh keys to be imported to use our RSA routines  --- Justin (**Anthony**) ~~
----
Ticket #393

## ~~  ?   RSA implementation finish up   ---   Justin  (**Anthony**) ~~
----
Ticket #247

Improve the existing implementation with padding scheme as defined in PKCS!#1 to prevent. It may be possible to use the existing repy SHA without porting SHA256. A masking function will also need to be implemented. This will be done to prevent the vulnerability of a chosen plaintext attacks. As noted in the wikipedia page (but not yet verified elsewhere), a Optimal Asymmetric Encryption Padding scheme is as vital to signing as it is to plaintext encryption.

A copy of PKCS!#1 V2.1 can be found at
http://www.rsa.com/rsalabs/node.asp?id=2125
Additional motivation for improvement can be found in
http://www.cs.bgu.ac.il/~beimel/Courses/crypto/Boneh.pdf






# Startup Tasks for new students
----
The following are startup tasks that are to be assigned to new developers joining Seattle in the spring.

## ~~    XMLRPC client library repy implementation   ---   Ivan (**Michael**) --- squishy 3 tokens ~~
----

## ~~  XMLRPC server library repy implementation   ---   Ivan (**Conrad**) --- squishy 3 tokens ~~
----

## ~~   Write a simple repy pickle implementation (with wiki page)   ---   Justin   --- squishy 3 tokens ~~
----

## Change run_tests.py so that the seattlelib tests can be run using it ---   Justin --- squishy 2 tokens
----


## ~~   Write a key gen daemon   ---   Ivan (**Kon**)   ---   squishy 2 tokens (including tutorials) ~~
----

Ticket #7

Maintain generated keys in a process (not database). Communicate with this process over a socket to request new keys.

## ~~  Write NTP forwarder   ---   Justin (**Zachary**) --- squishy 2 tokens (including tutorials)  ~~
----

## ~~  Read the local VM's resource file (given a user port)   ---   Justin (**Monzur**) --- squishy 2 tokens (including tutorials) ~~
   


# Collaboration
----

Move from IM/email to IRC/tickets?
   Let's have an IRC "group meeting" to decide how to assign tasks!  
 
Bug weekends!
   There will be some prize or prizes to be determined.   If you have an idea, let us know!