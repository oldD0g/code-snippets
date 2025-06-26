#!/usr/bin/env python
# Simple argparse example with a couple of arguments and an optional argument.
# Example usage:
#  ./argparse-optional-argument.py --action delete --input_file testfile
#  OR
# ./argparse-optional-argument.py --action delete --input_file testfile 42

import argparse

import os
import sys

# Create the parser
description=("This is an argparse example, with two "
    "mandatory arguments, and an optional 'line' argument if needed.")
my_parser = argparse.ArgumentParser(description=description)

# Add the arguments
my_parser.add_argument('--action',
                       type=str,
                       help='the action to take with the file')

my_parser.add_argument('--input_file',
                       action='store',
                       help='the name of the file to act on')

my_parser.add_argument('line', nargs='?',
                       help='an optional line in the input file to start from')

# If no arguments are provided, print help
if len(sys.argv) == 1:
    my_parser.print_help(sys.stderr)

# Execute the parse_args() method
args = my_parser.parse_args()

if args.input_file:
    print(f"Input file argument received: {args.input_file}")
else:
    print(f"Please supply an 'input_file' argument")

if args.action:
    print(f"Action switch received: {args.action}")
else:
    print("No action specified.")

if args.line:
    print(f"Line specified: {args.line}")
else:
    print("No line specified.")


        
