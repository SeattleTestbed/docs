# Seattle Latency, Bandwidth, and BufferBloat Assignment

The purpose of this assignment is to illustrate how latency, bandwidth, and bufferbloat impact network traffic.  Students will learn the impact of each feature on video traffic from their computer.   They will take notes on the relative time it takes to interact with the video as well as the amount of video that can pass over the channel in a given amount of time (i.e. the load time per second of video).

When performing these steps, you are running software on end user machines around the world.   As such it is possible (but unlikely) that you may have a node fail as a user turns off their laptop, loses network connectivity, etc.   If so, you should be able to redo the previous step to continue with the assignment.

This assignment consists of ?? steps and should take about one hour to complete.   Let's begin!

**Windows users:** You must have Python installed in order to run Seattle. For help installing the right version of Python, refer to our [wiki:InstallPythonOnWindows Python installation instructions].

----

----


# Sending video


## Step 1 : Setting up the video player
----


Help!!!




## Step 2 : Communicating through a local relay
----

Download the relay code [wiki:relaycode.zip linked here].   Unpack it and run ```python simplerelay.py``` or ```simplerelay.py```.   
 If these fail, you may need to [download python](http://www.python.org).   On Windows systems, you may also need to set your environment path to point to the copy of python you installed by clicking on Control Panel--> Systems--> Advanced Settings-->Environment Variables.   

Now open your video player server and tell it to ...    (Set up listening / chatting so it goes through the relay.)




## Step 3 : Examining latency
----

Now we will run the relay with additional latency.   This is similar to the behavior you will see when communicating with a computer that is very far away, such as in another country.

First, we will start with an example of latency you might see over certain connections (especially satellite links for geographically distributed computers).   To do this, run ```python simplerelay.py 1000```    This instructs the relay to delay your traffic by 1000 ms (or 1 second).   Now open the video program and you will observe a 1 second delay between actions and their display on the screen.  

You can also try this with a very extreme example of latency.   To do this, run ```python simplerelay.py 10000```    This instructs the relay to delay your traffic by 10000 ms (or 10 seconds).   Now open the video program and you will observe a 10 second delay between actions and their display on the screen.  

If you stop the server chat program, does the video stop immediately or does it takes a while for the client to notice?

Does the picture look as clear as the local relay communication?




## Step 4 : Examining bandwidth
----

Now we will run the relay with constraints on the available bandwidth.  This is similar to what you will see communicating over a slow network

First, we will set the bandwidth to be 100Kbps.   To do this, run ```python simplerelay.py 0 100```    This instructs the relay to set a bandwidth limit of 100Kbps.   Now open the video program and you will observe the video quality is degraded due to the lower bandwidth.  

You can also try this with a very slow connection.   To do this, run ```python simplerelay.py 0 10```    This is a setting of 10Kbps (a similar speed to older dial-up modems).   Now open the video program and you will observe a further degradation of quality.  

If you stop the server chat program, does the video stop immediately or does it takes a while for the client to notice?

Does the picture look as clear as the local relay communication?




## Step 5 : Examining bufferbloat
----

Now we will run the relay with constraints on the available bandwidth and store content at the relay.  This is similar to what you will see communicating over a slow network that has large buffers in the network hardware.   For an excellent article about bufferbloat, please see XXX.

First, we will set the bandwidth to be 100Kbps with a buffer of 10MB.   To do this, run ```python simplerelay.py 0 100 10000```   Now open the video program and you will observe the video quality is degraded due to the lower bandwidth.   Let the chat programs run for 20 seconds or so.

If you stop the server chat program, does the video stop immediately or does it takes a while for the client to notice?

Does the picture look as clear as the local relay communication?


Now try to set the bandwidth and buffering to a different value.   Try to set the bandwidth to 10Mbps with a buffer of 10MB.   To do this, run ```python simplerelay.py 0 10000 10000```   Now open the video program and you will observe the video quality is degraded due to the lower bandwidth.   Let the chat programs run for 20 seconds or so.

Did this change the video stop time?

Did this change the picture quality?





# Communicating through a remote Seattle relay


## Step 6 : Adding resources
----

Login to the Seattle [Clearinghouse website](https://seattle.poly.edu/geni/).   If you don't already have an account, go ahead and register for an account.   Click on the My VMs tab and you'll see that you currently aren't using any resources. 

In the top pane, select WAN and choose 5 VMs, and click "Get".  At this point, you should have VMs that you can use to run your code!



## Step 7 : Running Seash
----

Now click on the Profile tab, and download the demokit linked from this page.   Unpacking the zip file will create a directory that contains a shell called seash.py and a bunch of other files you need to do the take home assignment.   Click to download your Private Key and Public Key (save the files to the directory with seash.py).  This will give you the credentials necessary to run your programs on the computers now at your disposal.     

 * On Windows do start, run, cmd and then cd to the folder where you downloaded the demokit.   

 * On Mac / Linux, open a terminal window and change to the directory where you downloaded the demokit.   

Then type "python seash.py" or "seash.py".   If these fail, you may need to [download python](http://www.python.org).   On Windows systems, you may also need to set your environment path to point to the copy of python you installed by clicking on Control Panel--> Systems--> Advanced Settings-->Environment Variables.   

You will see a prompt like " !> " once seash starts.  Seash will allow you to easily run programs across multiple computers at the same time.



## Step 8 : Browsing your resources
----

Now lets add the credentials you just downloaded from the website into seash.  Type the following command at the prompt, **(replacing ''username'' with the user name you used to log into the Seattle Clearinghouse website)**

```python
!> loadkeys username
```

Then, type

```python
!> as username
```

This will change the prompt to " username@ !> " to indicate that by default, you are now acting with your credentials.  Next, tell seash to search for VMs you control by typing browse:

```python
username@ !> browse
```

This will search for VMs that you control so that seash can access them.  You should see several vessels added.  The output from browse command will look something like the following:

```python
username@ !> browse            
Added targets: %1(IP:port:VMname), %2(IP:port:VMname), %3(IP:port:VMname), ...
Added group 'browsegood' with X targets      
```

This tells you that the seash has discovered (at least some of) the computers you selected and verified that they are ready to run your code.  

If some of the virtual machines were not recognized, feel free to go to the My VM tab and remove those VMs.   You can then acquire new ones.   If you browse again, you should see the new computers as recognized.   (Your old ones will still be known to seash too.)



## Step 9 : examining characteristics of remote computers
----


NEEDS TO BE REVISED

In the above print-out response to the browse command, the %1, %2, %3, etc are an easy way to refer to a computer.  For example, we can run a "hello world" program on computer %1 by typing:

```python
username@ !> on %1 run helloworld.repy
```

To see the results of this command on computer %1 we would type:

```python
username@ !> on %1 show log
```

This shows you the output from the %1 computer, which should say "Hello World". If you're going to deal with a specific computer over and over, then constantly typing "on computername" before every command can be very annoying.   You can instead set the default target by simply typing

```python
username@ !> on %1
```

and hitting enter.  This will change your prompt to be:

```python
username@%1 !>
```

This indicates that you're acting as your username and you're acting on %1 (unless otherwise specified).  Try typing

```python
username@%1 !> run helloworld.repy
```

and then type


```python
username@%1 !> show log
```

You'll see two "Hello World" lines now because you've run the program twice.  

## Conclusion

Needs work!!!

That's all for the take home assignment.   You've just seen non-transitive connectivity in practice, used one hop detour routing to circumvent it, and also determined if your computer is behind a NAT.   We hope this has been informative and enjoyable.   If you would like to [DonatingResources donate resources] to the Seattle project, you call install Seattle on your home computer.   Clicking on the Get Donations tab from your Seattle Clearinghouse account and picking the appropriate installer to download will credit the donation to your account.   If you have any comments or questions please contact justinc -AT- cs -DOT- washington -DOT- edu