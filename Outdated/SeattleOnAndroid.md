# Seattle on Android


**THIS PAGE IS OUT OF DATE!   PLEASE DOWNLOAD THE [SEATTLE ON ANDROID](https://play.google.com/store/apps/details?id=com.seattletestbed#?t=W251bGwsMSwxLDIxMiwiY29tLnNlYXR0bGV0ZXN0YmVkIl0.) APP IN THE ANDROID MARKETPLACE!!!**


This page discusses our port of Seattle to the Android platform. You will be able to download a native Android installer (APK) Real Soon Now from our clearinghouse web site. In the meantime, find instructions how to install Python, the Seattle runtime, and the Seattle Node Manager below.


----




[Our](http://cs.univie.ac.at/research/research-groups/future-communication/) device here is a ZTE Blade Android 2.3 ("Gingerbread") phone running [CyanogenMod](http://www.cyanogenmod.org/) 7.

----

## Overview
Here is a general outline of steps to be performed. You will get access to Python, Repy (Seattle's runtime), and the Seattle Node Manager, respectively.
 1. Set up [Python for Android (Py4A)](http://code.google.com/p/android-scripting/wiki/InstallingInterpreters).
 1. [wiki:RepoAccess Check out] the latest version of Seattle from SVN (r5656 and later should work): ```svn co https://seattle.poly.edu/svn/seattle/```
 1. Install Seattle on the command line. This won't give you autostart capabilities, though.

(If you want to work on the SeattleOnAndroid GUI (not discussed here), import the code in ```seattle/trunk/dist/android``` as an "existing Android project" from within Eclipse. Then just "run as" on the android emulator or your device.)

Quite a few command line settings on this page requires your device to be rooted, i.e., you need root privilege on your phone to run these settings. How to root a device largely depends on the phone, Android version, etc. Fortunately [CyanogenMod](http://www.cyanogenmod.org/) firmware is rooted by default.

PS: Terminal commands on Android are either the limited version of standard Linux, or even not implemented (when you use ```adb shell```, you can see all of the implemented commands in ```/system/bin```). There is an app called Busybox in Play store which has better implementation of many (but not all) commands. To use Busybox, your device needs to be rooted. 


## Setting up Python for Android

 1. On the home screen, press ''Menu''. Go to ''Settings > Applications'' and make sure ''Unknown Sources'' is checked. This is needed for installing non-Market APKs right after downloading them.
 1. Download the Python 2.6.2 interpreter for Android ([Py4A]) from [here](http://code.google.com/p/python-for-android/downloads/list=). Tap on the download notification to install. Congratulations! You can now run Python code from within the Py4A GUI, either using scripts from files or an interactive interpreter.
 1. Undo Step 1 for obvious security reasons.

### Python from shell

To get shell access to your device, run ```adb shell``` which comes within your android-sdk/platform-tools (the location may vary depending on your OS or other settings). [adb](http://developer.android.com/tools/help/adb.html) is Android debug bridge, which lets you communicate with a connected Android device or emulator instance. 

Shell access to the Python interpreter is tricky to add because the shell knows nothing about Python's paths yet. Depending on which shell you have, there are different routes to take from here. Be sure to adapt the actual paths to your device/installation.

For ```sh``` (which is the default shell also greeting you via [adb](http://developer.android.com/guide/developing/tools/adb.html)'s ```shell``` command), I don't know yet where it takes its run commands (.shrc) from. If you have [Jackpal's AndroidTerm2](https://github.com/jackpal/Android-Terminal-Emulator/wiki) installed, you could write an rc script and configure AndroidTerm to run it on startup: Press ''Menu'', go to ''Settings > Start command'' and enter /path/to/your/script.

For ```bash```, mount ```/system/etc``` writable by issuing ```mount -o rw,remount /system``` as the superuser (you need a rooted device here). Add the following lines to ```/system/etc/bash/bashrc``` (The last line puts the Python interpreter on your ```$PATH```, so you can type ```python``` to access it right away):

```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/data/com.googlecode.pythonforandroid/files/python/lib
export PYTHONPATH=/mnt/sdcard/com.googlecode.pythonforandroid/extras/python:/data/data/com.googlecode.pythonforandroid/files/python/lib/python2.6:/data/data/com.googlecode.pythonforandroid/files/python/lib/python2.6/lib-dynload
export PYTHONHOME=/data/data/com.googlecode.pythonforandroid/files/python
export TEMP=$TEMP:/mnt/sdcard/com.googlecode.pythonforandroid/extras/python/tmp/
export PATH=$PATH:/data/data/com.googlecode.pythonforandroid/files/python/bin
```

These lines are inspired by [this file in the Py4A repository](http://code.google.com/p/python-for-android/source/browse/python-build/standalone_python.sh).

<!--
Not all of their path names work on our phone. I'm not blaming the original authors -- pathnames are a botch in Android, everything shows up in multiple places (/etc == /system/etc and so on), and all of a sudden you find yourself on a device not supporting links (sdcard, its filesystem is VFAT) or mounted read-only but listed as temp directory.
-->


## Setting up Repy

Repy is the restricted version of Python Seattle supports. To install the Repy runtime environment, you need to prepare the required files beforehand:

 1. Check out ```trunk``` (>=r5656) from Seattle's SVN
 1. Create a directory for the files we will upload to the Android device, let's call it ```/target```.
 1. Inside ```trunk```, run ```python preparetest.py /target```.
 1. Download a restrictions file [attachment:restrictions.test:wiki:RepyTutorial such as this one] to ```/target```.
 1. Finally, upload the contents of ```/path/to/files``` to your Android device, e.g. using ```adb push /target /seattle/on/android/directory```.

If you want to allow Repy to collect data from your phone, you have to get a [Seattle Sensor](https://seattle.poly.edu/wiki/UsingSensors) running. [Here](https://play.google.com/store/apps/details?id=at.univie.sensorium) is one implementation that interfaces lots of sensors on your Android device, and makes values available in a GUI and programmatically over an XML-RPC interface.

Congrats, now you can run ```python repy.py restrictions.that_you_have your_script.repy``` from the command line! An example test script can be found [here](https://seattle.poly.edu/attachment/wiki/SeattleOnAndroid/test_script.repy). 



## Setting up the Seattle Node Manager

**This doesn't work at the moment. seattleinstaller.py is not in the list of files preparetests.py thinks are necessary.**

<!--
Before you can install the Seattle Node Manager, you need to tell the command-line installer which vessels of what size it should create, and who should be able to access them. For altruistic donations, use the ```vesselinfo``` file from [an installer package](https://seattleclearinghouse.poly.edu/download/flibble/). If you want to have ```seash``` access to your own device, use the [wiki:CustomInstallerBuilder]. Either way, push the ```vesselinfo``` file into the directory you created for Repy. Then,

 1. Run ```python seattleinstaller.py```. You might want to increase the percentage of resources donated using e.g. ```--percent 50```. On our phone, 10 percent of resources mean even [source:/trunk/repy/apps/allpairsping/allpairsping.repy allpairsping] needs to much RAM to run. The installer won't be able to configure Seattle for autostart.
 1. Run ```python nmmain.py```. It will take a while to register at the advertisement server.
 1. If you downloaded a customized installer that has your user key in the ```vesselinfo``` file, you can try to access your device using ```seash``` now.

Although the node manager is not registered to automatically start when the device boots, it can be run manually now. The software updater isn't started automatically either.
-->
-----