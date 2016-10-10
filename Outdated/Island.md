 = Island / CADET Profiling =

An Island is a construct which is based on a VirtualNamespace. It has the additional property that it profiles all of the standard API calls, and provides additional statistical routines to determine various things like time consumed doing certain activities, or the number of files opened, bytes read from a socket, etc.

This is a central component of CADET, since it is utilized to determine the performance characteristics of a program to optimize the host machine selection.



----

----


## Components

The functionality of the Island is provided across several components.
The components and their function are listed below:
 * virt_island.repy : Provides the implementation of the Island class. Evaluating an Island stores its profile information with in the object.
 * island_stats.repy : Provides routines to generate info from an Island. Includes general usage statistics, Island timeline, and time consumption information.
 * stoptime_logger.repy : Logs the time's repy was stopped, and makes the information available. Used by island_stats for time consumption.
 * prgm_stat.repy : Forces a normal repy program to run within an Island, and prints statistics upon termination.




## Island Class Implementation Details


The Island class is designed to have a minimal overhead, while still collecting all potentially valuable information for later analysis.
Specifically, the Island class tracks all calls to resource consuming API's. The Island maintains usage information about all resources,
and for files and sockets it also tracks usage on an individual basis. E.g. One could request the total bytes written to disk, or the bytes
written to a specific file.


The Island operates by providing an API which mimics that of the VirtualNamespace. However, when evaluate() is called on a context,
all the underlying API calls are wrapped by Island specific implementations which track the resource utilization of the API call.
Additionally, the wrapper functions maintain a "timeline" for each thread in the Island. The timeline is a chronologically ordered array of all the "events"
in the thread. This includes thread creation, thread destruction, and API calls. When an API which can block or may use variable amounts
of resources is called, the Island first registers a "Start API X" call followed by a "API X call" so that it is possible to know the initial TOC,
and the "Time of Return". Each event has an associated API, and a resource utilization amount. So, a typical event will be something like
: ("file.write", 1.24, 8) which indicates that at 1.24 seconds into the execution a call to file.write returned having wrote 8 bytes. Since the
timelines are maintained on a per-thread basis, the Island can avoid locking every call to an API which reduces the overhead.


Sockets and files have some additional handling which allows them to track usage on the individual level and in the broader global 
resource usage scope. This is done by wrapping the file and socket objects returned to the program, and including some additional
logic on the various function calls.




## Island Statistics Implementation Details

The functions in island_stats are directly related to the implementation of the Island class. They are able to parse the internal
structures of the Island to provide meaningful data. The basic usage is to simply print information about the island, such
as the amount of various resources used, either globally, at a thread level, or at a file and socket level.

There are also functions which will compile the timelines of the individual threads into a single "Island" timeline, which
allows for external processing of the activity to extend functionality.

One use of this information is provided by island_stats in the form of time consumption determination. By using the "Island" timeline,
it is possible to closely determine how time was utilized in the Island. This is done determining which resources are used by each
API, and then using the "Start call X" and "Call X" entries to determine the time spent within each API call. If an API is not being evaluation,
then it is assumed that the Island is performing general computation so "cpu" is being consumed. What complicates matters is determining
how to compensate for Repy being stopped. When the Island timeline is generated, an entry is inserted for each time that repy is "stopped"
by requesting that information from the stoptime_logger module. When we are processing the timeline, if a "Repy Stopped" event is encountered,
then we decide how to account for the stoptime. If a thread is sleeping during the stoptime, then the stopping had no effect. As an extension,
if the thread is not in an API call, then the stop had the effect of stopping "cpu" consumption for the stoptime and increasing the amount of time
a thread was in the "stopped" state. The complicated situation is when a thread is stopped within an API call. To handle this, we determine the
"expected time" of the API, which is based on the current resource utilization and the amount of resources used by the API. E.g. if we are allowed
to write 10 bytes per second to disk, and we are stopped on a call which writes 20 bytes, we expect that call to take 2 seconds.  If we compare the
amount of time we are stopped to the expected time, and determine that the expected time < total stoptime, then
we assume that the stopping had an effect of the time spent, so we discount that time from the resource utilization and count it against time which is
stopped.


One critical flaw with this approach is that there are valid reasons for the actual time to be much greater that the expected time without being due
to the stoptime. As an example, take socket.recv(). Since this call blocks a call to receive a single byte may block for hours, even though it is expected
to return immediately. If repy is stopped during that API call, it is impossible to determine why the call took longer than expected, so we must "assume"
that it is due to being stopped. This problem should go away with the transition to Repy V2 since all blocking operations are replaced by non-blocking
equivalents.




## Stoptime Logger Module Implementation Details

The stoptime logger module is used by island_stats when determining the time spent doing various activities. The reason it is needed is that
getresources() will only return the last 100 stoptimes, which may not be enough to span the entire life of an Island. The stoptime logger
implements a simple interface which launches a separate polling thread.


This thread will periodically sample for the repy stoptimes, and store any new stoptimes. The module stores some number of the entries
in memory, but after a arbitrary threshold, the module will log the stoptimes to disk. This way, the module maintains a constant memory
footprint while still providing access to as many stoptimes as needed.


