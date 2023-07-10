#!/usr/bin/env python
# Simple argparse example with a single argument, e.g. a filename

import argparse

import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(description='Argparse example')

# Add the arguments
my_parser.add_argument('devicefile',
                       type=str,
                       help='an input file containing device names')

# Execute the parse_args() method
args = my_parser.parse_args()

if args.devicefile:
    print(f"Reading from {args.devicefile}")
else:
    printf(f"Please supply a filename argument")


        