# Continuous Build

We have a continuous build system that runs some of our tests regularly based on the current svn trunk. The idea is to run it on multiple different "slave" systems and have the results collected by a "master" system.

Current slave systems each have a "continuousbuild" user that the master system's "continuousbuild" user can ssh into to collect test output.

Overall test results page: http://blackbox.cs.washington.edu/~continuousbuild/

Test failures RSS feeds (there's a separate one for each slave):
  * http://blackbox.cs.washington.edu/~continuousbuild/linux/failures.rss
  * http://blackbox.cs.washington.edu/~continuousbuild/bsd/failures.rss
  * http://blackbox.cs.washington.edu/~continuousbuild/mac/failures.rss

The continuous build is currently running only some of our tests. Time just needs to be spent making other tests work with the system.

To add new tests to the system, add files to svn in trunk/continuousbuild/tests/ that are executable and have a filename that starts with 'run_'. Then make the script accept two arguments: the first is a path to svn trunk, the second is a file that all stdout and stderr output from the tests should ultimately be written to. The testrunner then runs the tests and exits with a non-zero status the tests failed. Any output from the testrunner itself will not indicate failure but will be recorded in the logs for the run (that output should be kept to a minimum, though).

Make sure to setprop svn:executable on any files added to trunk/continuousbuild/tests/. (This will change when we make the tests all python scripts so they can run on windows).

# What if the continuous build doesn't seem to be running?

If the continuous build doesn't seem to be running even though the crontab is setup properly, check to see if a previous run got interrupted and left a "running" directory in the location that output is kept in on the particular slave system. For example, if a slave box was power cycled in the middle of a run, the "running" directory would be left behind. If that directory is there, future attempts to run the continuous build will quickly abort because they think another copy is already running.

# General Slave Setup Information

Generally:
  * Create a user account for running the continuous build tests (call it "continuousbuild", if you can).
  * Go to the home directory for the user (e.g. /home/continuousbuild) and 'svn co http://seattle.poly.edu/svn/seattle/trunk"
  * From your own system's copy of trunk which you've checked out while authenticated, copy the 'assignments' directory to the copy of trunk you've checked out without authentication on this slave system. The software updater tests need the assignments/webserver/ directory in order to run.
  * cp trunk/continuousbuild/cron_run_tests.sh to /home/continuousbuild
  * Modify /home/continuousbuild/cron_run_tests.sh as needed (e.g. setting the PATH)
  * cp trunk/continuousbuild/config.py.sample trunk/continuousbuild/config.py
  * create a directory for output, e.g. trunk/continuousbuild/output
  * edit trunk/continuousbuild/config.py so that it puts log output in trunk/continuousbuild/output
  * Edit the user's crontab so that cron_run_tests.sh gets run hourly.
  * Put the blackbox.cs continuousbuild user's ssh pubkey in the slave continuousbuild user's .ssh/authorized_keys file.

After setting things up on the slave, go to the master (blackbox.cs), edit /home/continuousbuild/pull_test_results.sh, and modify it to rsync over the files from the new slave.

# Slave Setup on testbed-opensuse

The following is information specific to setting up the continuous build system on our testbed-opensuse box.

## Python

The continuous build on testbed-opensuse is running on Python 2.6.3 which was built by us. The 2.5.1 version of python available on the system by default has problems with sqlite, which are required to run the Seattle Clearinghouse tests.

Python was built by the `continuousbuild` user with:

```
./configure --with-sqlite --prefix=/home/continuousbuild/opt
make install
```

and the resulting binary in `~/opt/bin` is linked in `~/bin`. The `cron_run_tests.sh` script in the user's home directory is modified with `export PATH=/home/continuousbuild/bin:$PATH`.

Django 1.1 is also installed by the continuousbuild user with:

```
python setup.py install --prefix=/home/continuousbuild/opt
```

## Firewall

At the time of writing, NAT forwarding is new and not 100% reliable. This was causing the nodemanager tests to occasionally fail when a forwarder couldn't be found. Opening up port 1224 on this opensuse box involved the following:

Create a file `/etc/sysconfig/SuSEfirewall2.d/services/seattle-nodemanager` with the following:

```
# space separated list of allowed TCP ports
TCP="1224"
```

Edit the file `/etc/sysconfig/SuSEfirewall2` to add the name of the file created above to the list of services here:

```
FW_CONFIGURATIONS_EXT="sshd apache2 apache2-ssl seattle-nodemanager"
```

Reload the firewall:

```
/etc/init.d/SuSEfirewall2_setup reload
```

Note: you should check `iptables --list` after you reload the firewall to make sure you did it correctly. I'm not a SuSE person and apparently SuSE people think it makes sense to have two different init.d scripts, `/etc/init.d/SuSEfirewall2_init` and `/etc/init.d/SuSEfirewall2_setup`, and running `/etc/init.d/SuSEfirewall2_init reload` instead of `/etc/init.d/SuSEfirewall2_setup reload` will leave you with something other than what you wanted, namely, what appears to be no new inbound connections to any ports.

# Slave Setup on testbed-freebsd

The most noteworthy issue for the setup on testbed-freebsd is that bsd systems don't seem to have a setsid command available. So, we compile [browser:seattle/trunk/continuousbuild/util/setsid.c our own] on the system. Then put this somewhere (like /home/continuousbuild/bin) and customize the cron_run_tests.sh script so our setsid binary is in the PATH by adding this near the top:

```
export PATH=/home/continuousbuild/bin:$PATH
```

We also don't bother running Seattle Clearinghouse tests here, so we have set `SKIP_TEST_RUNNERS = ['run_seattlegeni_tests.sh']` in trunk/continuousbuild/config.py.

# Slave Setup on testbed-mac

Like testbed-freebsd, we have to provide our own setsid and customize the cron_run_tests.sh script so that our setsid binary is in the PATH. Unlike testbed-freebsd, the PATH that is setup by default for scripts run through cron seems to be lacking something important. (More details: #763)

So, we put the following in cron_run_tests.sh (that is, we keep the same PATH that one gets through an interactive shell as it seems to do the trick):

```
export PATH="/Users/continuousbuild/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/X11/bin"
```

We also don't bother running Seattle Clearinghouse tests on testbed-mac, so we have set `SKIP_TEST_RUNNERS = ['run_seattlegeni_tests.sh']` in trunk/continuousbuild/config.py.
