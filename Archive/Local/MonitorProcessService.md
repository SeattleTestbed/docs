# Seattle and SeattleGENI Monitoring Scripts

----

----

## Overview
----

The monitoring scripts that live in Seattle and SeattleGENI ensure that critical processes that are running on the machines are constantly running. The script runs every 15 minutes on both machines, and if any of the critical processes are down then the system admins are sent an email as well as a message is posted on the irc.



## Configuration
----

 * Seattle and SeattleGENI monitoring scripts live in /home/geni/cron_tests/
 * The tests run as the geni user on a cron schedule scheduled by the user cron of the geni user
 * The test logs are written to /home/geni/cron_logs/



## Monitor Processes
----

### Purpose
The purpose of monitor_processes.py is to ensure that if any of the critical processes go down in either seattle.cs or seattlegeni.cs then the system admins are notified and a message is posted on the irc. The script runs every 15 minutes.

### Deployment
To deploy monitor_processes, run the deploy_monitor_processes.py located in trunk/integrationtests/deployment_scripts/. Run the script with the option -cseattle in order to set up the crontab on the seattle.cs machine and with the option -cseattlegeni to setup a crontab for the script to run every 15 minutes.

In order to set everything up, create a folder in the same directory that the folder trunk/ is located <folder_1>. Create a second folder <target_folder> where you want to deploy the monitor_processes script. Run preparetest.py on <folder_1>. Then copy over the file deploy_monitor_processes.py and setup_crontab.py from the deploy_scripts/ folder to <folder_1>. Copy over preparetest.py from trunk/ to <folder_1> Then run the deploy_monitor_processes script using the following line:
```
python deploy_monitor_processes.py -cseattle <target_folder> <target_log_folder>
   or
python deploy_monitor_processes.py -cseattlegeni <target_folder> <target_log_folder>
```
<target_log_folder> is the folder where you want the logs from the centralizedputget script to be stored.

### Schedule
The script runs once every 15 minutes. The current crontab on seattle.cs looks like:
```
*/15 * * * * export GMAIL_USER='seattle.devel@gmail.com' && export GMAIL_PWD='repyrepy' && /usr/bin/python /home/geni/cron_tests/monitor_processes/monitor_processes.py -seattle > /home/geni/cron_logs/seattlecron_log.monitor_processes
```
and the crontab on seattlegeni.cs looks like:
```
*/15 * * * * export GMAIL_USER='seattle.devel@gmail.com' && export GMAIL_PWD='repyrepy' && /usr/bin/python /home/geni/cron_tests/monitor_processes/monitor_processes.py -seattlegeni > /home/geni/cron_logs/seattlecron_log.monitor_processes
```



## Processes Currently Running
----
These are the processes that are currently running on the machines, which are being monitored
 * **Seattle**
    1. advertiseserver.py
 * **SeattleGENI**
    1. expirevessels.py
    1. donationtocanonical.py
    1. canonicaltoonepercent_mayevents.py
    1. dbnode_checker.py
    1. apache2
    1. mysqld
