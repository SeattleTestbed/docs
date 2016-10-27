## Developers' Notes for Modifying the Clearinghouse Code Base

If you are a developer wanting to work on the Clearinghouse code, you will probably want to start each component of the Clearinghouse separately and manually to check whether it performs as it should.



### Before you begin
Ensure that the key database (usually called `keydb`) is set up. You can do this from the MySQL prompt using the `show databases;` command. To see if `keydb` contains tables, `use keydb; show tables;`

If the database does not exist, set it up as follows:

  * Make sure have a MySQL database to use for the key database. We suggested above to call it
      `keydb`.
  * Edit the file `keydb/config.py` and set the database information for the key
      database.
  * Create the key database structure by executing the contents of the file
      `keydb/schema.sql` on the new key database you created. If set up as suggested with both the user and databse names `keydb`:
```sh  
$ mysql -ukeydb -p --database=keydb < keydb/schema.sql
# This will prompt for the keydb database password!
```
  * Make sure that the file `keydb/config.py` is not readable by the user the web server will be running as, i.e. it is only user-readable (but neither group- nor world-readable), owned by the clearinghouse user, and the web server is not in the user group the file belongs to.
  * The same goes for `backend/config.py`.
  * Furthermore, edit the file 'backend/config.py' and set a value for `authcode`.


## Developers: Working on the clearinghouse code

The backend scripts can be started with a script [#Runningstart_clearinghouse_components.sh start_clearinghouse_components.sh]. When starting the components manually, you need to start them **in the order shown**. Most importantly, first start the lockserver, then the backend, then everything else.

For every component that you run, we advise to set up a new `screen` instance (or use separate shells if you prefer). Make sure you have set the environment variables, `PYTHONPATH` and `DJANGO_SETTINGS_MODULE`, correctly. See wiki:ClearinghouseInstallation for details.

The steps below assume you deployed your test clearinghouse into `/tmp/TARGET/clearinghouse`, and have the RepyV2 runtime set up in `/tmp/TARGET/seattle`.

  * **Start the lockserver**
```sh
$ cd /tmp/TARGET/clearinghouse
$ python lockserver/lockserver_daemon.py
```
The lockserver starts and tells you which port it listens on, and that a thread has been started.
(If you get an `ImportError` instead, then please check your environment variables again.)

  * Start the backend_daemon. Due to a bug, this must be done from the `seattle` directory currently
      (because the repy files need to be in the directory it is run from):
```sh  
cd /tmp/TARGET/seattle
python ../clearinghouse/backend/backend_daemon.py
```

  * **Start the polling daemons**. Again, this must be done from the `seattle` directory currently:
```sh   
cd /tmp/TARGET/seattle
python ../clearinghouse/polling/check_active_db_nodes.py
```

  * **Start the node state transition scripts**. Again, this must be done from the `seattle` directory currently:
```sh
cd /tmp/TARGET/seattle
python ../clearinghouse/node_state_transitions/TRANSITION_SCRIPT_NAME.py
```
    * The four transitions scripts that you want running are:
      * transition_donation_to_canonical
      * transition_canonical_to_twopercent
      * transition_twopercent_to_twopercent
      * transition_onepercentmanyevents_to_canonical

This should leave you with a working Clearinghouse instance.

