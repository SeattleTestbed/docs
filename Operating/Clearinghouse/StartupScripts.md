# Seattle Clearinghouse Start up Scripts
This page describes which scripts need to automatically start on system boot and how to set them up.




## Overview
These scripts must be running **at all times** on both the production and beta Clearinghouses. They should be started as user root in a **screen** by running 
seattlegeni
deploymentscripts
start_seattlegeni_components.sh which will automatically start the needed components.
 * lockserver_daemon.py 
 * backend_daemon.py
 * check_active_db_nodes.py
 * transition_donation_to_canonical
 * transition_canonical_to_twopercent
 * transition_twopercent_to_twopercent
 * transition_onepercentmanyevents_to_canonical

Currently we handle automatically starting these scripts on system boot with a cron job under root.  The following is the cron job for the beta Clearinghouse.
 ```@reboot screen -S betaseattleclearinghouse -d -m /home/geni/start_seattlegeni_components.sh```
This can be set by 
 ```$ sudo crontab -e```
and entering the following line in the text editor.  Be sure to enter the proper values for ```clearinghouse_username``` and ```/path/to/start_seattlegeni_components.sh```.
 ```@reboot screen -S clearinghouse_username -d -m /path/to/start_seattlegeni_components.sh```
 