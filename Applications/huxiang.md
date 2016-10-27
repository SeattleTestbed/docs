# What is huxiang?

Taking advantage of the ability to register a domain name for a node's IP address through [wiki:Zenodotus zenodotus], you can host and maintain your own website through one of Seattle's nodes by the means of Overlord. By following the listed instructions and providing the application a word for your zenodotus address, your Seattle Clearinghouse username, and the directory path to the folder containing the files that make up the website, your website will be up for three hours unless you renew the VMs you borrowed (see the section on "Renewing Hosting")

# Huxiang Client versus Huxiang Server

This wiki page is meant to help you setup your own Huxiang server that you can maintain on your own computer. But for those who just want to get a webpage quickly hosted, alternatively you could use the Huxiang online server to do the hosting for you, with some restrictions

You can access the server [here](http://huxiang_online.zenodotus.cs.washington.edu:63140) or [here](http://128.208.4.96:63140) (if previous link doesn't work).

# Requirements
 * A Linux or Mac operating system
 * [M2Crypto](http://chandlerproject.org/bin/view/Projects/MeTooCrypto) installed

# Restrictions
There are a few restrictions that users must be aware of when hosting websites through huxiang:

  - Stated below later on in detail, links between pages hosted on the same server must be relative addresses instead of absolute ones

  - To avoid problems uploading files on to nodes, keep file sizes limited to about 1 MB at max

  - The computer running the file must remain on for Overlord to do its regular maintenance on the webhosting. Otherwise, the website will remain up for a maximum of 7 days since shut-down or until an error occurs with all the nodes

  - Overlord will also temporarily cease operations when the computer goes into sleep mode, but will automatically perform a maintenance round the moment the computer resumes operation

# Setting Up
 1. If you haven't done so already, to ensure you will have the necessary credits to use Seattle's P2P resources, download the version of Seattle appropriate to your operating system [here](https://seattleclearinghouse.poly.edu/download/flibble/), and follow the instructions on installing and starting it up.

 2. Next, download the Seattle demokit and extract the files to its default folder "demokit"

 3. Download the huxiang_webserver.tar file (either at the end of this page or [here](https://seattle.poly.edu/raw-attachment/wiki/huxiang/huxiang_webserver.tar)) and extract its contents into the same folder as your Seattle demokit.
 * Whether than keeping the recently extracted files in a separate folder within the demokit directory, move a copy of each file into the main demokit folder.

 4. If you haven't done so already, register for a public and private key for Seattle Clearinghouse [here](https://seattleclearinghouse.poly.edu/html/register), and download the publickey and privatekey file into your demokit folder

 5. Within the demokit directory on your console, follow the instructions in setting up Overlord [wiki:Libraries/Overlord here].

 * Within the instructions, you will also be asked to set up the Seattle Experiment Library within the overlord folder. Please follow the steps in doing so as well

 * There should now be a folder called "overlord" in the demokit folder.

 6. Either create your own web files or download the website you want to copy, and store it within a new folder in demokit. This can include HTML, CSS, image files, and other files that make up your webiste.
 * Make sure address linking between files are based on relative directory, not absolute URLs.

 For example, instead of using:
```
<a href="https://seattle.poly.edu/html/index.html">Home Page</a>
```
 for a link to the home page, change it to:
```
<a href="index.html">Home Page</a>
```
 ...instead.

 * While the 'Save Page as...' function of most web browsers is sufficient for saving a copy of a web page, for those who do not want to go through the trouble of saving each page of a website one by one and editing the links within each file, a better alternative is [HTTrack Website Copier](http://www.httrack.com). The program is capable of doing internal linking automatically for you when you download the site as a whole, and catches certain files that a browser may miss through 'Save Page as...'

 7. Within the folder "overlord", in the !experimentlibrary folder, open up seattlegeni_xmlrpc.py and set the value of CA_CERTIFICATES_FILE to the location of a PEM file containing CA certificates that you trust. Do the same for the seattlegeni_xmlrpc.py file in your main demokit directory
 * Alternatively, if you don't know where that is on your own system, download a PEM file from a trustworthy site and into the !experimentlibrary folder without making any changes to seattlegeni_xmlrpc.py. One such place to download this file is [here](http://curl.haxx.se/ca/cacert.pem)


## Hosting the Site
The main file you will be using is huxiang_creator.py, while huxiang_server.repy will handle the server side of things for the hosted website. If you want to make any changes to the server's callback function in handling HTTP requests, edits in code and functionality can be made to huxiang_client.repy before recompiling the file into huxiang_server.repy.
If you made any changes to huxiang_client.repy, be sure to pre-process the file through [wiki:SeattleLib/repypp.py repypp.py] with the command:
```
$ python repypp.py huxiang_client.repy huxiang_server.repy
```
or else the website hosting behavior will not reflect the changes you made.

Otherwise, the huxiang_server.repy included in the tarball should work fine.

Run huxiang_creator.py with the following four arguments:

  - A single-word string used to set part of the hosted website's home address. It cannot include any spaces or symbols

  - The Seattle Clearinghouse username the website will be hosted under.

  - Directory path of the file folder holding the web site files you're hosting.

  - Directory path from the base file folder to the file that will act as the homepage of your website

As an example of how the command should look:
```
$ python huxiang_creator.py example guest ./example_web_site ./html/index.html
```
With the above command, all the files within the folder 'example_web_site' will be hosted on all the nodes currently owned by 'guest' at the address 'example.zenodotus.cs.washington.edu'. For a user to access the site, the URL the person would browse for is 'example.zenodotus.cs.washington.edu:(port number)', where (port number) is the Seattle Clearinghouse port number assigned to "guest". The number is immediately available and labeled as "Port" the moment you sign on to Seattle Clearinghouse. The user will then finally be directed to .../html/index.html, which will act as your website's homepage. It is important that you include the arguments in the order listed above or else the application will throw an error.


The check the status of your webhosting, simply open up the "huxiang_webhosting.log" file with any text editor, and it will show you information on the number of nodes currently hosting the site, any errors that occurred, actions taken by Overlord to handle the errors, and other messages.

If you forgot the address of your website, you can also open up the same log file and it should be listed in the first line of the file.



## To Stop Hosting
Simply create a file named "stop" within the overlord folder. While the program may take up to 15 minutes to terminate, you are free to release the nodes that you currently own at that point in time and do whatever is needed without Overlord interfering.

Alternatively, perform a keyboard interrupt within the console if the huxiang_creator.py is running in the foreground.



# Troubleshooting
**All of the nodes are timing out when trying to upload huxiang_server.repy**
 The problem should be fixed now. Make sure you are using the latest version of overlord and demokit.

**How do I install M2Crypto?**
 (for Ubuntu ver 10.04 and later) You can simply install the required package through the command:
```
$ sudo apt-get install python-m2crypto
```
 Otherwise, for more details, check the link provided above.
 

**I can't access the hosted website, but the hosting node says it's running just fine.**
 Make sure you inputted the URL of the hosted site into your browser correctly. Also, there may be a variable amount of delay between execution of the application to the web site actually being accessible through a browser. 

**One of the images are missing on the site, but I'm pretty sure I downloaded all of the required files to host the web page separately**
 A common issue with the "Save Page as..." function of browsers such as Firefox is the inability to save images used in the CSS style sheet. The only way to circumvent this at the moment is to manually save the images into the same folder as the rest of the web page's file contents, or use [HTTrack](http://www.httrack.com) to get a more comprehensive download of the page.



# Further Information

For more about how the assignment of names to node's IP addresses work, visit the Zenodotus page [wiki:Zenodotus here].

Basically, when running in a node, this will associate the set zenodotus address with the node's IP Address. When a user types in the address along with your respective port number into the browser, they will automatically be directed to the home page of the site. Any further URL requests will result in the server doing a check to see that the requested path matches the site map's configuration, and either send back the web file associated with page requested or display an error message.

Also, when a user requests a query for the location of the node by adding "?location" into anywhere in the path, the server will automatically bring up a frame at the top of the page displaying the coordinates of the node and its location, if available.

