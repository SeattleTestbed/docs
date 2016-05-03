"""
<Program Name>
  build_connectivity_map.py

<Started>
  November 17, 2008

<Author>
  ivan@cs.washington.edu
  Ivan Beschastnikh

  Rewrite by Justin Cappos on Nov 6th, 2010.

<Purpose>
  Builds a simple, random connectivity mesh between a set of nodes.

  Takes a file with hostnames and outputs a list of lines that look like:
  srcip1 destip1
  srcip2 destip2
  ...

  The output graph is asymmetric, so if you see srcip1 destip1, you won't see
  destip1 srcip1.   The reason for this is to make it easier for the person
  using the graph to decide which node should initiate the TCP connection.
"""




import sys
import random



def build_map(hosts):
  """
  Takes a list of hosts and returns a list of tuples of hosts. The graph 
  will be connected and have between n-1 and n*n-1 / 4 edges.
  """
  conn_map = []
  random.shuffle(hosts)
  numhosts = len(hosts)

  # create an initial chain of connected nodes so that our map is
  # guaranteed to be connected no matter what happens
  for hostpos in range(numhosts - 1):
    conn_map.append((hosts[hostpos], hosts[hostpos+1]))


  # This should mean that at most 1/2 of the edges will be in the graph.
  # We previously added numhosts -1
  for linkattemptcount in range(numhosts*(numhosts-1)/4 - numhosts -1):

    # choose hosts randomly...
    host1 = random.sample(hosts,1)[0]
    host2 = random.sample(hosts,1)[0]

    # no links to the same node...
    if host1 == host2:
      continue
    # the link exists.
    if (host1,host2) in conn_map or (host2,host1) in conn_map:
      continue

    conn_map.append((host1,host2))
          
  return conn_map

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print "usage: " + sys.argv[0] +" [filename]"
    sys.exit(1)

  # read the hosts file containing one hostname/ip per line
  f = open(sys.argv[1],"r")
  lines = f.readlines()
  f.close()
  hosts = []
  for line in lines:
    hosts.append(line.strip())

  # build the connectivity map
  conn_map = build_map(hosts)

  conn_map.sort()
  # output the connectivity map to stdout
  for src_host, dst_host in conn_map:
    print str(src_host) + " " + str(dst_host)
