#!/usr/bin/env python
"""
  How to count the number of elements in a generator.
  Two warnings: 
    One, if you do this you have to re-create the
    generator afterwards, as the counting will consume it.
    Two, don't do most of these with an infinite generator,
    e.g. Fibonacci numbers, as obviously that can't be counted.

  In this example I'll use a realistic generator, from pathlib,
  that lists all the files in /etc.  Realistic in that it's
  a usage of pathlib that is meaningful, but also clearly finite.
"""

from pathlib import Path

etc_generator = Path('/etc').glob('**/*')

num_of_files = sum(1 for _ in etc_generator)
print(f"Found {num_of_files} files in /etc by counting Path generator")

# If you want to use the generator, after printing out
# that summary, you need to replenish it.
# Alternatively, in an example like this, you could turn
#  the result into a list, count the list, and then process
#  the list.  This is reasonable when you know the list will
#  be of a reasonable size. (Famous last words!)

etc_files_list = list(Path('/etc').glob('**/*'))

print("Found {} files in /etc from list".format(len(etc_files_list)))

