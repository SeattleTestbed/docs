
# Security layer testing and penetration

In this assignment you will learn how to attack a reference monitor.  The reference monitor you will be testing uses the security layer framework (encasement library, etc.) for the Seattle testbed.  It is possible to do this assignment separately, but it is recommended that this assignment be completed after [Part One](ABStoragePartOne.md).  Either way you should already have a working security layer or access to one.  Testing the security layer is done by running a series of test cases that an adversary may use to circumvent your system. This assignment is intended to prepare you for thinking about security paradigms in a functional way. The ideas of information, security and privacy have been embedded into the steps of this assignment.




## Overview
----
In this assignment you are a tester.  You have been sent a bunch of reference monitors that need testing before they are deployed.  Your job will be to ensure an attacker cannot circumvent these security layers.  In order to do this, you will attempt to read, write, and append data without having the proper missions enabled. If you are able to do so, then the security layer is not secure. The future of the system depends on your ability to test code thoroughly!   

Three design paradigms are at work in this assignment: accuracy, efficiency, and security.

 * Accuracy: The security layer should only stop certain actions from being blocked. All other actions should be allowed.

 * Efficiency: The security layer should use a minimum number of resources, so performance is not compromised.

 * Security: The attacker should not be able to circumvent the security layer.

Within the context of this assignment these design paradigms translate to:

 * Accuracy: The security layer should only stop certain actions from being blocked. All other actions should be allowed. For example, if an app tries to read data from the backup file, this must succeed as per normal and must not be blocked. All situations that are not described above must match that of the underlying API.

 * Efficiency: The security layer should use a minimum number of resources, so performance is not compromised. For example, keeping a complete copy of every file on disk in memory would be forbidden.

 * Security: The attacker should not be able to circumvent the security layer. For example, if the attacker can cause an invalid file to be saved, read the "write to" file, or can write to the backup file we read from, then the security is compromised.

You will submit a zip file containing all of the tests you have created.   You will gain points for every student's reference monitor you find a flaw in.   It is good if multiple tests of yours break a student's reference monitor, but you gain the same number of tests whether one or more tests break the layer.



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



### Examples of tests
Test cases are briefly described at [github: SeattleTestbed/docs/blob/master/EducationalAssignments/ABStoragePartOne.md] and [wiki:RepyV2SecurityLayers]. Below is another example of a test case you may want to consider.  This test case gives the right 'style' for your all your test cases, but lacks in the number of test cases.  A good attack will include many test cases.
#### Test case 1:

```
# New File Operation

# Clean up of existing file
if "testfile.txt.a" in listfiles():
 removefile("testfile.txt.a")
if "testfile.txt.b" in listfiles():
 removefile("testfile.txt.b")

# Open File Function Call
myfile=ABopenfile("testfile.txt",True)  #Create an AB file

try:
 # Empty/New File should have contents 'SE' satisfying the requirement
 assert('SE' == myfile.readat(2,0))
 # Close the file:
 myfile.close()
except:
 myfile.close()
 # Error Handle or Failure Condition
 log("Empty file is not handled properly!")

```
#### Code analysis
It is important to keep in mind that only lowercase file names are allowed.  So  in the above code, specifically:

```

# Open a file
myfile=ABopenfile("testfile.txt",True)

```
testfile.txt is a valid file name, however Testfile.txt is not.  Examples of other invalid files names are, testfile@.txt, testfile/.txt, and testfile().txt.  Essentially all non-alphanumeric characters are not allowed.

In this case we are verifying the security of the reference monitor. This code attempts to check the contents of a new valid file created through reference monitor. First the file is opened using ABopenfile function `myfile=ABopenfile("testfile.txt",True)`. Next `myfile.readat(2,0)` tries to read from the file which has been created. The 0 refers to an offset of zero and 2 refers to number of characters being read. The assert call would look to validate the condition mentioned within its call `Check for valid empty file string "SE"`and pass if the statement made is true or raise exception if the statement made is false which can be caught using exception handlers. Then finally: statement will always run, closing the file.

