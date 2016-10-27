# Performance Isolation Benchmarks


This set of benchmarks will provide information about the performance isolation and the overhead of different virtual machine technologies.   By comparing the results of performance with and without stress in different VMs, you can use this to determine how well different types of VM software isolate performance of resources like CPU, memory, disk, and threads / processes.  By checking the amount of memory the VMs are using, it is easy to find out the overhead of the different VMs. 

We have two sets of benchmarks, one testing Seattle's upcoming Repy V2, and another non-Repy specific. Running these benchmarks will take about 10-15 minutes, depending on the speed of your system and type of benchmarks you will run. You can decide which benchmarks you want to run. 

Benchmarks which support three different kinds of OS are offered, a Windows version and a Linux and a Mac OS X version. Either can be downloaded to run the test.  The links can be found on the bottom of this Wiki page. 

----



----

## Setting up The Benchmarks

### Set up Repy V2

Check out Repy V2 from the repository. You can check the code out anonymously:
```
svn co https://seattle.poly.edu/svn/seattle/branches/repy_v2
``` 

If you have ssh credentials on seattle.poly.edu, you might alternatively run the following, replacing USER with your username:
```
svn co svn+ssh://USER@seattle.poly.edu/seattle/branches/repy_v2
```

Either command will create a folder `repy_v2` with the code from the repository.


### Setup Repy Tests


Depending on your operating system, download linux.zip, macos.zip, or windows.zip file from the bottom of this page and extract it to  the repy_v2 directory created in the previous step.

Next, create a folder to run the benchmarks. On Linux and Mac, this can be done like so:

```
cd path/to/repy_v2/
mkdir bench/
python preparetest.py bench
cp benchmarking-support/* bench/
cp linux/for_test_repy/* bench/   # On Mac, use "cp mac/for_test_repy/* bench/" instead.
```

On Windows, use

```
cd path
to
repy_v2
mkdir bench
python preparetest.py bench
copy benchmarking-support
* bench

copy windows
for_test_repy
* bench

```


### Setting up the Disk Benchmark on Windows

On Windows, iozone needs to be installed separately. It can be downloaded from the link below:

http://www.iozone.org/src/current/IozoneSetup.zip

Run iozoneSetup.exe and install it under both the for_test_python and for_test_repy directories. 




## Running the Benchmarks

''NOTE'': These benchmarks are quite resource-intensive and may lock your machine for considerable amounts of time. Please be patient! For better control, consider running the tests inside of virtual machines (see below for instructions).

Each type of benchmark has its own script to initiate the benchmarks. On Linux or Mac, 
 * Depending on the type of benchmark you'd like to run, change into the for_test_repy or for_test_python directory
 * To run the CPU benchmark, invoke ./cpubomb.sh
 * To run the fork benchmark, invoke ./fork.sh
 * To run the disk benchmark, invoke ./disk.sh
 * To run the memory benchmark, invoke ./memorybomb.sh

If you can't run the scripts due to a "Permission not Allowed" or similar error, please use chmod 755 to change the permission of the script to make it executable. 

To run the tests in Windows, run the corresponding *.bat files.

Be sure that you should connect to the Internet when you are running tests in Windows. Do not worry about the network communication which may be shown in the terminal. It is just acting the role of the timer. 


## Running the Benchmarks in Virtual Machines

It is highly recommended to run the benchmarks in VMs, such as VMware Workstation, Virtual Box, Xen, etc. 

Setting up virtual machines:
 * Create 5 different VMs
 * cd for_test_python
 * Run the tests separately without stress in first 4 VMs TWICE by "python ***.py" and the results will be saved in the file "***x.txt". (*** means the kind of the test and x means the number of the VM. example: python cpubomb1.py )
 * Run the stress file in the 5th VM. 
 * Run the Python tests separately THREE TIMES simultaneously in first 4 VMs(run the same test in each VM at the same time) and the results will also be saved in the "***x.txt" file. 

Example:
Take running CPU benchmarks as an example. 

Run cpubomb1.py, cpubomb2.py, cpubomb3.py, cpubomb4.py separately first in 4 different VMs TWICE and gain the results files. This will produce cpu1.txt, cpu2.txt, cpu3.txt and cpu4.txt respectively in the four VMs, and each of them will contain 2 numbers of runtime without stress. Run cpubomb.py in the 5th VM and run cpubomb1.py, cpubomb2.py, cpubomb3.py, cpubomb4.py in the first 4 different VMs THREE TIMES and get the results. The text files should now contain 5 numbers. The last three numbers are the runtime with stress.

The stress files are cpubomb.py, fork.py, memorybomb.py and run_iozone, respectively. 

Be sure that you should connect to the Internet when you are running tests in Windows.


----

## Interpreting the result of the benchmarks
The benchmarks will return several result files to illustrate the isolation of Seattle. 
The file names of the benchmark results are related to the type of the test, for example: cpu bomb are cpu1.txt, cpu2.txt, cpu3.txt, cpu4.txt.

The first 2 numbers in each file illustrate the run time of calculating Fibonacci(37) without stress. The last 3 numbers in each file illustrate the run time of calculating Fibonacci(37) with stress. 

If the first 2 numbers do not differ from the other 3 very much, than it shows that the performance isolation is quite good. 

If the first 2 numbers differ largely from the other 3 it shows that the contention due to the stress has slowed down the runtime and that the performance isolation is bad and not effective.

Finally, the percentage of the increase of the runtime between before and after stress is given, which can show the performance isolation effects more clearly. 


## Overhead of the VMs
Another important factor of a good VM is its overhead.  If a VM is lightweight, it means you can run hundreds and thousands of VMs together compared to a heavyweight VM, which can only run 5 or 6 VMs together. We can calculate the overhead of the VMs by measuring the memory it will take. We can also determine the number of VMs your computer can run by dividing the whole memory of your computer. An example; if a VM takes up 1 GB of RAM and a computer has 8 GB total we can run around 7 VMs (depending on the RAM required by the OS) 


To measure the memory which a VM will cost, we can just open the System Monitor or Task Manager of the OS and check the memory it will take for a certain VM. Another method you can use to determine memory cost is to change the whole memory being used currently by adding or removing a VM and then find out the difference between them. 


In Seattle, we can determine the overhead by the memory each Python process uses which is shown in the System Monitor / Task Manager.


## Caution
 * Since this is a type of resources bomb benchmarks, the non-Repy benchmarks may lock up the computer. Because of this, it is highly recommended to run these benchmarks inside of VMs. The Repy benchmarks are safe and won't lock your machine. 
 * The tests may take a lot of time to finish depending on the computer specifications. If the controlling terminal is forced to close , please kill the processes manually in the system monitor / task manager. 


## Thanks
We would appreciate it if you can send the results of the benchmarks to us and also include your computer specifications (such as OS, CPU including number of cores, memory, etc.) and the performance of the VMs (such as the version, overhead, assigned CPU cores, cpu performance, memory, disk of the VMs).  We would also appreciate it if you could contact us if you encounter any problems.


Please contact: enchl317 at gmail.com
