1. <a href="#Intro">Introduction</a>
1. <a href="#Setup">Setup</a>
1. <a href="#Config">Configuration</a>
1.  - <a href="#ConfigTravis">Configuration for Travis</a>
1.  - <a href="#ConfigAppVeyor">Configuration for AppVeyor</a>
1. <a href="#Workflow">Workflow</a>

<a name="Intro" />
## Introduction - Continuous Integration
Continuous Integration is the process of automating the build and unit testing of the various projects for The Seattle Test Bed. Applications that The Seattle Test Bed will take advantage of are Travis-CI and Appveyor, both of which maintain a variety of operating systems (Linux and Mac OSX for Travis-CI and Windows for Appveyor) with flexible installation of applications, such as python. 

<a name="Setup" />
## Setup For Continuous Integration
Given a GitHub repo for which you want to enable continuous integration using AppVeyor, Travis-CI, or both:

### Setting Up Travis-CI
1.	Go to [Travis-CI](https://travis-ci.org) and login with your GitHub User ID and Password
1.	In Travis: Press the Sync button to sync with GitHub
1.	In Travis: Switch on the repos on the Travis-CI home page which you want to build and test
1.	In Travis: Press the Sync button
1.	Write .travis.yml. In the absence of a .travis.yml file in your repo, Travis-CI will simply run a build with default settings, for every commit, whenever there is a push to the repo. The defaults are unlikely to be of use to us, so you will have to write a .travis.yml file (if it is not present already) in your repo. <a href="#ConfigTravis">See section below</a> for sample .travis.yml file. The [general Travis-CI yml reference is here](https://docs.travis-ci.com/user/customizing-the-build/).
1.	Commit & push the .travis.yml file to your repo and Travis-CI should detect the new commit and start a build for it within a few minutes. At travis-ci.org/[user]/[repo]/builds, you should see the build in the list along with the results.
1.	In GitHub: Modify the readme file of the fork to include the badge from Travis-CI. See [here for Travis-CI badges](https://docs.travis-ci.com/user/status-images/).

### Setting Up AppVeyor:
1.	Go to [AppVeyor](https://ci.appveyor.com) and login with your GitHub User ID and Password
1.	In Appveyor: Click on New Project and select the desired repo from the list of your repos available on GitHub.
1.	Write appveyor.yml. In the absence of an appveyor.yml file in your repo, AppVeyor will simply run a build with default settings, for every commit, whenever there is a push to the repo. The defaults are unlikely to be of use to us, so you will have to write an appveyor.yml file (if it is not present already) in your repo. The [general AppVeyor reference for appveyor.yml is here](https://www.appveyor.com/docs/appveyor-yml).
1.	Commit & push the appveyor.yml file to your repo and AppVeyor should detect the new commit and start a build for it within a few minutes. At ci.appveyor.com/project/[user]/[repo], you should see the build in the list along with the results.
1.	In GitHub: Modify the readme file of the fork to include the badge from AppVeyor. See [here for AppVeyor badges](http://www.appveyor.com/docs/status-badges).



<a name="Workflow" />
## Working with Continuous Integration
1.	Starting builds: whenever a commit is pushed to the repo that AppVeyor or Travis are connected to, a build will automatically be started. AppVeyor also allows you to manually start builds from the project page with the "New Build" or "Rebuild commit" buttons.
1.	Verify the build status badges in a few minutes and click on them if they are showing as failed (Note: Badge in readme is optional).
1.	If build is shown as passing, submit pull request to merge your code to main branch *((Not sure what the intention is here - unless we're writing instructions for contributors on how to get code into Seattle projects... but that's not here. Just leaving it for now....))*


####Tips:
- To avoid a specific commit automatically triggering a new build, include "[ci skip]" in the commit message.


<a name="Config" />
## Configuring Continuous Integration
<a name="ConfigTravis" />
### Configuring Travis-CI: Writing .travis.yml
Travis's default configuration is unlikely to provide meaningful results. A .travis.yml file is required. Here's a basic sample for any Seattle project that includes buildscripts. The example below will run the unit testing framework on one version of python - 2.7 - on a Linux system on a Travis vm after performing basic updates (using apt-get).

```
matrix:                         # Matrix-include is essential to specify specific VM entries
  include:                              
    - language: python			# Language to initiate linux VM
      python: '2.7'				# Type of python to use		
      os: linux					# The OS of the VM
      install:					# tool installation 
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
For example, in the “scripts:” (Travis-CI) or “test_script:” (Appveyor) block of the YML file unit test can run individually or with a module. 

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
Here's a basic sample for any Seattle project that includes buildscripts. The example below will run the unit testing framework on one version of python - 2.7 - on a windows 64 bit system on a Appveyor VM after performing basic OS installation

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
##### Appveyor: Multiple VMs / Environments
When adding multiple python version under the **enviroments - matrix** set or multiple windows bit architectures under **platforms** set Appveyor will perform the cartesian product, thus resulting in multiple VMs. The example below shows that the Appveyor will run 4 VMs in serial.

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
