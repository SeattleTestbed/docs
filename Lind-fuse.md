# Installing Lind-FUSE

This document describes the steps you'll need to follow to mount the Lind POSIX file system on a normal machine.   This will require the installation of FUSE and its Python bindings as well as the code for Lind.   In the end, the Lind code (written in Repy V2) will be called to serve as a file system.



## Install FUSE


You need to have python-fuse installed to use lind fuse.  Right now there is not a lind-fuse installer.   The mechanism to install FUSE depends on your OS.


### Linux


First try to install it using your package manager.   For example, on Ubuntu use the following command:

```sh
$ sudo apt-get install python-fuse
```

(On RedHat / Fedora, you'll need to use ```yum``` instead.   On OpenSuSE, you'll need to use ```yast```.)


If none of these work, try to download the tarball at the following link instead:   http://pypi.python.org/pypi/fuse-python/

If you don't use the package manager, to install the package:
```sh
$ tar zxvf fuse-python-0.2.tar.gz
$ cd fuse-python-0.2
$ sudo python setup.py install
```


To check if you have fuse:
```sh
$ ls -l /dev/fuse
```

### Mac instructions (untested)


If you are using a Mac you can try installing [MacFuse](http://code.google.com/p/macfuse/).   Then follow the Linux instructions above where it mentions to download the tarball and make fuse-python directly.



## Load the Appropriate Seattle code

You will need to get the nacl_repy branch of Seattle from SVN.   

```sh
$ svn co https://seattle.poly.edu/svn/seattle/branches/nacl_repy
```

Once that happens, run the ```preparetest.py``` script to copy the files into a directory of your choice (existing files there will be removed).   For example, to use ~/test-fuse do the following:

```sh
$ cd nacl_repy
$ mkdir ~/test-fuse
$ python preparetest.py -t ~/test-fuse
```


## Use

To use lind-fuse, you can simply mount a file system, and perform operations on it. Then unmount it.  Some operations are not currently supported (such as df)

### Example

```sh
$ cd /tmp
$ mkdir /tmp/lind-fuse-mountpoint   # make an empty directory
$ python ~/test-fuse/lind_fuse.py -f /tmp/lind-fuse-mountpoint & # given the mountpoint you just made, mount a Lind-fuse filesystem into it. '&' will make it run in background.
$ cd lind-fuse-mountpoint   # now try it out
$ ls
$ cp -r /var/log .
$ ls
$ cd ..  # when you are done
$ fusermount -u lind-fuse-mountpoint  # un-mount the file system.
```

This should work as any user (not just root).

The lind file system backing file used (or created) by the system will be whatever is in the local directory.


### Development

The core Lind-fuse files are:

 * lind-fuse.py: the driver which all the filesystem calls are sent to
 * test_fuse.sh: a small tester for the file system
 * lind_fs_calls.py: the implementation of the file system calls
 * lind_fs_constants.py: some useful file system related constants


lind fuse uses the python-fuse interface.  The code is very simple. Two classes, one which handles filesystem related system calls, and the other which does file related system calls.  To debug what is going on, you can run lind-fuse in the foreground, so you can see its output:

```sh
$ python lind_fuse.py mountpoint -f -v
```

Output will come out in this shell. Now go to another and do things in mountpoint.

## Limitations

Many system calls are not implented in lind-fuse.  Most of the basic ones related to file directory creation and read/write work though.  More could be added easily.