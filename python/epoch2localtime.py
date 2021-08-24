#!/usr/bin/env python
# Convert epoch time to localtime
# e.g. ./epoch2localtime.py 1629702731

import sys  # So I can do simple argument processing
import time

if len(sys.argv) != 2:
    print("Usage: {} epoch-time".format(sys.argv[0]))
    sys.exit()

print("Converting epoch {} into localtime".format(sys.argv[1]))
print(time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(float(sys.argv[1]))))