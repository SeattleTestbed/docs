# 10th GENI Engineering Conference (GEC 10)

## Introduction
----
This page describes what the MillionNodeGENI/SeattleGENI project will cover during the GEC 10 conference. 
The GEC 10 will be held this year at the Sheraton Puerto Rico Convention Center Hotel between March 15-17, 2011 at San Juan, Puerto Rico. 

The MillionNodeGENI project will have a tutorial session on **March 15th, 2011 at 2:30PM in San Cristobal.** This tutorial will be followed by a demonstration of some project that uses MillionNodeGENI to run cool experiments.
[[br]]

## Tutorial
----
[[br]]

## MillionNodeGENI project Demo
----
Monzur Muhammad will be demoing several of the projects that students and developers have written using MillionNodeGENI and the Repy language.

### Repy www sandbox
----
Albert Rafetseder from University of Vienna has implemented a web version of the Repy interpreter. The interpreter itself was written using the Repy language. By launching the program, an user is able to put up a webserver that allows an user to execute Repy code without the hassle of installing anything. A version of this code is running currently at the site: [http://repy_demo.zenodotus.cs.washington.edu:6060] 

If you would like to test out any network related code, the **ports 40000 - 40199** have been made available for use on [http://repy_demo.zenodotus.cs.washington.edu:6060]

If you want to run your own version of sandboxed www repy interpreter, you can download the attachment below. A copy of a default restrictions file has also been attached. You must preprocess the file using repypp.py and then run the program with a given port. Make sure that the restrictions file you are using has the right ports allowed. 

An example has been show below.
```python
$> python repypp.py repy_www_sandbox.0.1.1.py repy_www_sandbox.0.1.1.repy
$> python repy.py restrictions.default repy_www_sandbox.0.1.1.repy 12345
```
[[br]]

### HuXiang project
The HuXiang project was developed by the student Alan Loh at University of Washington. It allows a SeattleGENI user to host a website on a node without worrying about any configuration of hosting. Furthermore HuXiang takes advantage of the fact that we are able to register a domain name through our zenodotus server and is able to register the website you are hosting with the domain name of your choice. 

You can learn more about the HuXiang project by visiting its wiki page at [wiki:huxiang HuXiang Project]. You can download the required files from the wiki page and follow the instructions easily to host a website in minutes! 
[[br]]

### Seobinggo
The Seobinggo project was developed as a peer-to-peer backup system. It allows you to backup any of your local file, which are backed up locally as well as remotely on a peer node. The data that is backed up is encrypted with a publickey so unless you have the equivalent privatekey you won't be able to retrieve the backup file.

To learn more about the Seobinggo project please take a look at the [wiki:Applications/Seobinggo Seobinggo wiki] page