# How To Submit a Patch To Seattle Testbed

More than a hundred developers have submitted code that has been accepted into our repository.   We'd love to have your contribution too!   You will find a lot of helpful information on the Contributors Page.

First of all, please check that we have not already fixed the bug that you have found or added the feature you want.   To do this, please check out the latest version of the software [from GitHub](https://github.com/SeattleTestbed).   If we have fixed it, but have not yet merged it into the master and pushed the release, feel free to let us know about it and that you would like us to push!

## GitHub contributors

If you have an account on [GitHub](https://github.com/) already, the easiest way to submit patches is by creating a **Pull Request**. The usual workflow for this is as follows:
 * Find the source repository under [SeattleTestbed](https://github.com/SeattleTestbed) that contains the file you want to patch.
 * Create a **fork** of this repo into your GitHub user account.
 * On your fork, create a new **branch** with a descriptive name for the functionality you add, or issue you fix. Examples for good branch names: `fix-seash-#118`, `add-headless-install`
 * Commit to your branch, and push the results to GitHub.
 * Once you are satisfied with your work, issue a **pull request** to the repository you forked from. Please add to the description of the pull request any references to existing issues and relevant commit hashes, and use **@mentions** to bring your work to the attention of any non-core Seattle developers.

([wiki:Local/RepoAccess Our wiki] has more details on working with Git and GitHub.)



## Contributors with no GitHub access

You don't have to have an account on GitHub to contribute. If you have a small patch (such as a one line bug fix), simply email a diff of the file to the developers mailing list.   Please either give the original file's commit hash or the version of the Seattle installer (look in `nmmain.py`) so that we know what to compare it with.

If the patch is more significant, please also contact the developers list. They will first create an issue describing the feature or bug.  The development team will discuss the patch on the mailing list and multiple developers will weigh in.


## Good patches

A good patchset comes with a succint description of the problem it solves, and ways to test that the fix is actually effective. We encourage writing [wiki:UnitTestFramework Seattle unit tests] for any non-trivial fix or feature addition.

For pull requests, please give your branches self-explanatory names that refer to existing issue numbers etc. (if available). 

Any patchset or pull request that we consider for inclusion in the master branch must match the [wiki:CodingStyle coding style] guidelines for the project.   (A core member will ensure this for you for tiny patches.)   

In general, the BDFL (Justin) is very protective of the trusted code base (the Repy VM, node manager, and Software updater).   As such, you should definitely discuss any proposed feature additions to these components **before** writing code.



-----



Many developers who submitted a patch ended up being part of the core team and earning commit access.   We look forward to your contributions!