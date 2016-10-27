# Running the Security Layer Benchmarks

## Setup
First it is necessary to setup a folder to run the benchmarks. This can be done like so:

```
cd $SEATTLE/branches/repy_v2/
mkdir bench/
python preparetest.py bench
cp benchmarking-support/* bench/
```

## Running the Benchmarks
Each type of benchmark has it's own script to initiate the benchmarks.
 * To run the basic overhead tests, invoke ./benchmark.sh
 * To run the allpairsping test, invoke ./benchmark-allpairs.sh
 * To run the richards test, invoke ./benchmark-richards.sh
 * To run the webserver tests, run ./benchmark-webserver.sh and then ./benchmark-webserver-meg.sh
 * To run the blocking storage server tests, run ./benchmark-blockstore.py

Each benchmark file has some configurable settings that can be edited. For example, the number and type of security layers to benchmark with may be changed. This is done by changing the constants in the bash files.

All benchmarks can be found at: [browser:seattle/branches/repy_v2/benchmarking-support/ benchmarking-support].

## Instructions for benchmark-blockstore.py
Change the arguments of blockstore.py to the prefix of your public/private keys and a valid port number (e.g, 12345).
For example, if your keys are my_name.publickey and my_name.privatekey, the first argument would be my_name.
