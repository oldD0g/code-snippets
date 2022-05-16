#!/bin/sh
# Ping a target a bit randomly with random packet sizes and sleeps to generate traffic
# Pure Bourne shell for those GNS3 Linux boxes

TARGET=192.168.86.39
SLEEPMAX=5
RUNMAX=10

while [ 1 ]; do
  rnd1=$RANDOM
  if [ -z "$rnd1" ]  # Bourne, Dash don't have $RANDOM
  then
    rnd1=`hexdump -n 2 -e '/2 "%u"' /dev/urandom`
  fi
  rnd2=$RANDOM
  if [ -z "$rnd2" ]
  then
    rnd2=`hexdump -n 2 -e '/2 "%u"' /dev/urandom`
  fi
  
  sleepTime=`expr $rnd1 % $SLEEPMAX`
  runTime=`expr $rnd2 % $RUNMAX`
  runTime=`expr $runTime + 1` # Because 0 means forever
  
  echo "Running ping for $runTime seconds then sleeping for $sleepTime"
  pktSize=$RANDOM
  ping -w $runTime -s $pktSize $TARGET
  
  sleep $sleepTime
  
done