All the data written to the file is "aligned" on a per-entry basis. This causes additional bytes to be read, written, and stored, but it allows
the module to perform binary searches on the data, enabling much faster retrieval of stoptimes on an interval once there is a substantial
number of entries logged.




## Program Stats Implementation Details

The prgm_stat.repy file is a very simple Dylink module which dispatch's the next module inside of an Island. Once the island terminates,
or calls exitall() the global resource usage, Island timeline, and time consumption information are calculated and printed.

This provides  a simple way to use the functionality of the Island, while bootstrapping existing code which is not designed to directly
use the Island module, or any of its parsing routines.




## Examples


### Single threaded program

Here is a simple program, which only uses a single thread of execution:

```

def write_data():
    limit, usage, stoptimes = getresources()
    # find out what twice my write limit is...
    file_write_amount = limit["filewrite"] * 2

    testfileobj = open("test.out","w")
    # write out twice my per second write limit...
    data = "X" * int(file_write_amount)
    testfileobj.write(data)
    testfileobj.close()

def use_cpu():
    start = getruntime()
    while getruntime() - start < 1:
        for x in xrange(500):
            val1 = x ** 2
            val2 = x ** 3

write_data()
use_cpu()

```

The write_data() function determine what about of data can be written in a second,
and tries to write twice that amount. This should cause the program to block for second,
while we compensate for over-using our file write resource.

The use_cpu() function performs some trivial computation in a loop until a second of 
wall time has elapsed. The only action the program takes is to first call write_data(), and
then use_cpu().

I've named this program test_basic.repy, and ran it a 10% CPU restriction,
allowing 100K bytes to be written per second, with the following command:

```
$ python repy.py restrictions.test dylink.repy prgm_stat.repy test_basic.repy

--- Island Summary ---

Total threads: 1
Live threads: 0
Total files: 1
Open files: 0
Total sockets: 0
Open sockets: 0

--- Global Sum ---

Total 'fileread': 0
Total 'filesopened': 1
Total 'tcpsend': 0
Total 'random': 0
Total 'insockets': 0
Total 'filewrite': 200000
Total 'events': 0
Total 'udpsend': 0
Total 'udprecv': 0
Total 'tcprecv': 0
Total 'outsockets': 0
Total 'cpu': 0.182549

--- Island Timeline ---

TOC, Thread, API, Amount
1.78870010376 MainThread island_create_thread 
1.7893280983 MainThread open 1
1.78962397575 MainThread start call file.write
2.79035711288 MainThread file.write 200000
2.87065291405 ALL Stopped 0.704621213531
3.675604105 ALL Stopped 0.906205998082
4.58244991302 MainThread island_destroy_thread 

--- Thread Time Consumption ---

Thread:
  Name: MainThread
  Total 'filewrite': 1.00073313713 (35.82%)
  Total 'live': 2.79374980927 (100.0%)
  Total 'stopped': 1.61082721161 (57.66%)
  Total 'cpu': 0.182189460521 (6.52%)

All Threads (Global)
  Total 'filewrite': 1.00073313713 (35.82%)
  Total 'live': 2.79374980927 (100.0%)
  Total 'stopped': 1.61082721161 (57.66%)
  Total 'cpu': 0.182189460521 (6.52%)

```

Now, lets look at the output produced. At the top we have our "Island Summary" and "Global Sum". This shows us that the
Island has only a single thread over its life, and that the only resources it used were a single file handle, 200K bytes worth
of filewrite and about ~0.18 seconds of actual CPU time. Since we wrote 2x our filewrite limit (100K) to a single file,
this all seems consistent.

Next, we see a timeline of activity in the Island. The MainThread has a "island_create_thread" event which indicates that
it has "joined" the Island at a certain time. Then a file is opened, we start the call to file.write() and eventually return from it.
Notice the difference between the T.O.C and the T.O.R from the file.write of 1 second. This reflects what we expected, since
we wrote twice our limit. After that, it shows that "ALL" the threads were stopped at 2.87 and 3.67 seconds for 0.70 and 0.91 seconds
respectively. This corresponds to the call to use_cpu() which is presumably using as much CPU as possible. Finally, we see
"island_destroy_thread" which indicates that the thread has left the Island or terminated.
 
Lastly, we have our thread time consumption. Since we only have a single thread, the Global usage, and the usage of the
"MainThread" are the same, so we an just focus on one. The first key entry is the 'live' entry. This indicates the total amount
of wall time that this thread was part of the Island. We are reporting about 2.8 seconds, which can be checked by looking at
the island_create_thread and island_destroy_thread times above. Next, we have the "filewrite" entry. It indicates that 1 second
was spent writing to a file, which is correct and accounts for about 35% of the life of the program. One might expect the remaining
time to be allocated to "cpu", since all we did was perform some computation in a loop. However, since we are throttled to 10% CPU usage,
a more significant portion of our time was spent stopped. In face, the proportion of time stopped and in "cpu" is no coincidence.
Notice that "cpu" / ("cpu" + "stopped") = 0.10 which matches our CPU restriction.