#### Test case 2:

```
# WRITE OPERATION
# New File Operation

# Clean up of existing file
if "testfile.txt.a" in listfiles():
  removefile("testfile.txt.a")
if "testfile.txt.b" in listfiles():
  removefile("testfile.txt.b")

# Open File Function Call
myfile=ABopenfile("testfile.txt",True)  #Create an AB file

# Write valid data to the file
myfile.writeat("StestE",0)

#Close the file
myfile.close()

# READ OPERATION
# Reopen file again to read
myfile=ABopenfile("testfile.txt",True)

# Read the file to check the contents
try:
 assert('StestE' == myfile.readat(6,0))
 #Close the file
 myfile.close()
except:
 #Close the file
 myfile.close()
 log("Valid Data write to a file is unsuccessfull!")

```
#### Code analysis

In this case we are verifying the accuracy of the reference monitor.  This code attempts to write `"StestE"` to the file and verify the contents.  We assume that valid data is written in the file from the zero offset. First the file is opened using `myfile=ABopenfile("testfile.txt",True)`. Next `myfile.writeat("StestE",0)` tries to write `"StestE"` to the file. Then `myfile.readat(6,0)`  tries to read the contents of the file. The 6 refers to an byte size of 6 characters and 0 refers to the offset 0 in the file. If the security layer fails the test then the assert call raises exception to be caught by except statement to show the error. The final statement which will always run, closing the file.

If this case produces anything other than "No Output", then this layer fails the accuracy design paradigm.  The security layer should not stop a file from being read or written.

#### More information on: Try, Except, Else, Finally
The try, except, else and finally statements are part of **exception handling**.  For more information on exception handling please visit:

 * [http://docs.python.org/tutorial/errors.html]
 * [http://wiki.python.org/moin/HandlingExceptions]
 * [http://www.tutorialspoint.com/python/python_exceptions.htm]

### Hints and Ideas for testing

When writing your own tests it is important to test for a complete set of possible penetrations.  Keep in mind, it only takes one test case to break through a security layer.  Some of the things you may want to test for include:

 * threading
 * writing to multiple files

And more!  Remember a good security layer can't be broken by anyone!  Which is all part of the fun!  It's about solving a puzzle.  First you make the puzzle - write the security layer, then you solve the puzzle - try to bypass it.  If your puzzle is "good enough", no one will be able to break it, no matter what.  


## Notes and Resources
----

 * The following link is an excellent source for information about security layers: http://isis.poly.edu/~jcappos/papers/cappos_seattle_ccs_10.pdf

 * [repy_v2/benchmarking-support/allnoopsec.py](https://seattle.poly.edu/browser/seattle/branches/repy_v2/benchmarking-support/allnoopsec.py) is an empty security layer that doesn't perform any operations.

 * [repy_v2/benchmarking-support/all-logsec.py](https://seattle.poly.edu/browser/seattle/branches/repy_v2/benchmarking-support/all-logsec.py) is security layer that performs logging functions.

 * In repy 'log' replaces 'print' from python.  Many students find this to be a stumbling block.

 * Note that you should not assume that any files exist in your directory.  You should create any files (e.g., testfile.txt) yourself in your test program.




## Extra Credit
----
Find bugs in the extra credit reference monitors given the altered threat model.  You should include more test cases in the extra credit!



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

 * Turn in the test cases used to attack a given reference monitor in a zip file.   The name of each testcase must start with your netid in lowercase.   For example: abc123_securitytest1.r2py abc123_goodaccuracytest.r2py are both valid names.
 * Optionally turn in the test cases used to attack the extra credit reference monitors in a zip file.   Note that in this case, you can expect that your code is run more than once.   In the name of the file, say if it needs to be run multiple times.   For example:  abc123_run_twice_metadata_removal.r2py abc123_run_once_threading_hack.r2py.
