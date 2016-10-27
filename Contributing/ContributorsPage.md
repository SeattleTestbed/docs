# Contributor Page

This page contains information useful to developers working on Seattle.   Anything that is essential for each developer to read is **in bold text**.

Note: We've recently moved our VCS and ticket system to GitHub. Please see our [organization's page](https://github.com/SeattleTestbed) for the latest code, to discuss open issues, and to create forks off our code base for your contributions!

**If you are a new contributor, please look at our [wiki:GettingStarted Getting Started] page.**
 * Accessing our GitHub repositories, building components, Github & Git tutorial, and using the wiki
   * Check out (i.e., ```git clone```) our source code from [https://github.com/SeattleTestbed]
   * [wiki:BuildInstructions Instructions] for building Seattle components

   * [wiki:Local/RepoAccess Github and Git] instructions
   * [Useful Git Commands](http://zackperdue.com/tutorials/super-useful-need-to-know-git-commands)
   * [How to resolve a merge conflict with Git](https://help.github.com/articles/resolving-a-merge-conflict-from-the-command-line)
   * [wiki:SubmittingAPatch How to submit a patch for inclusion if you do not have commit access]
   * ~~**[wiki:ContributorAccounts Getting accounts] for Seattle Wiki, testbed machines, and seattle-devel**~~
   * ~~**[wiki:ManagingTracTickets Managing Trac tickets]**~~

 * Programming in Repy
   * The [Python Tutorial](http://docs.python.org/tutorial/) from the Python site.
   * [wiki:PythonTutorial Subset of Python Tutorial] with basic information about the subset of Python needed to write code in Repy
   * [wiki:PythonVsRepy Python You Need to Forget to Use Repy]
   * **[wiki:RepyTutorial Repy Tutorial]**
   * [wiki:RepyApi Repy Library] reference
   * [wiki:SeattleLib Seattle Standard Library] reference
   * [wiki:PortingPythonToRepy Porting Python to Repy Guide]
   * [wiki:RepyHelper Importing Repy code into Python using repyhelper]
   * [wiki:RepyV1vsRepyV2 Difference between Repy V1 and Repy V2]

 * Testing
   * **[wiki:UnitTestFramework Writing Tests for Seattle's Unit Test Framework]**
   * **[wiki:UnitTests Running Repy and / or node manager unit tests]**
   * [wiki:UnitTestFrameworkRunning Supplemental information about Running Tests with Seattle's Unit Test Framework]
   * [wiki:UpdaterUnitTests Running Software Updater Unit Tests]
   * [wiki:IntegrationTestFramework Writing Integration Tests] 
   * [wiki:Local/RunningIntegrationTests Running Integration Tests]
   * [wiki:ClearinghouseInstallation Running a Clearinghouse test server]
   * [wiki:Archive/CustomInstallerBuilderTesting Running a Custom Installer Builder test server]
   * [wiki:RemoteTestingService Running remote tests on seattle testbeds]
   * **Continuous Integration via Travis-CI and AppVeyor:**
      * [For team members - managing CI](https://github.com/SeattleTestbed/seattlelib_v2/wiki/Continuous-Integration-for-the-Team)
      * [For potential contributors - how to contribute and test](https://github.com/SeattleTestbed/seattlelib_v2/wiki/How-to-Contribute)

 * Style guidelines for documentation, python code, web code
   * **[Python/Repy style guidelines](https://github.com/secure-systems-lab/code-style-guidelines) for most Seattle programming**
   * [wiki:WebCodingStyle Web style guidelines] for web programming
   * **[wiki:Local/WikiFormatting Documentation format guidelines] for wiki pages**

 * Installation instructions and documentation
   * [wiki:InstallerDocumentation Formal Installer Documentation]
   * [wiki:SeattleDownload Download and installation instructions] for Seattle
   * [wiki:ClearinghouseInstallation Installing your own instance of Seattle Clearinghouse]
   * [wiki:CustomInstallerBuilder Using the Custom Installer Builder]

 * API specifications for user-facing services
   * [wiki:SeattleGeniApi Seattle Clearinghouse XML-RPC API]
   * [wiki:SeattleGeniClientLib Seattle Clearinghouse XML-RPC Client Library]
   * [wiki:CustomInstallerBuilderApi Custom Installer Builder XML-RPC API]

 * Deployment
   * [wiki:BaseInstallers Building] the base installers
     * [wiki:NsisSystemSetup System setup instructions] to be able to build the Windows GUI installer
   * [wiki:Local/VersionDeployment Deploying] a new version
   * [wiki:SoftwareUpdaterSetup Setting up] the software updater
   * [wiki:Archive/SeattleGeniProductionHttp Updating] the production Seattle Clearinghouse code
   * [wiki:BuildDemokit Building the Demokit]
   * [wiki:Libraries/Overlord Overlord Deployment and Monitoring Library] for deploying persistent services on VMs

 * Developer Resources
   * [wiki:Libraries/ExperimentLibrary Experiment Library] for use in scripting communication with nodes, etc.
   * [wiki:DevelopingWithEclipse Developing with Eclipse]

 * ~~Project Resources~~
   * ~~[wiki:SeattleResources A full listing of Seattle project services]~~
   * ~~[wiki:Local/ContributorAccountManagement Creating and deleting accounts for developers]~~
   * [wiki:SeattleAdminResources Resources needed by Seattle sysadmin]

 * Events relevant to Seattle and Seattle team information
   * [wiki:SeattleTalks Upcoming talks] about Seattle
   * **[wiki:Local/ContributorContactInfo Project Members] contact information**
 
 * Other
   * [wiki:SeattleBackend  Seattle Backend]
   * [wiki:ContainmentInSeattle] about controlling node outgoing traffic
   * ~~[wiki:Archive/MobileCeNotes Windows CE] implementation notes and problems~~
   * [wiki:BenchmarkCustomInstallerInfo Benchmark and Custom Installer Info] implementation notes and problems.
   * [wiki:RepyNetworkRestrictions Repy Network Restrictions] information and errata.
   * [wiki:Libraries/StatisticsLibrary Statistics Library] for analyzing date regarding nodes & VMs on Seattle.
   * [wiki:Applications/GeoIpServer Running a GeoIP Server]
   * How to run the [wiki:RunningSecLayerBenchmarks security layer benchmarks]
   * [SeleXor](http://selexor.poly.edu/) for additional control over the VM acquisition process.