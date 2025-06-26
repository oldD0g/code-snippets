#!/bin/env python
"""
Load a JSON file
"""

import argparse
import json

my_parser = argparse.ArgumentParser(description='Load JSON formatted file')

my_parser.add_argument('inputfile',
                       type=str,
                       help='an input file in JSON format')

args = my_parser.parse_args()

if args.inputfile:
    print(f"Reading from {args.inputfile}")
else:
    printf(f"Please supply a filename argument")

#filename = "somefile.json"

with open(args.inputfile, encoding='utf-8') as data_file:
   data = json.load(data_file)

print("Loaded JSON file {} successfully, length {}".format(args.devicefile, len(data)))
print("This file contains these keys:")
for my_key in data.keys():
    print("  - {}".format(my_key))

