#!/usr/bin/env python
# Simple argparse example with several arguments plus an optional one

import argparse

import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(description='Argparse arguments example')

# Add the arguments
my_parser.add_argument('--boolean-switch',
                       action='store_true',
                       help='a boolean switch to dosomething')


# Execute the parse_args() method
args = my_parser.parse_args()

if args.dosomething:
    print(f"dosomething is set")
else:
    print(f"dosomething is not set")


        
