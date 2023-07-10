#!/usr/bin/env python
# Simple argparse example with a single Boolean switch

import argparse

import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(description='Argparse switch example')

# Add the arguments
my_parser.add_argument('--dosomething',
                       action='store_true',
                       help='a boolean switch to dosomething')

# Execute the parse_args() method
args = my_parser.parse_args()

if args.dosomething:
    print(f"dosomething is set")
else:
    print(f"dosomething is not set")


        
