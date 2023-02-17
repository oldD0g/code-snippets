#!/bin/bash
# Very simple arg processing
# See also: https://tldp.org/LDP/abs/html/internalvariables.html#ARGLIST
# Some code copied from there directly

echo "Number of args is: $#"

echo "Listing args with \"\$@\":"
for arg in "$@"
do
  echo "Arg #$index = $arg"
  let "index+=1"
done             # $@ sees arguments as separate words. 
echo "Arg list seen as separate words."

echo "Argument number one is:"
if [ ! -n "$1" ]
then
  echo "Not defined"
else
  echo "$1"
fi
