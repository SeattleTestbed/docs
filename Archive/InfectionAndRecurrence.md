# Infection and Recurrence

# Overview

Our mission is to make it as simple as possible for us and the users to install seattle on their system, and to make sure that we can keep our installations running and up to date for as long as possible.

## Coding Sprint

 * January 17th

## Jan 10th - Jan 15th

 * Sal: Bring Justin's Python "deployment" program up to the standards specified in the code style guidelines and add unit tests.   Ensure that information is being logged from the program running on remote systems.

 * Brent: Check to see if the state of the files that are on the system is normal and if not log enough information that we can understand the issue.

 * Cosmin: Check the state of the running processes and if something is abnormal, log enough information that we understand the problem.

 * Carter: Build scripts that completely uninstall a failed install or otherwise clean up as needed.

## Jan 20th - Jan 27th

 * Brent: Go through the softwareupdater and its tests, checking for correctness, and documenting both update procedures and testing procedures.

 * Carter: Go through the process of creating the base installers and preparing the code for release to the software updaters. Document the procedure on the wiki.

 * Cosmin: Examine the current geni code and look for areas to improve. Determine which areas of the code need testing.

## Interesting things to think about

Many of the unit tests are timing based and so will fail on "slow" systems.   Can we address this somehow?

There are no repyportability / seattlelib unit tests.   

How do we prevent repy errors of the wrong type from having unit tests pass?

Lots of extra files in the installer that don't need to be there.

The installer builder / software updater builder has lots of unnecessary and distracting output

A "config file" to get rid of repyconstants, hardcoding the version in nmmain, etc.

Black box testing of installers / uninstallers

Do we need a tarball that allows people to run Repy code without being a Seattle node?

Clean up of installer

Bug autopsies?
