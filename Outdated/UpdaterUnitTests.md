# Running Software Updater Unit Tests

The softwareupdater tests start a local webserver and serve update files from there.

----

----



## Running the tests
  * Linux/Mac/BSD:
    * cd to the same directory preparetest.py is in (that is, trunk)
    * run `./softwareupdater/test/run_local_tests.sh name_of_directory_to_put_tests_in`
      * For example, create a temp directory and pass that as the only argument to the script.
  * Windows:
    * Run preparetest.py to a folder of your choosing.
    * Copy over the files from trunk/softwareupdater/test/ to that same folder.
    * Go to that directory and run `python utf.py -m softwareupdaters`
    * When running these tests on Windows, ps cannot be used to check process status.  You will have to do this yourself in the task manager.

## Notes
  * There cannot be another instance of softwareupdater.py running, or the restart tests will fail.  

## Output

Output if the test passed is one line indicating whether the test passed or failed (this test will take a while).

If the test fails, output will be produced, telling you what went wrong in which part of the test.

If everything is successful, there will be an instance of softwareupdater.py and nmmain.py running when the script completes.  It is non-trivial to clean these up automatically, because we do not directly start these processes.

Note: Actually, it's not that hard to clean them up (it can be done with process groups). The current scripts don't do it, though, so you'll end up with extra nmmain and software updater process running at the end.