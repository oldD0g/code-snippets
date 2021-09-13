#!/usr/bin/env python
# Check on when a device was last backed up, by reporting the most recent file
# containing that device name

import argparse

import os
import sys
import glob
from yaml.loader import SafeLoader
from atlassian import Confluence
from pprint import pprint
import yaml

CONFIG_FILE = '../api-key.yml'

with open(CONFIG_FILE, 'r') as config_file:
    config = yaml.load(config_file, Loader=SafeLoader)

apikey = config['confluence']['apikey']
username = config['confluence']['username']
url = config['confluence']['url']

# Create the parser
my_parser = argparse.ArgumentParser(description='Report on configs')

# Add the arguments
my_parser.add_argument('devicefile',
                       type=str,
                       help='an input file containing device names')

my_parser.add_argument('configdir',
                       type=str,
                       help='the folder where config files are found')

# Execute the parse_args() method
args = my_parser.parse_args()

# todo: Check that devicefile and configdir are readable
if args.devicefile:
    print(f"Reading from {args.devicefile}")
else:
    printf(f"Please supply a filename argument")

# Read in all the devices from the nominated file
with open(args.devicefile) as file:
    lines = file.readlines()
    devices = [line.rstrip() for line in lines]

latest_configs = {}

# Use glob to find the latest config file for each device
# todo: Set to "Not found" if there is no such file
for device in devices:
    print(f"Checking device {device}")
    config_pattern = "*/{}".format(device)
    configs = glob.glob(config_pattern, recursive=True)
    print(f"Latest config file for {device} is {configs[-1]}")
    latest_date = configs[-1].split('/')[0]
    latest_configs[device] = latest_date

wiki_table = "||Device||Date||"
for device, date in latest_configs.items():
    print(f"Creating row for {device} with date {date}")
    wiki_table += "\n" + f"|{device}|{date}|"

print("Wiki text for table is:")
print(wiki_table)

page_ID = 1703937
confluence = Confluence(
    url=url,
    username=username,
    password=apikey)

# Using representation "wiki" allows wikitext, normally this would be "page"
result = confluence.update_page(
    page_id=page_ID,
    title='Config Retrievals',
    representation="wiki",
    body=wiki_table)

#pprint(result)
print(f"Title of page set to '{result['title']}'")
print(f"Confluence revision for page is now {result['version']['confRev']}") 


