# Build Instructions

This page guides readers through building the components of 
[Seattle Testbed](https://github.com/SeattleTestbed).  The Seattle Testbed 
is comprised of a dozen, or so, interdependent sub-components that may be 
individually built, run, and tested.  Specifically, this instructional guide 
covers the `initialize.py` and `build.py` scripts that are utilized by all 
of the Seattle Testbed components; these two build scripts may be used to 
fetch each component's dependencies, and to build the component and its unit 
tests.  There are sections explaining how to build components; how to build 
and run a component's unit tests; the different use cases for the build 
scripts; how contributors will typically develop and contribute source code 
while using the build scripts; and how the build scripts themselves work. 
The guide begins by discussing the software prerequisites of the 
Seattle Testbed.

-----

## Prerequisites
Before you begin, make sure that you have the following pieces of software 
on your computer:
* [Python 2.7](https://www.python.org/downloads/).
* [Git 1.7](http://www.git-scm.com/download) (or later)

Many operating systems (such as Linux and Mac OS X) ship with these installed. 
On Windows, you will usually need to install Python and Git.

*Note: Please double-check your Python version! We don't support Python 3 
at the moment.*


## Building RepyV2
This section describes how to build RepyV2, SeattleTestbed's sandbox,
from its source repository on [GitHub](https://github.com/SeattleTestbed),
using the command line.
We'll use a Unix-like system throughout our examples. Windows users
should use Windows PowerShell or Command Prompt.

*Note: These build instructions apply similarly to all other SeattleTestbed
components.*


1. Clone the RepyV2 repository from [SeattleTestbed's GitHub](https://github.com/SeattleTestbed).

```sh
$ git clone https://github.com/SeattleTestbed/repy_v2
```
If you usually use `SSH` instead of `https` to clone your git repos, you can do:
```sh
$ git clone git@github.com:SeattleTestbed/repy_v2.git
```

(If you want to clone a different repository, replace `repy_v2` with
the appropriate repository name.)


2. This yields a folder named like the repository you cloned. Inside of 
it, there is a `scripts/` folder which in turn contains a script called 
`initialize.py` to fetch the dependencies of this component. Continuing 
with `repy_v2` for this concrete walkthrough:

```sh
$ cd repy_v2/scripts
$ python initialize.py
```

`initialize.py` Git-clones the dependent repositories into `DEPENDENCIES` 
directory which will be created as a sub-directory inside your main 
repository. It takes its instructions from `config_initialize.txt` to 
fetch the dependencies.

3. To build a runnable component from the source dependencies, run the 
`scripts/build.py` script. You may supply it an optional target folder for 
the build (which must be created first). Name this folder as you like.
```sh
$ mkdir TARGET_FOLDER
$ python build.py TARGET_FOLDER
```

If you don't setup a target directory, `build.py` will itself create a 
target folder named `RUNNABLE` which will be a sub-directory inside the 
component's main repository, e.g. `repy_v2/RUNNABLE`.

`build.py` will copy all the files necessary to build the particular Seattle 
Component into the target directory. It will indirectly call 
`../DEPENDENCIES/common/build_component.py` and make use of `config_build.txt` 
in order to fetch the list of files and directories to copy to target.


*Done!* Your target folder now contains a runnable version of the
RepyV2 sandbox (or other component you chose)!


## Building and Running Unit Tests
When making changes to the code (or build scripts!) you will want to ensure 
that the change does not have side effects or breaks functionality that had 
been working before. In order to ensure this, most components are *testable* 
and come with a set of *unit tests*. These components have a `tests` or 
`test` directory within their repository.

The steps of the previous section intrinsically downloaded the required 
unit test files. You just need to run the build script again to create a 
testable build. Use the `-t` command line option to indicate you want 
the test files to be included. Again, specifying a target directory is optional!
```sh
$ mkdir TEST_TARGET_DIR
$ cd COMPONENT/scripts
$ python build.py -t TEST_TARGET_DIR
```

Then, change to the test target directory (which will either be `RUNNABLE` 
or your `TEST_TARGET_DIR`), and start the unit tests:
```sh
$ cd TEST_TARGET_DIR
$ python utf.py -a
```

The unit test framework prints out the test name and result (plus debugging 
information if available), e.g.:
```
	Running: ut_nm_addfiletovessel.r2py                         [ PASS ]
```


## How The Build Process Works

The Seattle build procedure makes use of three scripts, `initialize.py`, 
`build.py` and `build_component.py`, and two sets of configuration 
instructions, `config_initialize.txt` and `config_build.txt`.

`config_initialize.txt` contains links to the dependent repositories of a 
component.  `initialize.py` Git-clones each link it reads from 
`config_initialize.txt` and saves the cloned repositories to particular 
directories, which are also specified in `config_initialize.txt`.  Usually, 
`config_initialize.txt` contains Github links to the main repositories, 
[github/SeattleTestbed](https://github.com/SeattleTestbed), but contributors 
often modify these links to point to other repositories during development. 
Note that links may include branch or commit specifiers so as to enable release 
management ("tagging"). Entries are of form

```
ADDRESS_OF_REPOSITORY [``-b'' BRANCH_IDENTIFIER] PATH_TO_CLONE_INTO
```

`config_build.txt` provides `build_component.py` with the names and paths of 
necessary files that are to be copied over from the cloned repos to the target 
directory to build the required Seattle component. Entries are of form

```
SOURCE_PATH/FILENAME_OR_GLOB [DESTINATION_PATH_BELOW_TARGET_DIR]
``test'' SOURCE_PATH/FILENAME_OR_GLOB [DESTINATION_PATH_BELOW_TARGET_DIR]
```

`build.py` is a wrapper-script that automates the running of 
`build_component.py` from inside the `scripts/` directory of a component, so 
that users don't need to leave the scripts directory in order to run 
`build.py`.

A sample `config_initialize.txt` looks like this:
```
# This is a sample config showing the different allowed forms of entries.
# (And yes, this is how comment lines can be added!)
https://github.com/SeattleTestbed/repy_v2 ../DEPENDENCIES/repy_v2
https://github.com/aaaaalbert/seash.git -b sync-with-affix-alpha-release ../DEPENDENCIES/seash
```

Here is the corresponding ```config_build.txt```:
```
# Build file for the Repy runtime that the custominstallerbuilder requires. 
./*
DEPENDENCIES/repy_v2/*
DEPENDENCIES/seash/* seash_subdir/

# Tests
test ./tests/*
```


One can add comments to the configuration files by prefixing lines with `#`. 

Within `config_build.txt`, lines starting with `test ` specify the test files 
(or file patterns) that are copied over to the target directory if the build 
script is called in test mode (`build.py -t target_dir`). 


The required directory layout for a repository supporting this build method 
is this:

```
the_component/     # Repo base directory, includes code etc.
the_component/scripts/
the_component/scripts/initialize.py
the_component/scripts/build.py
the_component/scripts/config_initialize.txt
the_component/scripts/config_build.txt
the_component/DEPENDENCIES/common/build_component.py
```


*Note:* `build_component.py` is not part of `scripts/`. Running 
`initialize.py` clones the dependent repositories into 
`the_component/DEPENDENCIES/`, and one of these cloned dependencies is 
`common` which contains `build_component.py`. Users don't need to manually run 
`build_component.py` script. The script `scripts/build.py` indirectly runs 
`build_component.py` and takes care of it.



## Use Cases for the Build Scripts

### End Users

End users do not normally modify nor contribute source code to 
[SeattleTestbed](https://github.com/seattletestbed), but instead build and 
run specific `SeattleTestbed` components.  For this use case, the build 
procedure for end users is straightforward and matches the procedure outlined 
in the previous section ("How the Build Process Works"):

1. `git clone` a [SeattleTestbed](https://github.com/seattletestbed) repository

2. cd `scripts/`

3. Run `python initialize.py` to fetch the cloned repository's dependencies 
(as indicated in `config_initialize.txt`).

4. Run `python build.py`, supplying an optional destination directory. By 
default, modules that are built are saved to `../RUNNABLE`

End users may then navigate to the `../RUNNABLE` directory and execute a 
specific program. For example:

```
$ cd ../RUNNABLE/
$ python seash.py
Enabled modules:  

 !> 
```


### Developers

Github developers typically fork (or create a new branch on 
[SeattleTestbed](https://github.com/SeattleTestbed) if they are a member of 
`SeattleTestbed`) repositories and make pull requests to contribute source 
code.  There are multiple approaches developers may follow to build and test 
a component that they have modified.  Developers may either (1) build and 
test a buildable/non-buildable repository that they have modified, or (2) build 
and test a component that contains a developer-modified dependency (e.g., build 
and test `repy_v2` when the developer has modified `seattlelib_v2`).

Approach (1) is almost identical to the end-user scenario, but developers 
`git clone` their modified repository, rather than one of the 
`SeattleTestbed` repositories.

Modified dependencies in approach (2) can be built and tested in two ways: 
(A) The modified dependency is available on Github and is specified in 
`config_initialize.txt` by the developer, or (B) the modified dependency is 
available locally and is manually added to a "DEPENDENCIES" subdirectory of 
the component.

#### Approach A

1. `git clone` a [SeattleTestbed](https://github.com/seattletestbed) repository

2. cd `scripts/`

3. A "dependencies" entry in `config_initialize.txt` is edited so that it 
points to the developer's modified repository.  For example:
```
https://github.com/JohnSmith/seattlelib_v2 ../DEPENDENCIES/seattlelib_v2
https://github.com/SeattleTestbed/portability ../DEPENDENCIES/portability       
```

Notice that the first entry in the example above specifies 
`https://github.com/JohnSmith/seattlelib_v2`, which is the developer's 
modified repository.

4. Run `python initialize.py` to fetch the component's dependencies, including 
the developer's modified repository

5. Run `python build.py`, supplying an optional destination directory. By 
default, modules that are built are saved to `../RUNNABLE`

The developer may test the component by running its unit tests 
(`python build.py -t` is required to build testable components) or running 
the built program and verifying functionality.


#### Approach B

1. `git clone` a [SeattleTestbed](https://github.com/seattletestbed) repository

2. The developer creates a subdirectory named `DEPENDENCIES` under the 
cloned repository.

3. The developer manually copies their modified component to the 
`DEPENDENCIES` subdirectory.

4. cd `scripts/`

5. `python initialize.py -s` is executed to fetch the repository's 
dependencies and skip any existing subdir of `DEPENDENCIES`. This will usually 
be the developer's modified subdirectory, but actually **any** subdir, no 
matter its contents, will be skipped if its name matches a repo's!

6. `python build.py`, supplying an optional target directory instead of the 
default `../RUNNABLE`

The developer may test the component by running its unit tests 
(`python build.py -t` is required to build testable components) or running the 
built program and verifying functionality.

NOTE: Using the `-s` (skip mode) option with `python initialize.py` is 
dangerous because it doesn't check whether the existing dependencies are 
fully-working copies (e.g., repository not checked out completely due to user 
cancelling the process) and skipping incomplete dependencies might mask errors 
and lead to build/runtime errors.

## `SeattleTestbed` Development and the Build Scripts
Contributors have two methods for testing and building the source code changes 
that they intend to contribute to SeattleTestbed repositories:

1. Edit module and test files in the root directory of the component.  That is, 
the files that are tracked by Git are directly edited by the contributor, and 
`scripts/build.py' is repeatedly executed after each edit so that testing and 
verification of behavior can be conducted.  Edited files may then be added, 
committed, and a pull request issued to https://github.com/SeattleTestbed/ 
from the Git-tracked, root directory.

2. For quick & convenient editing and testing of a component's modules, the 
files that are built in the target directory (RUNNABLE by default) may be 
directly modified.  For example, a module in RUNNABLE can be updated and 
immediately tested from the same directory.  However, files that are edited 
in the target directory are not tracked by Git.  One shortcoming of this 
method is the manual task of moving or copying over changes to the Git-tracked 
directory; this approach may unfortunately lead to edits that are accidentally 
excluded from pull requests because edits are not eventually copied over to 
the Git-tracked versions of modified modules.
