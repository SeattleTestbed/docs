# Setup NSIS on Linux System
''Note:'' These instructions were adapted from the detailed page http://www.xdevsoftware.com/blog/post/How-to-Install-the-Nullsoft-Installer-NSIS-on-Linux-.aspx

Because the NSIS program makensis.exe, which generates Windows GUI executable (.exe) installer, is meant to be run on Windows systems, below are instructions on how to generate the makensis.exe program so that our Windows GUI installer can be generated on a Linux system instead.

## System Requirements
The following tools must be installed:
 * Wine must be installed in order to run the final makensis.exe program
 * Scons (similar to 'make') -- usually available through apt-get
 * A 'C' compiler (gcc and g++ packages)
 * Python

[[Br]]

## Instructions

 1. **Download the following two packages from SourceForge.net: http://sourceforge.net/projects/nsis/files/ for the latest ''VERSION'' of NSIS**
   1. nsis-''VERSION''-src.tar.bz2 (NSIS source code)
   1. nsis-''VERSION''.zip (zip package)
''As of the writing of this wiki, the current VERSION is 2.46, so the needed two packages would be **nsis-2.46-src.tar.bz2** and **nsis-2.46.zip**''

 2. **Create a new directory called 'nsis' in which these two packages will live.**  Make sure that this directory exists somewhere where anyone who needs to build the base installers will have permission to access it.  Move the two NSIS packages from SourceForge.net into this 'nsis' directory.

 3. **Move to the new directory, and extract the two packages:**
   a. ''tar -jxvf nsis-2.46-src.tar.bz2''
   a. ''unzip nsis-2.46.zip''
''Extracting these two files will have created two subdirectories within the 'nsis' directory: 'nsis-2.46-src' and 'nsis-2.46' ''

 4. **Build the NSIS compiler for Linux.** This process will build the makensis.exe Windows executable file used to generate the Windows GUI installer. **From within the 'nsis/nsis-2.46-src' directory,** issue the following command:
''scons SKIPSTUBS=all SKIPPLUGINS=all SKIPUTILS=all SKIPMISC=all NSIS_CONFIG_CONST_DATA=no PREFIX=/full/path/to/nsis/nsis-2.46 install-compiler''
[[Br]]
**''NOTE 1:'' DO NOT FORGET TO INCLUDE THE ''install-compiler'' OPTION AT THE END OF THE scons COMMAND! **
[[Br]]
**''NOTE 2:'' Make sure the full path given to the PREFIX option goes to nsis/nsis-2.46 and NOT to nsis/nsis-2.46-src**
[[Br]]
**''NOTE 3:**'' If you receive the error **sh: o: command not found** while scons is running, then you do not have the 'C' compiler packages installed (gcc and g++).

 5. **Make the new makensis.exe file executable.** Navigate to the 'nsis/nsis-2.46' directory, and it should contain the ''makensis.exe'' file just created by the scons command above.  To make the ''makensis.exe'' file executable, **run the command: ''chmod a+x makensis.exe**''
**''NOTE:**'' If the makensis.exe file does NOT appear within the ''nsis-2.46'' directory, then there was a problem with the scons command above.

 6. **Finished! ** At this point, you should be done setting up NSIS in order to build the Windows GUI installer.