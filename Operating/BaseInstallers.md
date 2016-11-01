# Building Base Installers

Explains how to go about building the base installers (everything you need to distribute the program except custom VM information).

__NOTE:__ In order to build the Windows GUI installer, NSIS must be properly installed and configured on the system building the base installers. Click [here](https://github.com/SeattleTestbed/docs/blob/master/Operating/NsisSystemSetup.md) for quick detailed instructions on how to do this.

## Sample Usage
Running from `trunk/dist` directory: 

```
python make_base_installers.py at .. updaterkeys/updater.publickey updaterkeys/updater.privatekey outputdir [version]
```

## Step by Step
 1. Make sure you are operating on a Linux system.
 1. Choose an output folder for the base installers. Note: If there are already base installers of the same names in this folder, they will be overwritten without warning. A common directory would be `/var/www/dist/` (The dist folder doesn't exist and must be created.)
 1. Checkout the seattle trunk from svn.

    ```
    svn co http://seattle.poly.edu/svn/seattle/trunk
    ```
 1. If a pair of public key and private key doesn't exist for the updater then the following steps must be followed.
   1. Create a temporary folder.
   1. Navigate to the trunk/ folder.
   1. Run the command:

      ```python
      python preparetest.py TEMP_FOLDER
      ```
      (where the temp folder is the folder created in step 1)
   1. Navigate to the TEMP_FOLDER.
   1. Run the command:
    
      ```python
      python generatekey.py NAME_OF_YOUR_PUBKEY_PRIV_KEY
      ```
      An example would be:

      ```python
      python generatekey.py softwareupdater_key
      ```
   1. You can copy these two files over to where you want to store the keys. You can delete the `TEMP_FOLDER` and all its contents at this point if you want.
   1. Navigate to the `trunk/nodemanager` directory.
   1. Edit the `nmmain.py` file and change the global variable `version` to whatever version you want to call it.
   1. Navigate to the `trunk/dist` directory.
   1. Run the program (`make_base_installers.py`) with the following arguments:
     - Various flags that will modify the behavior of the program. Include "m" to create a Mac installer, "l" to create a Linux installer, "w" to create a Windows installer, "i" to create a Windows Mobile installer, "a" to create installers for all supported Operating Systems, and "t" (optional) to include the test cases with the installers. Example: "mlt" will build Mac and Linux installers with test cases.
     - The path to trunk; for example, ".." if you are running from the dist directory.
     - The path to the public key that the installation will eventually use to communicate with the software updater.
     - The path to the private key that the installation will eventually use to communicate with the software updater.
     - The path to the output directory that you wanted any created installers to end up in.
     - (Optional) The version of the installer which will be included in the installer name.
      Most likely you will run a command like this:
      
        ```python
        python make_base_installers.py a .. DIR_OF_UPDATER_KEYS/softwareupdater_key.publickey DIR_OF_UPDATER_KEYS/softwareupdater_key.privatekey output/dir [current_version_of_seattle]
        ```
     - This would have created the several installers for the different operating systems.
     - To remove cached versions of user-build installers from the Custominstallerbuilder, run `manage.py cleaninstallers` from the Custominstallerbuilder's Django project directory.
     - If you are planning on running a version of Seattle Clearinghouse as well, then you need to go through a few more extra steps. Some extra installers need to be created from the ones we just created.
     - Run the following set of commands:
      
      ```
      sudo chown test_user.dev seattle_0.1_test_version*
      sudo -u test_user ln -s -f seattle_0.1_test_version_linux.tgz seattle_linux.tgz
      sudo -u test_user ln -s -f seattle_0.1_test_version_mac.tgz seattle_mac.tgz
      sudo -u test_user ln -s -f seattle_0.1_test_version_win.zip seattle_win.zip
      ```
      Assuming that the version of seattle is ```0.1_test_version``` and you are running under the user ```test_user```, you should have the following files in your dir: ```seattle_0.1_test_version_linux.tgz```, ```seattle_0.1_test_version_mac.tgz```, ```seattle_0.1_test_version_winmob.zip```, ```seattle_0.1_test_version_win.zip```


## Using the base installers to test your code
You might often want to package up the code nicely so that you can easily test the current contents of your working directories on various systems. In this case, you might not care very much about the keys for the software updater or the VM information. If this is true, then you can quickly and easily build installers by navigating to trunk/dist and running the following: 

```python
python make_base_installers.py at .. updater_keys/updater.publickey updater_keys/updater.privatekey output/dir
```

Before running the installer on any system, you will want to first run ```python nminit.py``` from inside the install directory. This will generate some sample VM information.