#!/bin/bash
# Loop through a sequence of numbers

for i in {1..10}
do
  echo "i is $i"
done

# You can also use 'seq'
END=5
for i in $(seq 1 $END); do echo $i; done

# And if you want leading zeroes this is pretty cute:
for i in {01..05}; do echo "$i"; done