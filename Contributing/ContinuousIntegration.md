## Introduction
Seattle Testbed [components](https://seattle.poly.edu/wiki/BuildInstructions) can be built and tested automatically on multiple operating systems using different versions of Python. This document describes how to configure Travis-CI and AppVeyor, two continuous integration web tools, in order to perform automated building and unit testing.

## Configuration and Usage
Given a GitHub repo for which you want to enable continuous integration using Travis-CI and AppVeyor:

1. The config files (currently `appveyor.yml` and `.travis.yml`) should already be in your `fork/branch`. 
  - If not, make sure that your [fork is in sync](https://help.github.com/articles/syncing-a-fork/) with the original SeattleTestbed repo, and 
  - that your *`<feature>`* branch is in sync with your `master` branch *(Hint: `$ git merge master`)*.
  - If the config files still aren't there, refer to <a href="#sync-config">Sync config changes with SeattleTestbed repos</a>
1. Link your GitHub account with Travis-CI and Appveyor
  - **Travis-CI**
    1. Go to [Travis-CI Website](https://travis-ci.org) and sign in with your GitHub user-ID and password
    1. Authorize application to access your GitHub account
    1. Go to your profile page
    1. Flick on the repo switch for the repo you want to build and test
    1. Commit and push something to your repo, and
    1. go to `travis-ci.org/<GitHub-user>/<repo>/` to see build and test results
    1. *(optional) add [Travis-CI Build Status Badges](https://docs.travis-ci.com/user/status-images/) to your `README.md` file on GitHub*
  - **AppVeyor**
    1. Go to [AppVeyor Website](https://ci.appveyor.com) and log in with your GitHub developer account
    1. Authorize application to access your GitHub account
    1. Click on `NEW PROJECT`
    1. Authorize application to access your GitHub repositories 
    1. Add the repo you want to build and test
    1. Commit and push something to your repo or click `NEW BUILD` on the AppVeyor web interface, and
    1. go to `ci.appveyor.com/project/<GitHub-user>/<repo>/` to see your test and build results
    1. *(optional) add [AppVeyor Build Status Badges](http://www.appveyor.com/docs/status-badges) to your readme file on GitHub*

*Note: To avoid a specific commit automatically triggering building and testing, add ``[ci skip]'' to your commit message*

<a name="sync-config" />
## Sync config changes with SeattleTestbed repos
The CI configuration files are maintained at [SeattleTestbed/continuous-integration](https://github.com/SeattleTestbed/continuous-integration). Different ideas of distributing them across all SeattleTestbed components are discussed in SeattleTestbed/continuous-integration#1. If you want to change the files or add nur configs, please
 1. push the changes to said repo,
 1. use script `git_sync_configs.sh` to distribute files *(maybe you have to modify some hardcoded links/filenames)*,
 1. submit Pull Requests in all affected SeattleTestbed components

<a name="further" />
## Further Readings
*...are currently commented out to make the page less convoluted and they might disappear entirely at some point. If you want to read them now and in the browser click on the raw button on top.*

<!---
<a name="Workflow" />
## Working with Continuous Integration
1.  Starting builds: whenever a commit is pushed to the repo that AppVeyor or Travis are connected to, a build will automatically be started. AppVeyor also allows you to manually start builds from the project page with the "New Build" or "Rebuild commit" buttons.
1.  Verify the build status badges in a few minutes and click on them if they are showing as failed (Note: Badge in readme is optional).
1.  If build is shown as passing, submit pull request to merge your code to main branch *((Not sure what the intention is here - unless we're writing instructions for contributors on how to get code into Seattle projects... but that's not here. Just leaving it for now....))*


<a name="Config" />
## Configuring Continuous Integration
<a name="ConfigTravis" />
### Configuring Travis-CI: Writing .travis.yml
Travis's default configuration is unlikely to provide meaningful results. A .travis.yml file is required. Here's a basic sample for any Seattle project that includes buildscripts. The example below will run the unit testing framework on one version of python - 2.7 - on a Linux system on a Travis vm after performing basic updates (using apt-get).

```
matrix:                         # Matrix-include is essential to specify specific VM entries
  include:
    - language: python      # Language to initiate linux VM
      python: '2.7'       # Type of python to use   
      os: linux         # The OS of the VM
      install:          # tool installation 
        - sudo apt-get update
script:
  - python --version
  - cd ./scripts
  - python initialize.py
  - python build.py -t
  - cd ../RUNNABLE
  - python utf.py -a
```

The "install:" block for every Linux VM can install any tools required for running the tests. Above, we simply perform an update on packages installed on the Travis VM, but one could install custom tools, perform basic setup - whatever is needed for the tests.


The "scripts:" block at the end will run for every configuration listed in the matrix above. Generally, you can run whatever you like in the scripts section at the bottom of your .travis.yml file, to be executed during the testing phase of the build. **Seattle employs [a unit test framework that is described in detail here](https://seattle.poly.edu/wiki/BuildInstructions).** Here are just a few examples:
For example, in the “scripts:” (Travis-CI) or “test_script:” (AppVeyor) block of the YML file unit test can run individually or with a module. 

```
script:
  - python utf.py –a # run all tests
```
```
script:
  - python utf.py –f filename
```
```
script:
  - python utf.py –m modulename
```


##### Travis-CI: Multiple VMs / Environments
Adding sections like the following under the **matrix** and **include** directives will cause the scripts to be run on addition VMs for each section with the specified configuration.
```
    - language: python
      python: '2.6'
      os: linux
      install:
        - sudo apt-get update
```

##### Travis-CI: Testing on OS X
Testing on OS X is quit similar to the Linux, though not all tools may be available on OS X and needs to be installed once the VM is created. The code below shows that python is installed through pyenv and adds the installed version of python to the default path. 
```
matrix:
  include:
    - language: objective-c
      os: osx
      install:
          - if [[ "$(uname -s)" == 'Darwin' ]]; then
             pyenv install 2.6.9;
             pyenv global 2.6.9;
            fi
          - export PYENV_ROOT="${HOME}/.pyenv"
          - if [ -d "${PYENV_ROOT}" ]; then
             export PATH="${PYENV_ROOT}/bin:${PATH}";
             eval "$(pyenv init -)";
            fi
script:
  - python --version
  - cd ./scripts
  - python initialize.py
  - python build.py -t
  - cd ../RUNNABLE
  - python utf.py -a
```
###### Additional Refrences: Testing on OS X
- [Travis docs for multiple OS setups](https://docs.travis-ci.com/user/multi-os/)
- [Travis docs for OS X environments](https://docs.travis-ci.com/user/osx-ci-environment/)



<a name="ConfigAppVeyor" />
### Configuring AppVeyor: Writing appveyor.yml
Here's a basic sample for any Seattle project that includes buildscripts. The example below will run the unit testing framework on one version of python - 2.7 - on a windows 64 bit system on a AppVeyor VM after performing basic OS installation

```
build: false                #defaults to the cloned repository

environment:
  matrix:
    - PYTHON: "C:/Python27"

platform:
- x64

test_script:
  - cd scripts
  - python initialize.py
  - python build.py -t
  - cd ../RUNNABLE
  - python utf.py -a
```
##### AppVeyor: Multiple VMs / Environments
When adding multiple python version under the **enviroments - matrix** set or multiple windows bit architectures under **platforms** set AppVeyor will perform the cartesian product, thus resulting in multiple VMs. The example below shows that the AppVeyor will run 4 VMs in serial.

```
build: false

environment:
  matrix:
    - PYTHON: "C:/Python26"
    - PYTHON: "C:/Python27"

platform:
- x86
- x64

test_script:
  - cd scripts
  - python initialize.py
  - python build.py -t
  - cd ../RUNNABLE
  - python utf.py -a

```
-->
