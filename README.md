# Welcome to Seattle Testbed!

Seattle Testbed is a free, open-source platform for networking and 
distributed systems research. 
This repository contains the Seattle documentation, including

* [High-level overviews of all parts of Seattle Testbed](UnderstandingSeattle/README.md),
* [Programming tutorials and API docs](Programming/), 
* [Educational assignments for class and home use](EducationalAssignments/),
* [Documentation for running Seattle infrastructure services](Operating/), and
* [Information for contributors](Contributing/README.md).

An introduction to Seattle Testbed follows below. For Seattle source code, 
please visit our organization page at https://github.com/SeattleTestbed

# What is Seattle Testbed?

Seattle Testbed is a free, community-driven network testbed for 
education and research. It offers a large deployment of computers 
spread across the world. You can use our [Clearinghouse](https://seattleclearinghouse.poly.edu/) 
website to share resources with other users, or obtain resources for your own 
project.  Seattle operates on resources donated by users and institutions. 
The global distribution of the Seattle network provides the ability to use it 
in application contexts that include cloud/fog computing, peer-to-peer 
networking, ubiquitous/mobile computing, and distributed systems.

Seattle runs on end-user systems in a safe and contained manner, with support 
for several platforms. Users install and run Seattle with minimal impact on 
system security and performance. Sandboxes are established on the user's 
computer to limit the consumption of resources such as CPU, memory, storage 
space, and network bandwidth. Programs are only allowed to operate inside of 
a sandbox, ensuring that other files and programs on the computer are kept 
private and safe. This allows researchers and students to safely run code without 
impacting performance or security.

For more information, please check out our 
[overview movie](http://seattle.poly.edu/static/SeattleMovieFinal.mov).

For a less technical overview of Seattle check out 
[the Seattle homepage](https://seattle.poly.edu/html/).

If you would like to contribute to Seattle, please head over to 
[our GitHub organization page](https://github.com/SeattleTestbed).


# Features
* Community-driven and free.
* Scalable architecture.
* Non-intrusive and safe for end users.
* Already installed on tens of thousands of computers around the world.
* Provides access to systems behind a wide array of network technologies.
* Easy to learn, based on a subset of [Python](https://www.python.org/).
* Simple and clean programs:
  * A UDP ping client is just six lines of code. A UDP ping server is just four lines.
   * A [Chord](https://github.com/sit/dht/wiki) implementation requires about 300 lines of code.
* Cross-platform support:
   * Windows (XP or newer)
   * Mac OS X
   * Linux
   * Many BSD variants
   * Portable devices (Android tablets and phones)
   * WiFi routers running OpenWrt


# Is Seattle for me?
Seattle is ideal for students, researchers, and companies that want to 
prototype and test code on testbeds that have varying scale, diversity, and 
topologies. The same code may easily be run on a variety of operating 
systems, architectures, and network environments in order to understand the 
performance and dynamics of a distributed system. Seattle is also ideal for 
studying the wide-area characteristics of the Internet. For example, path 
transitivity, latency and bandwidth variations, as well as availability can 
all be characterized with Seattle.

Users needing direct access to hardware or support for low-level languages 
should look elsewhere. Seattle forgoes these capabilities to ensure safety 
and performance isolation for end users.


# What makes Seattle different?

There is a wide variety of other platforms and testbeds readily available, 
each with an equally expansive set of project goals. Related projects 
include the following:
 
 * [PlanetLab](https://www.planet-lab.org/) is similar to Seattle in that it offers a platform composed of donated resources from around the world. However, PlanetLab nodes are dedicated to PlanetLab, while Seattle computers are not dedicated to the platform. In addition, PlanetLab's computers and network connectivity are very homogeneous. Seattle aims to be more widely distributed and to support broader resource diversity.
 * [SatelliteLab](http://satellitelab.mpi-sws.mpg.de/) is useful for studying network characteristics and aims to bring heterogeneity to PlanetLab. However, due to the reliance on PlanetLab nodes for forwarding traffic, SatelliteLab has fidelity limitations and is not able to scale to the diversity and size of Seattle.
 * [Emulab](http://www.emulab.net/) provides emulated network environments for researchers to conduct experiments. While emulation allows more control of network hardware and topology, it does not capture the behavior of the Internet. Running Seattle allows more realistic experimentation at larger scales by running on the Internet.
 * [BOINC](http://boinc.berkeley.edu/) and [HTCondor](http://www.cs.wisc.edu/htcondor/) also allow users to donate resources. However, the emphasis is on computational power, with a preference toward using a few supercomputers rather than a large group of cheaper PCs. Seattle places more emphasis on the diversity of the networks and systems used, as computational power is not the main goal.
 * [Amazon's EC2](http://aws.amazon.com/ec2/) is a paid service that provides operating-system virtual machines. Seattle instead relies on donated resources and provides programming-language virtual machines. 
 * [Google's AppEngine](http://code.google.com/appengine/) executes programs written in a constrained version of Python and supports high-level abstractions (such as global non-relational storage). It is useful for building locality-oblivious web applications that fit the HTTP request/response protocol model. However, its transparent handling of scalability and locality make it unsuitable for those wishing to teach or otherwise address these fundamental topics of distributed systems. AppEngine is run on Google-controlled resources instead of donated resources.
 * [The Tor Project](https://www.torproject.org/) is a widely used platform that protects users from Internet surveillance.   While some users have built Seattle applications for this purpose, simply installing Seattle does not provide any direct privacy benefits.   
 * ...and many others: [FIWARE](https://www.fiware.org/), [Splay](https://github.com/splay-project/splay), [Reservoir](http://www.reservoir-fp7.eu/), [OpenNebula](http://www.opennebula.org/), [Eucalyptus](http://open.eucalyptus.com/), [Fabric](http://www.cs.cornell.edu/projects/fabric/index.html), ...


# How do I learn more?

Learn the basics:

 * For more information, please check out our [ overview movie](http://seattle.poly.edu/static/SeattleMovieFinal.mov).
 * For a demonstration of Seattle, please view our [5-minute video](https://seattle.poly.edu/static/demo.mov).
 * Learn more about [how Seattle works](UnderstandingSeattle/README.md).
 * Try [donating resources](UnderstandingSeattle/DonatingResources.md) to other users.
 * Complete the [take-home assignment](EducationalAssignments/TakeHome.md) to get hands-on experience with Seattle.

Check out the portal pages for in-depth information:

 * [Programmers Portal](Programming/ProgrammersPage.md): Resources for programmers wanting to learn the platform.
 * [Educator Portal](EducationalAssignments/EducatorsPage.md): Example assignments for students using Seattle.
 * [Contributors Portal](Contributing/README.md): Detailed information about how to contribute to the project.

If you have questions about Seattle, send an email to jcappos@nyu.edu 
or visit the Seattle-users Google group (seattle-users@googlegroups.com, 
https://groups.google.com/forum/#!forum/seattle-users).
