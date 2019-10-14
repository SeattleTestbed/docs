# Contributor Page

This page contains information useful to developers working on Seattle.   Anything that is essential for each developer to read is **in bold text**.

Note: We've recently moved our VCS and ticket system to GitHub. Please see our [organization's page](https://github.com/SeattleTestbed) for the latest code, to discuss open issues, and to create forks off our code base for your contributions!

**If you are a new contributor, please look at our [Getting Started](README.md) page.**
 * Accessing our GitHub repositories, building components, Github & Git tutorial, and using the wiki
   * Check out (i.e., ```git clone```) our source code from [https://github.com/SeattleTestbed]
   * [Instructions](BuildInstructions.md) for building Seattle components

   * [Github and Git](../Archive/Local/RepoAccess.md) instructions
   * [Useful Git Commands](http://zackperdue.com/tutorials/super-useful-need-to-know-git-commands)
   * [How to resolve a merge conflict with Git](https://help.github.com/articles/resolving-a-merge-conflict-from-the-command-line)
   * [How to submit a patch for inclusion if you do not have commit access](SubmittingAPatch.md)

 * Programming in Repy
   * The [Python Tutorial](http://docs.python.org/tutorial/) from the Python site.
   * [PythonTutorial Subset of Python Tutorial](../Programming/PythonTutorial.md) with basic information about the subset of Python needed to write code in Repy
   * [Python Vs Repy Python You Need to Forget to Use Repy](../Programming/PythonVsRepy.md)
   * [Python vs RePyV2 Python You need to Forget to Use RePyV2](../Programming/PythonVsRepyV2.md)
   * **[Repy Tutorial](../Programming/RepyTutorial.md)**
   * **[RePyV2 Tutorial](../Programming/RepyV2Tutorial.md)**
   * [Repy Library](../Programming/RepyApi.md) reference
   * [RepyV2 Library](../Programming/RepyV2Api.md) reference
   * [Seattle Standard Library](../Programming/SeattleLib_v1/SeattleLib.md) reference
   * [Porting Python to Repy Guide](../Programming/PortingPythonToRepy.md)
   * [Importing Repy code into Python using repyhelper](../Programming/RepyHelper.md)
   * [Difference between Repy V1 and Repy V2](../Programming/RepyV1vsRepyV2.md)

 * Testing
   * **[Writing Tests for Seattle's Unit Test Framework](UnitTestFramework.md)**
   * **[wiki:UnitTests Running Repy and / or node manager unit tests]**
   * [Supplemental information about Running Tests with Seattle's Unit Test Framework](UnitTestFrameworkRunning.md)
   * [Running Software Updater Unit Tests](../Outdated/UpdaterUnitTests.md)
   * [Writing Integration Tests](../Operating/IntegrationTestFramework.md) 
   * [Running Integration Tests](../Archive/Local/RunningIntegrationTests.md)
   * [Running a Clearinghouse test server](../Operating/Clearinghouse/Installation.md)
   * [Running a Custom Installer Builder test server](../Archive/CustominstallerBuilderTesting.md)
   * [wiki:RemoteTestingService Running remote tests on seattle testbeds]
   * **Continuous Integration via Travis-CI and AppVeyor:**
      * [For team members - managing CI](https://github.com/SeattleTestbed/seattlelib_v2/wiki/Continuous-Integration-for-the-Team)
      * [For potential contributors - how to contribute and test](https://github.com/SeattleTestbed/seattlelib_v2/wiki/How-to-Contribute)

 * Style guidelines for documentation, python code, web code
   * **[Python/Repy style guidelines](https://github.com/secure-systems-lab/code-style-guidelines) for most Seattle programming**
   * [Web style guidelines](WebCodingStyle.md) for web programming
   * **[Documentation format guidelines](../Archive/Local/WikiFormatting.md) for wiki pages**

 * Installation instructions and documentation
   * [Formal Installer Documentation](../UnderstandingSeattle/InstallerDocumentation.md)
   * [wiki:SeattleDownload Download and installation instructions] for Seattle
   * [wiki:ClearinghouseInstallation Installing your own instance of Seattle Clearinghouse]
   * [wiki:CustomInstallerBuilder Using the Custom Installer Builder]

 * API specifications for user-facing services
   * [wiki:SeattleGeniApi Seattle Clearinghouse XML-RPC API]
   * [wiki:SeattleGeniClientLib Seattle Clearinghouse XML-RPC Client Library]
   * [wiki:CustomInstallerBuilderApi Custom Installer Builder XML-RPC API]

 * Deployment
   * [Building](../Operating/BaseInstallers.md) the base installers
     * [wiki:NsisSystemSetup System setup instructions] to be able to build the Windows GUI installer
   * [Deploying](../Archive/Local/VersionDeployment.md.md) a new version
   * [Setting up](../Operating/SoftwareUpdaterSetup.md) the software updater
   * [Updating](../Archive/SeattleGeniProductionHttp.md) the production Seattle Clearinghouse code
   * [Building the Demokit](../Operating/BuildDemokit.md)
   * [Overlord Deployment and Monitoring Library](../Archive/Libraries/Overlord.md) for deploying persistent services on VMs

 * Developer Resources
   * [Experiment Library](../Archive/Libraries/ExperimentLibrary.md) for use in scripting communication with nodes, etc.
   * [wiki:DevelopingWithEclipse Developing with Eclipse]

 * Project Resources
   * [wiki:SeattleAdminResources Resources needed by Seattle sysadmin]

 * Events relevant to Seattle and Seattle team information
   * [Upcoming talks](../SeattleTalks.md) about Seattle
   * **[Project Members](../Archive/Local/ContributorContactInfo.md) contact information**
 
 * Other
   * [Seattle Backend](../UnderstandingSeattle/SeattleShellBackend.md)
   * [Containment In Seattle](../Outdated/ContainmentInSeattle.md) about controlling node outgoing traffic
   * [Benchmark and Custom Installer Info](../UnderstandingSeattle/BenchmarkCustomInstallerInfo.md) implementation notes and problems.
   * [Repy Network Restrictions](../Programming/RepyNetworkRestrictions.md) information and errata.
   * [Statistics Library](../Archive/Libraries/StatisticsLibrary.md) for analyzing date regarding nodes & VMs on Seattle.
   * [Running a GeoIP Server](../Applications/GeoIpServer.md)
   * How to run the [Security Layer benchmarks](../OutdatedRunningSecLayerBenchmarks.md)
   * [SeleXor](http://selexor.poly.edu/) for additional control over the VM acquisition process.
