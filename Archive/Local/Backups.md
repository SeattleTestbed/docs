# Backups of Server Data

This describes the current state of our backups. There's an open ticket for backups: #267

If anything looks incomplete, missing, or wrong, then it probably is and assistance/reminders/criticism is welcome.

## General Info

Backups are currently being done on seattle.cs, seattlegeni.cs, or betabox.cs.

On any of these systems, its own backed up data and helper scripts for backing up the data are found in a /backups directory (yes, that's at the root of the filesystem). This is owned by root and is chmod 0700.

The /backups/scripts directory contains scripts that do the backups. Some or all of these will be invoked through root's crontab.

The ssh key for scp'ing to a remote system will be found at /root/.ssh/backups_rsa. For backups that are being scp'd to a remote system, the remote system had a user created on it specifically for backups from this specific server. For example, seattlegeni.cs has a user account named backups-seattle which seattle.cs uses to scp files over. The /home/backups-* directories are always chmod 0700 (and owned by the corresponding user).

The danger of ssh access between systems (e.g. risk to other systems in the event of a single system compromise) is mitigated by having scponly installed on each system that receives backups (i.e. `apt-get install scponly`) and having the backups-* users always have /usr/bin/scponly as their shell. I haven't gone through the process of setting up scponlyc (the chroot'd version) on each system because that's not as simple as just installing the package. Ideally, it should be done.

Not backed up automatically, but relevant to ask justinc or jsamuel at any random time to test their knowledge: do you know where backups of the main and beta software update keys are, as well as the v2 owner keys?

## seattle.cs

Contents of /backups:
  * one-offs
  * scripts
    * scp_backups_to_other_system.sh
    * svn_backup.sh
    * trac_backup.sh
  * svn
  * trac

The svn_backup.sh script uses svn-hot-backup (from the Ubuntu package subversion-tools). The trac_backups.sh uses trac-admin hotcopy. Both of these are run weekly. The reason they aren't run daily at the moment is mostly because there is no cleanup of old backups.

The scp_backups_to_other_system.sh scp's to seattlegeni.cs the latest trac and svn backups. Currently, only a single copy of the backups are kept on seattlegeni.cs at a time.

Current backup-related entries in root's crontab:
```
### svn_backup.sh: Friday night svn backup
20      0       *       *       6       /backups/scripts/svn_backup.sh
### trac_backup.sh: Friday night trac backup
0       1       *       *       6       /backups/scripts/trac_backup.sh
### scp_backups_to_other_system.sh: Saturday night scp'ing of backups to another system.
0       2       *       *       0       /backups/scripts/scp_backups_to_other_system.sh
```

## seattlegeni.cs

Contents of /backups:
  * geni
  * mysql
  * one-offs
  * scripts
    * automysqlbackup.sh
    * scp_backups_to_other_system.sh
    * tar_geni_home_dir.sh

MySQL backups on each system are done with [automysqlbackup.sh](http://sourceforge.net/projects/automysqlbackup/). The result is the the maintaining of daily, weekly, and monthly sql dumps for each database.

The tar_geni_home_dir.sh script runs weekly.

Backups are scp'd to seattle.cs. The scp'd files are the last 7 days of mysql database dumps and the latest tar of the geni home dir.

Current backup-related entries in root's crontab:
```
### automysqlbackup.sh: nightly backup of all mysql databases
0       0       *       *       *       /backups/scripts/automysqlbackup.sh
### tar-geni-home-dir.sh: Sunday night tar'ing up of the /home/geni directory
20       0       *       *       6       /backups/scripts/tar_geni_home_dir.sh
### scp_backups_to_other_system.sh: Saturday night scp'ing of backups to another system.
0       1       *       *       0       /backups/scripts/scp_backups_to_other_system.sh
```

## betabox.cs

Contents of /backups:
  * geni
  * mysql
  * one-offs
  * scripts
    * automysqlbackup.sh
    * scp_backups_to_other_system.sh
    * tar_geni_home_dir.sh

MySQL backups on each system are done with [automysqlbackup.sh](http://sourceforge.net/projects/automysqlbackup/). The result is the the maintaining of daily, weekly, and monthly sql dumps for each database.

The tar_geni_home_dir.sh script runs weekly.

Backups are scp'd to seattlegeni.cs. The scp'd files are the last 7 days of mysql database dumps and the latest tar of the geni home dir.

Current backup-related entries in root's crontab:
```
### automysqlbackup.sh: nightly backup of all mysql databases
0       0       *       *       *       /backups/scripts/automysqlbackup.sh
### tar-geni-home-dir.sh: Friday night tar'ing up of the /home/geni directory
20       0       *       *       6       /backups/scripts/tar_geni_home_dir.sh
### scp_backups_to_other_system.sh: Saturday night scp'ing of backups to another system.
0       1       *       *       0       /backups/scripts/scp_backups_to_other_system.sh
```

## Links
[Backing Up and Restoring Database](http://www.thegeekstuff.com/2008/09/backup-and-restore-mysql-database-using-mysqldump/)