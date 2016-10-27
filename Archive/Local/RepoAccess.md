# Github and Git
Seattle's code base and ticket system are hosted on [Github](https://github.com/).
Github is a web application that can be used for collaboration, code review, and code management.
It is popularly used in open source projects and by distributed developers.  Contributions to
Seattle  are expected to be made using [pull requests](https://help.github.com/articles/using-pull-requests)
to repositories of the [SeattleTestbed](https://github.com/SeattleTestbed) organization.

Git is a free and open source distributed [VCS](http://en.wikipedia.org/wiki/Version_control_system)
(Version Control System).  A VCS helps manage changes made to files.  Users can run Git on their local
computers and upload changes to remote repositories and files hosted on Github.  [SeattleTestbed](https://github.com/SeattleTestbed)
contributors can edit files locally, upload their changes to Github, and then initiate a pull request. The following document
covers the basics of using Git and submitting a pull request to one of Seattle's Github repositories.





## Git Installation
Github provides platform-specific installers for Mac and Windows users.  Installation instructions
are provided in the links below for each supported platform.

[Mac](https://mac.github.com)

[Windows](https://windows.github.com)

[Linux](http://git-scm.com/download/linux)


Linux users may install Git using their distribution's package manager.
Installation commands for many Linux distributions are available at [Linux](http://git-scm.com/download/linux).

For example, Debian-based Linux distributions can use [APT](http://en.wikipedia.org/wiki/Advanced_Packaging_Tool) (Advanced Packaging Tool).
```
$ sudo apt-get install git
```


## Configure Git User Information

After installing Git, the next step is for the user to configure his/her author information (username and email address) so that Git will correctly log the author of a commit. 


To configure Git author information, open the Terminal and type **git config --global user.name "user's name"**, which will allow you to configure Git on your local machine. Each repository you create will use the same user (author) configuration if you use the global flag (as in the provided example). 

```
$ git config --global user.name "John Smith"

$ git config --global user.email "john.smith@example.com"
```

You can check your user information by typing the following command:

```
$ git config --list
```


## Configure Github User Account
Before a pull request can be submitted to a [SeattleTestbed](https://github.com/SeattleTestbed)
repository, a user account (free) must be created on Github.  This user account is also needed to create
new repositories and fork ones that already exist on Github.


A Github user account can be created at https://github.com/join

Once users create their accounts, user-specific home pages are created. For example: ''https://github.com/john-smith''.
A user-specific home page can contain repositories that the user has created or forked, contribution activity,
and organizations he/she has joined. 


## Fork a `SeattleTestbed` Repository

Forking refers to making a copy of a repository and saving it to your user home page. General instructions on forking repositories and managing pull requests are available [here](https://help.github.com/articles/fork-a-repo)

Forking a [SeattleTestbed](https://github.com/SeattleTestbed) repository requires clicking the ''fork'' button on the selected repository's Github page, which creates a copy of the repository and saves it to a repository directly controlled by the user (on the user's Github home page).  The URL of the forked repository can then be used with Git to create and save a local copy.  

Navigate to the [repy_v2](https://github.com/SeattleTestbed/repy_v2) repository and click on the ''fork'' button in the upper right-hand corner of the page.


[[Image(fork_sm.png)]]

## Clone a Git Repository

The **git clone** command creates a local copy of a remotely hosted Github repository.  So far, the **repy_v2** repository has only been copied and saved to the user's Github home page.  In the following example, the **repy_v2** `SeattleTestbed` repository is cloned to the user's local Git repository.  

```
$ git clone https://github.com/john-smith/repy_v2
Cloning into 'repy_v2'...
remote: Counting objects: 1547, done.
remote: Total 1547 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (1547/1547), 1.06 MiB | 0 bytes/s, done.
Resolving deltas: 100% (778/778), done.
Checking connectivity... done.
```


A **repy_v2** folder is created in the local, current working directory.  Before issuing Github commands, you need to change directories - to either the cloned repository's directory, or to one of its sub-directories. For example:

```
$ cd repy_v2/
```

### Set Alias for Forked Repository
Setting an alias for a repository can help developers better manage repository changes and
keep local and remote repositories in sync.  The alias is a string that refers to the repository by name instead of the
repository's full URL.  In the example below, the forked [repy_v2](https://github.com/SeattleTestbed/repy_v2) repository is given the **upstream** alias:


```
$ git remote add upstream https://github.com/SeattleTestbed/repy_v2.git
```


### Retrieve Latest Version of Forked Repository

Fetching and merging the latest changes of `upstream` (remembering that the `upstream` alias points to the forked repository) can be done with the
`pull` Github command.  The `pull` command fetches changes made to the remote repository and merges them into your local repository.  Branches are multiple working versions of a master project (or document). The main branch is the master repository and multiple, local branches of this master may be created by users so that they can work on the project before committing their work to the master document.  The pull command expects to see a (by default, the master) branch name, which the user will find on the project's [main repository](https://github.com/SeattleTestbed/repy_v2).  Information on creating a new branch is in the next section, ''Add a New Branch Locally''.

[[Image(branches_sm.png)]]

Additional information on branching: [branching](http://git-scm.com/book/en/Git-Branching-What-a-Branch-Is)

```
$ git pull upstream master
From https://github.com/SeattleTestbed/repy_v2
 * branch            master     -> FETCH_HEAD
  * [new branch]      master     -> upstream/master
  Already up-to-date.
```

### Add a New Branch Locally

First, list all known local branches of the repository, by typing the following:  

```
$ git branch
* master
```

Next, to add a new branch, which is the preferred method for working on and adding new features, type **git branch new_branch**, where **''new_branch**'' is the name of the new branch:

```
$ git branch new_branch
```

The next step is to switch to the newly created branch:

```
$ git checkout new_branch
Switched to branch 'new_branch'
```


### Commit a New File to the Branch

Create a `README.txt` file and save it to the local machine. You do this by opening a new document in a text editor and saving as `README.txt` in the current directory. In the README file you would typically put instructions or details about the project. 

The next step is to ask Git if it can find the README.txt file, by asking it to identify all untracked files (on the local repository):

```
$ git status
On branch new_branch
Untracked files:
  (use "git add <file>..." to include in what will be committed)

    README.txt

    nothing added to commit but untracked files present (use "git add" to track)
```

Git indicates that the README.txt file is untracked, so the first command (git add) will add it. The second command (git status) will tell us whether the file has been added successfully. 

```
$ git add README.txt

$ git status
On branch new_feature
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    new file:   README.txt
```

After adding the file it must be committed. By committing a file, Git creates a message about the file that will be transmitted once the file is ready to be pushed to the master branch.  A Git message should be descriptive and mention the reason for the change, or changes, to be committed.  In the following example, the `-m` flag (for message) is used and a commit message is appended in quotes.

```
$ git commit -m "Add a README file to the project"
[new_branch 7660f34] Add a README file to the project
 1 file changed, 1 insertion(+)
  create mode 100644 README.txt
```

If you want to check to see that all files have been added and committed, type **git status** again. The status should show that the directory is clean, as in the example below:

```
$ git status
On branch new_branch
nothing to commit, working directory clean
```

To get a list of commit messages made thus far, type **git log**. 
This will show the user's information and the commit message (in this case "Add a README to the project"):

```
$ git log
commit 3c9b1d0068075fdac6ed928f8e5a27ac3253ca5e
Author: John Smith <john.smith@example.com>
Date:   Tue Sep 2 14:46:36 2014 -0400

    Add a README to the project.
```


### Push the Commit to the Remote (Forked) Repository

This step will push the branch to the remote repository controlled by the user (the forked version that you created earlier). The changes committed in the "Commit a New File to the Branch" so far exist on the local repository.  The earlier commit message, along with the file, are pushed to the user's remote repository. 

```
$ git push origin new_branch

Username for 'https://github.com': john-smith 
Password for 'https://john-smith@github.com': 
Counting objects: 5, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 308 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
To https://github.com/john-smith/repy_v2
 * [new branch]      new_branch -> new_branch
```


### Pull Request

After the files are pushed, they can be made available to the Seattle Testbed Organization, after you (the user) initiates a pull request. 


Visit the forked ''repy_v2'' repository and click on the green button next to the drop-down list of branches.
The next page is where you will preview the commits and write/post a summary or comments about the changes you made. The image below shows where to locate the pull request button.


[[Image(pull-request_sm.png)]]

A page (containing the user's Pull Request) is generated by Github and viewable by both the user and developers of the **repy_v2** repository.  A [repy_v2](https://github.com/SeattleTestbed/repy_v2) developer can review the user's changes and either accept, decline, or ask that the user address issues with the pull request.    The pull request's page provides a section to enter comments and allow the user and [repy_v2](https://github.com/SeattleTestbed/repy_v2) developers to collaborate.  The user can make additional changes to the pull request (for example, to address an issue raised) by pushing commits to the user's forked repository.  In the following example, the user first edits the `README.txt` file and saves the changes before issuing **git add README.txt**: 


```
$ git add README.txt

$ git commit -m "Add missing section to README noticed by reviewer"

$ git push origin master
```

### Resolve a Merge Conflict

Merge conflicts might occur with Git's push or pull actions if multiple contributors attempt to modify the same section of a file, and merge their conflicting modifications to the server’s “master" branch. For example, suppose one contributor wants "foo" to appear in the first three characters of a file, while another contributor desires "bar". When a merge conflict occurs, the affected contributors must mutually resolve the conflicting section. That is, the file in the previous example must be edited to produce one unique version of the file; either "foo" appears in the first three characters, or "bar" does.

If Git detects a merge conflict after a pull or merge action, it inserts special markers in the conflicting section(s) of the file to indicate what needs to be resolved:

```
    <<<<<< HEAD
    foo
    ======
    bar
    >>>>>>
```

The text between <<<<<< HEAD and ===== is what is currently on the server’s “master” branch.  The text between ===== and >>>>>> is what is being merged and causing the conflict.  To resolve the merge conflict, a contributor must open the file in a text editor and manually remove the merge conflict markers and either keep what is currently on the “master” branch or what is being merged.  In the merge conflict example above, a contributor would keep either the text “foo” or “bar”, and remove the rest of the markers inserted by Git.  To finalize the merge conflict, the contributor must commit the resolved changes.

Steps to resolve the merge conflict:

Edit the file containing the merge conflict in a text editor.
To discard what is currently on the server and replace it with “bar”, delete “foo” and the three inserted markers.

1. Save the file.

2. ```$ git add```

3. ```$ git commit```

4. ```$ git push```

The following page provides a comprehensive guide on resolving merge conflicts: https://help.github.com/articles/resolving-a-merge-conflict-from-the-command-line/

## Miscellaneous Git commands
Typing **git help -a** on the command-line outputs the full list of commands supported by Git.
Consult Git's help pages for more information about each command.
Another resource that covers useful Git commands can be found here:
http://zackperdue.com/tutorials/super-useful-need-to-know-git-commands

The section below lists some useful, common Git commands.


To show changes/differences in the README.txt that have not been committed:

```
$ git diff README.txt
diff --git a/README.txt b/README.txt
index 70a3d0f..93bce69 100644
--- a/README.txt
+++ b/README.txt
@@ -1 +1,2 @@
 README file.
 +new line added here.
```


To Mark README.txt as removed and stage it for removal:

```
$ git rm README.txt
```


To unstage the modified README.txt file and reset its contents to the current version on the repository:

```
$ git reset README.txt
```


To move a file to a new location but let Git know of the change:

```
$ git mv
```


To temporarily store modified files in order to change branches:

```
$ git stash
$ git stash list
$ git stash pop
```