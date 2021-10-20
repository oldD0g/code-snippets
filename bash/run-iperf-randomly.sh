#!/bin/sh
# Run iperf randomly to generate traffic
# Assumes you have a server set up already, this only runs the client

TARGET=10.1.1.2
SLEEPMAX=3
RUNMAX=10

while [ 1 ]; do
    sleepTime=$((1 + $RANDOM % SLEEPMAX))
    runTime=$((1 + $RANDOM % $RUNMAX))
    echo "Running iperf client for $runTime seconds..."
    iperf -t $runTime -c ${TARGET}
    echo "Sleeping for $sleepTime seconds..."
    sleep $sleepTime
done