Analyzing this information reveals that the greatest speed-up to this program would be from allocating more CPU, to reduce the amount
of time spent in the "stopped" state.




### Multi-threaded Program

I've taken the example program from above, but replaced the last two lines with the following:

```
            
settimer(0.1, write_data, ())
settimer(0.1, use_cpu, ())
sleep(0.2)

```

This has the affect of running each method in a separate thread, and to make the MainThread spend most of it's short life sleeping.
I've also reduced the CPU allocation to 1%. Now, lets look at the output this produces:

```
$ python repy.py restrictions.test dylink.repy prgm_stat.repy test_basic.repy 

 
--- Island Summary ---

Total threads: 3
Live threads: 0
Total files: 1
Open files: 0
Total sockets: 0
Open sockets: 0

--- Global Sum ---

Total 'fileread': 0
Total 'filesopened': 1
Total 'tcpsend': 0
Total 'random': 0
Total 'insockets': 0
Total 'filewrite': 200000
Total 'events': 2
Total 'udpsend': 0
Total 'udprecv': 0
Total 'tcprecv': 0
Total 'outsockets': 0
Total 'cpu': 0.103658

--- Island Timeline ---

TOC, Thread, API, Amount
8.59868597984 MainThread island_create_thread 
8.59897899628 MainThread start call settimer
8.59966897964 MainThread settimer 1
8.59981298447 MainThread start call settimer
8.60012602806 MainThread settimer 1
8.60028600693 MainThread start call sleep
8.67762613297 ALL Stopped 0.294054779492
8.9728770256 MainThread sleep 0.2
8.97305107117 _EVENT:Thread:3 island_create_thread 
8.97326397896 _EVENT:Thread:2 island_create_thread 
8.97368502617 MainThread island_destroy_thread 
8.9745631218 _EVENT:Thread:2 open 1
8.97507095337 _EVENT:Thread:2 start call file.write
9.07225203514 ALL Stopped 10.0952581368
19.168954134 _EVENT:Thread:3 island_destroy_thread 
19.1693820953 _EVENT:Thread:2 file.write 200000
19.170222044 _EVENT:Thread:2 island_destroy_thread 


--- Thread Time Consumption ---

Thread:
  Name: MainThread
  Total 'live': 0.374999046326 (100.0%)
  Total 'sleep': 0.2 (53.33%)
  Total 'stopped': 0.172591018677 (46.02%)
  Total 'cpu': 0.00240802764893 (0.64%)

Thread:
  Name: _EVENT:Thread:3
  Total 'live': 10.1959030628 (100.0%)
  Total 'stopped': 10.0952581368 (99.01%)
  Total 'cpu': 0.100644926038 (0.99%)

Thread:
  Name: _EVENT:Thread:2
  Total 'filewrite': 1.0 (9.81%)
  Total 'live': 10.196958065 (100.0%)
  Total 'stopped': 9.19431114197 (90.17%)
  Total 'cpu': 0.00264692306519 (0.03%)

All Threads (Global)
  Total 'filewrite': 1.0 (4.82%)
  Total 'live': 20.7678601742 (100.0%)
  Total 'sleep': 0.2 (0.96%)
  Total 'stopped': 19.4621602974 (93.71%)
  Total 'cpu': 0.105699876752 (0.51%)

```

Now the information at the top has changed slightly. We now report that the Island had a total
of 3 threads, and that 2 events were used, which is correct.

The timeline is slightly more complicated now, since we see that several threads are inter-mingled.
However, we see that the MainThread first calls settimer twice, and then goes to sleep.

At that point, repy is stopped for 0.29 seconds. Following that, the two other threads are created,
and the MainThread wakes up from its sleep and exits. Thread "_EVENT:Thread:2" opens a file and beings
to write, when repy is stopped suddenly for 10 seconds, due to thread "_EVENT:Thread" which is just wasting CPU.
Afterward, the two threads finish up and exit.

Now we can look at the thread time usage information, which is broken down for each thread,
and then given globally. The MainThread is very simple to analyze. All that thread did was
call settimer twice, sleep and then exit. So as expected, we see that 0.2 seconds were spent sleeping,
and essentially the remaining portion of the thread's life was stopped. This seems accurate since the thread
was stopped during the sleep, which extended the amount of time in the API call.

Then we have the _EVENT:Thread:2 thread which was writing to disk. From before, we expected this file.write
call to take 1 second, but were we were stopped for 10 seconds during the API call. However, the time usage
information accurately reflects that 1 second was spent in "filewrite" and that the remaining 90% of the thread's
life was spent in a stopped state.

The _EVENT:Thread:3 thread spent its time just wasting CPU. Accordingly, the amount of CPU it was able to
use is that of our CPU restriction (1%). The remaining time, it was stopped to compensate for overuse.

The last entry is the Global sum, and it just sum's up the information to provide a higher level overview.
What is clear, is that at 93% of the time being "stopped", this program would greatly benefit from having more 
CPU allocated to it.




