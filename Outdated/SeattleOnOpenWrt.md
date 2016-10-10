# Open Wrt on Seattle

[OpenWrt](https://openwrt.org/) is a lightweight Linux System for embedded devices such as routers. This article shows how to install and run Seattle on Open Wrt using the current Linux Seattle Installer.




 




## Preparation
The following manual was tested on a "TP-Link TL-WR1043ND" running "Open Wrt Attitude Adjustment 12.09 rc1". The Open Wrt web-site provides a [ List of supported hardware](http://wiki.openwrt.org/toh/start) with detailed installation instructions for various router and non router models. After the installation the device can be accessed via telnet (user=root, password=""). To use ssh you have to change the password first.
Due to the sparse built-in storage on the test device Python and Seattle were installed on a USB pen drive. This requires some drivers to be installed:
```
opkg install kmod-usb-storage
opkg install kmod-fs-ext4
opkg install block-mount
mkdir /mnt/key
```
Additionally ```/etc/fstab``` needs to be modified in order to automount the pen drive if Seattle should be started automatically on system startup:
```
config 'mount'
  option 'target' '/mnt/key'
  option 'device' '/dev/sda1'
  option 'fstype' 'ext4'
  option 'options' 'rw,sync'
  option 'enabled' '1'
  option 'enabled_fsck' '0'
```
Open Wrt's packackemanger [opkg](http://wiki.openwrt.org/doc/techref/opkg) can be configured to install packages on an external device. The following command installs Python 2.6 on a previously mounted usb pen drive. Python 2.6 is preferred over Python 2.7 because of a [bug](http://bugs.python.org/issue5099) in 2.7 that causes Seattle's Unit Tests to fail.
```
echo ``dest usb /mnt/key'' >> /etc/opkg.conf

opkg -dest usb install libpthread, zlib, libffi
cd /mnt/key
wget http://downloads.openwrt.org/backfire/10.03.1/ar71xx/packages/python-mini_2.6.4-3_ar71xx.ipk
wget http://downloads.openwrt.org/backfire/10.03.1/ar71xx/packages/python_2.6.4-3_ar71xx.ipk
opkg -dest usb install python-mini_2.6.4-3_ar71xx.ipk 
opkg -dest usb install python_2.6.4-3_ar71xx.ipk 

ln -s /mnt/key /opt

export PATH=$PATH:/opt/usr/bin:/opt/usr/sbin
export LD_LIBRARY_PATH=/opt/lib:/opt/usr/lib

opkg install ldconfig
echo "/opt/usr/lib" > /etc/ld.so.conf
ldfconfig 
```

## Installation
Actually the Linux Seattle Installer already installs Seattle on Open Wrt without any code modification. There are some complaints though. Two of them can be ignored. First, the installer unsuccessfully greps for a line in ```/proc/cpuinfo``` and therefore fails the cpu resource benchmark. And second, there is a warning that Seattle was not properly started even though it was (#1195). One problem that remains is that Seattle won't start automatically on system startup (#1194). There is not necessarily a complaint about this in the installation output. An alternative to start Seattle on boot is to use an init.d script, e.g. ```/etc/init.d/seattle```: 
```/bin/sh /etc/rc.common
 
START=99  

start() {
	export PATH=$PATH:/opt/usr/bin:/opt/usr/sbin
	export LD_LIBRARY_PATH=/opt/lib:/opt/usr/lib
	sh /mnt/key/seattle/start_seattle.sh
}
```
The start variable defines when the script is executed, relatively to the other init scripts. If Python or Seattle were installed on an external USB pen drive, this value has to be higher than the ```fstab``` init script. Also, the path has to be added before calling the starter. The following commands enable the init script:

```
chmod +x /etc/init.d/seattle
/etc/init.d/seattle enable
```

## Usage and Unit Test
For routers with restricted computational resources like the used test device, the code evaluation time in ```safe.py``` has to be given a higher value to avoid safety evaluation timeout. 
Nevertheless, there are still some unit tests that fail for unknown reasons, so Open Wrt on Seattle is definitely work in progress.