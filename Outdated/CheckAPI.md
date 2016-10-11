# CheckAPI

CheckAPI is used to check for behavioral differences between implementations of Repy V2 on various supported hardware. This document serves as a guide on how to use CheckAPI, additionally it covers its current limitations. 

----

----




## Using CheckAPI

CheckAPI's primary version uses security layers to interpose on API calls, log them and then verify them against a model of the API. The first step in using CheckAPI is to copy all of the required files from https://seattle.poly.edu/browser/seattle/branches/repy_v2/checkapi/ into a directory that contains all of the required Repy V2 files. This can be done via preparetest.py

If the application you are running with CheckAPI will try and **open any existing files** in the filesystem they must be added to the check_api_initial_filestate.input file that is used at initialization time of CheckAPI. If this is not done the model will not know that a given file exists but the implementation will, which will result in a conformance failure. It should be noted that any new files added to this file must be separated by a new line.

```
python preparetest.py -checkapi <directory_name>
```


After this you can run any application that supports Repy V2 with CheckAPI with the following command:

```
python repy.py <restrictions file> encasementlib.repy dylink.repy check_api.repy <program under test>
```


## Current Limitations

 * Currently looking into a method to reduce some false-positives for pending API calls.

## Future Work

**Core Model File System State:**

 * Currently the user of CheckAPI must list in the check_api_initial_filestate.input file **all** of the possible files that an application may want to access on the filesystem. This can sometimes be difficult to tell if the applications you are using are ones that you did not make yourself. It may be nice for the CheckAPI core model to attempt to import a file into its model state if and only if it exists in the file system. For example:
    * If while in the middle of executing an application it calls openfile("repy.py", create=False) where repy.py was not listed in the check_api_initial_filestate.input file before execution this would normally cause an model conformance failure. This is because the model has no idea that this file exists in its file system where as the implementation checks the file system and opens it without any problem.
 * Where as an updated version of the core model, specifically the openfile() API call, would check the the filesystem (via the implementation openfile() call) to see if the file in question existed, if it does then it would import the file and its contents into the core model's in memory state.
 * It should be noted, however, that this could mask some bugs related to openfile reporting that a file exists when it shouldn't, or errors like this. I imagine these would be rare though.

## API Calls Currently Not Verified by CheckAPI
Some API calls are not currently being verified by CheckAPI. Below is a list of the calls that are currently not supported with a brief explanation as to why they are not included. If an API call from [RepyV2API](https://seattle.poly.edu/wiki/RepyV2API) is not included in this list it means it is supported by CheckAPI.

 * sleep(), getruntime()
    * Not modeling time.
 * getthreadname()
    * Assumed correct for CheckAPI to work.
 * exitall()
    * Nothing to verify. However, this currently forces a final verification of other calls when executed.
 * createvirtualnamespace(code, name), virtualnamespace.evaluate(context)
    * Not modeling namespace calls.
 * getresources()
    * Some aspects of resources are being verified but not the getresources call itself.
 * getlasterror()
    * Not supported.
 * safelyexecutenativecode(binary, arglist)
    * Not modeling Lind related calls.

## Unit Tests that are not supported with CheckAPI
A handful of repyv2 unit tests are not supported with CheckAPI. This is mostly because of resource usage assumptions that the unit tests have.
 * ut_repyv2api_fileclosereleasesresource.py
 * ut_repyv2api_filereadatperformsresourceaccounting.py
 * ut_repyv2api_filewriteatperformsresourceaccounting.py
 * ut_repyv2api_openfileconsumesfilehandles.py -> resources & listfiles issue.
 * ut_repyv2api_initialusevaluesaresane.py
 * ut_repyv2api_openfileperformsresourceaccounting.py
 * ut_repyv2api_listfilesperformsresourceaccounting.py
 * ut_repyv2api_removefileperformsresourceaccounting.py
 * ut_repyv2api_stoptimesaresane.py

