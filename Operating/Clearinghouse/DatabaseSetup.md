# Seattle Clearinghouse Database Service

Seattle Clearinghouse uses the MySQL database, and InnoDB table types.

 * For info on installing/configuring the database, creating the necessary tables, etc, see [wiki:Archive/SeattleGeniInstallation].

----

----

## Configuration
----

The configuration file for MySQL is /etc/mysql/my.cnf

For example, this file defines the directory where MySQL tables live on disk: /var/lib/mysql



## Starting/Stopping/Restarting MySQL
----

Log into seattleclearinghouse.poly.edu as root or run the following commands as sudo to start/stop/restart mysql:

```
$ /etc/init.d/mysql start
$ /etc/init.d/mysql stop
$ /etc/init.d/mysql restart
```



## Making sure that MySQL is running
----

To test if MySQL is running, run the following command and make sure that you can see /usr/sbin/mysqld in the process list:

{{{
$ ps auwx | grep mysqld | grep -v grep