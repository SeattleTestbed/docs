"""
Tests memory allocation speed
"""

import threading
import subprocess
import os
import time

# see if the process is over quota and if so terminate with extreme prejudice.
def mem_use(pid):
  # issue this command to ps.   This is likely to be non-portable and a source
  # of constant ire...
  memorycmd = 'ps -p '+str(pid)+' -o rss'
  p = subprocess.Popen(memorycmd, shell=True, stdout=subprocess.PIPE, 
	stderr=subprocess.PIPE, close_fds=True)

  cmddata = p.stdout.read()
  p.stdout.close()
  errdata = p.stderr.read()
  p.stderr.close()
  junkstatus = os.waitpid(p.pid,0)

  # ensure the first line says RSS (i.e. it's normal output
  if 'RSS' == cmddata.split('\n')[0].strip():
    
    # PlanetLab proc handling
    badproccount = 0
  
    # remove the first line
    memorydata = cmddata.split('\n',1)[1]

    # they must have died
    if not memorydata:
      return

    # the answer is in KB, so convert!
    memoryused = int(memorydata)

    return memoryused
  else:
    raise Exception, "Cannot understand '"+memorycmd+"' output: '"+cmddata+"'"

totalcount = 0
totalspeed = 0

class MemInfoThread(threading.Thread):
  frequency = 0.05

  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
	global totalspeed, totalcount
  	pid = os.getpid()
  	start = time.time()
	memlast = mem_use(pid)
	timelast = time.time()
	

	print "PID: ", str(pid)
	  	
  	while True:
  		mem = mem_use(pid)
  		speed = (mem-memlast)/(time.time() - timelast)
  		print str(time.time() - start), "Mem: ", str(mem), "Kb/s: ", str(speed)
  		memlast = mem
  		timelast = time.time()
  		totalspeed = totalspeed + speed
  		totalcount = totalcount + 1
  		time.sleep(self.frequency)


class MemUseThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
	arr = []
	while True:
		# Use lots of memory very fast
  		arr.append(42)

# Monitor mem usage
thread = MemInfoThread()
thread.start()

# Go crazy!
thread2 = MemUseThread()
thread2.start()

# Only allow running for a few seconds to keep system functional
time.sleep(4)

# Print the results
print "Avg Kb/s: ", str(totalspeed/totalcount)

# Force quit
exit()
