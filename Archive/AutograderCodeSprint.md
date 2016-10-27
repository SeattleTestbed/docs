# Autograder Code Sprint Strategy

This page will hopefully get us more organized in our approach in adding automatic grading support for the Seattle release.  Anyone is welcome to edit this page in a constructive manner in spirit of conversation!

## Completed work
 * Initial Demo version of the autograder up and running.  This was a good starting point and now we are ready to work on the production version!  We have lots of bugs to fix, and features to design.

## Plan of Attack
 * Features required for this release are listed at https://seattle.poly.edu/milestone/Autograder%20v1
 * Design and implement a way for course staff to specify an NS file, and ensure it meets our criteria for launching experiments with the autograder.
 * Design and implement a way for course staff to specify test meta-data, specifically a mapping of repy-files to emulab nodes for each test case.  This should integrate well with our system for specifying NS files
 * Re-design the data-management layer to use a database instead of files and directories
 * Improve output of grade functions
 * Fix bugs and add tests that ensure good integration between the autograder logic and nm_remote_api


# Current Codemonkeys

 * Eric Kimbrel 
 * Alper Sarikaya
 * Sal Bagaveyev
 * Jenn Hanson