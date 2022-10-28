
# Security layer testing and penetration

In this assignment you will learn how to attack a reference monitor. The reference monitor you will be testing uses the security layer framework (encasement library, etc.) for the Seattle testbed. It is possible to do this assignment separately, but it is recommended that this assignment be completed after [Part One](LeftPadPartOne.md). Either way you should already have a working security layer or access to one. Testing the security layer is done by running a series of test cases that an adversary may use to circumvent your system. This assignment is intended to prepare you for thinking about security paradigms in a functional way. The ideas of information, security and privacy have been embedded into the steps of this assignment.


## Overview
----
In this assignment you are a tester. You have been sent a bunch of reference monitors that need testing before they are deployed. Your job will be to ensure an attacker cannot circumvent these security layers. In order to do this, you will attempt to write, and append invalid data. If you are able to do so, then the security layer is not secure. The future of the system depends on your ability to test code thoroughly!   

Three design paradigms are at work in this assignment: accuracy, efficiency, and security.

 * Accuracy: The security layer should only stop certain actions from being blocked. All other actions should be allowed.

 * Efficiency: The security layer should use a minimum number of resources, so performance is not compromised.

 * Security: The attacker should not be able to circumvent the security layer.

Within the context of this assignment these design paradigms translate to:

 * Accuracy:  The security layer should only modify certain operations (a strictly appending writeat() with one '\n') and raise an exception for certain other actions (a strictly appending writeat() with more than one '\n'). All situations that are not described above must match that of the underlying API.

 * Efficiency: The security layer should use a minimum number of resources, so performance is not compromised. For example, you may not call readat() everytime writeat() is called. It is permissible to call readat() upon fileopen(), however.

 * Security: The attacker should not be able to circumvent the security layer. For example, if the attacker can cause a non-strictly appending write to have ' ' inserted after '\n' or can cause the reference monitor to incorrectly error or hang, then the security is compromised.

You will submit a zip file containing all of the tests you have created. You will gain points for every student's reference monitor you find a flaw in. It is good if multiple tests of yours break a student's reference monitor, but you gain the same number of tests whether one or more tests break the layer.


## Prerequisites

This assignment assumes you have both the latest Python 2.7 and RepyV2
installed on your computer. Please refer to the [SeattleTestbed Build Instructions](../Contributing/BuildInstructions.md#prerequisites)
for information on how to get them.


### Helpful links
----
The following links will aid students in becoming comfortable with Python, Repy and seattle:
 * Official [Python tutorial](http://docs.python.org/tutorial/)
 * [Differences between RepyV2 and Python](../Programming/PythonVsRepyV2.md)
 * List of [RepyV2 API calls](../Programming/RepyV2API.md)


## Testing security layers
----
### Hypothesis, test case, counter example

The goal of a good tester is to test hypotheses.  A hypothesis is just a scientific way of asking a question.  The hypothesis of this assignment is "This security layer is well designed."  The questions you will ask when running your test cases will always be the same

 * "Is this reference monitor secure?"

 * "Does this reference monitor hamper performance?"

 * "Does this reference monitor prevent actions that should be allowed?"

Notice that these questions are parallels of the security paradigms: security, efficiency and accuracy, respectively.  

If we can find a case where the hypothesis is false, then the security layer is not secure.  Such a case is referred to as a counter example.  Hence all test cases should be designed to test for these three types of flaws.


#### Information on: Try, Except, Else, Finally
The try, except, else and finally statements are part of **exception handling**.  For more information on exception handling please visit:

 * [http://docs.python.org/tutorial/errors.html]
 * [http://wiki.python.org/moin/HandlingExceptions]
 * [http://www.tutorialspoint.com/python/python_exceptions.htm]

### Hints and Ideas for testing

When writing your own tests it is important to test for a complete set of possible penetrations.  Keep in mind, it only takes one test case to break through a security layer.  Some of the things you may want to test for include:

 * threading
 * multiple writes 

And more!  Remember a good security layer can't be broken by anyone!  Which is all part of the fun!  It's about solving a puzzle.  First you make the puzzle - write the security layer, then you solve the puzzle - try to bypass it.  If your puzzle is "good enough", no one will be able to break it, no matter what.  


## Notes and Resources
----

 * The following link is an excellent source for information about security layers: https://ssl.engineering.nyu.edu/papers/cappos_seattle_ccs_10.pdf

 * In repy 'log' replaces 'print' from python.  Many students find this to be a stumbling block.

 * Note that you should not assume that any files exist in your directory.  You should create any files (e.g., testfile.txt) yourself in your test program.

 * It's important to note that if a test has a flaw in any part of it, the entire test will be considered invalid. So, it's advisable to break your tests into different files. 

## How to run your tests on many reference monitors
----

Create a directory that the security layers will write their files into. You need to run repy with only access to this directory. You can write a test program that does `log(str(listfiles()))` to see if you are in the right place.

Have all the reference monitors to test and the test cases inside the same directory where the repy.py file exists.

* In the bash shell on Mac and Linux:
```
for referencemonitor in reference_monitor_*; do for testcase in <net_id>_*; do python repy.py restrictions.default encasementlib.r2py $referencemonitor $testcase; done; done
```
* In the Command Prompt on Windows:
```
FOR %r IN (reference_monitor_*) DO @FOR %a IN (<net_id>_*) DO @python repy.py restrictions.default encasementlib.r2py %r %a
```
* In PowerShell on Windows:
```
foreach ($referencemonitor in Get-ChildItem reference_monitor_*) { foreach ($testcase in Get-ChildItem <net_id>_*) { python repy.py restrictions.default encasementlib.r2py $referencemonitor.Name $testcase.Name } }
```

This will print out the output from each program. Make sure that you replace `<net_id>` with your NetID.

If you want to spot the referencemonitor that failed during the test run, add echo the name of each referencemonitor before the inner loop, like so:

* In the bash shell on Mac and Linux:
```
for referencemonitor in reference_monitor_*; do echo $referencemonitor under test; for testcase in <net_id>_*; do python repy.py restrictions.default encasementlib.r2py $referencemonitor $testcase; done; done
```
* In the Command Prompt on Windows:
```
FOR %r IN (reference_monitor_*) DO @(ECHO %r under test & FOR %a IN (<net_id>_*) DO @python repy.py restrictions.default encasementlib.r2py %r %a)
```
* In PowerShell on Windows:
```
foreach ($referencemonitor in Get-ChildItem reference_monitor_*) { Write-Host $referencemonitor.Name; foreach ($testcase in Get-ChildItem <net_id>_*) { python repy.py restrictions.default encasementlib.r2py $referencemonitor.Name $testcase.Name } }
```

This will print out the name of each reference monitor before it starts executing the testcases against it.


## What to turn in?
----
 * Never raise unexpected errors or produce any output. Your program must produce no output when run normally.
 * Turn in the test cases used to attack a given reference monitor in a zip file.   The name of each testcase must match the following format: [ net_id ]_attackcase1.r2py, [ net_id ]_attackcase2.r2py, etc.
