#!/usr/bin/env python
"""
    Object-oriented implementation of backup reporting code.
    Defines a class called 'Backup' that records all backups of a device
"""

import os, sys, argparse
import glob
from configparser import ConfigParser
from atlassian import Confluence

class Backup:
    def __init__(self, device, backup_root):
        self.device = device
        self.root = backup_root
        config_pattern = "{}/*/{}".format(self.root, device)

        configs = glob.glob(config_pattern, recursive=True)
        # Remove the full pathname, we only want the directory and the filename
        bkps = [dir[len(backup_root)+1:] for dir in configs]
        
        self.backups = bkps

    def name(self):
        return self.device

    def latest(self):
        return self.backups[-1]


def main():
    parser = ConfigParser()
    parser.read('/mnt/c/Users/micro/Documents/Computing/dev/code-snippets/python/atlassian/config.ini')
    device_list_file = parser['backups']['device_list']
    apikey = parser['confluence']['apikey']
    username = parser['confluence']['username']
    url = parser['confluence']['url']
    page_ID = parser['confluence']['page_ID']

    confluence = Confluence(url=url,
                            username=username,
                            password=apikey)

    # Read in all the devices from the nominated file
    with open(device_list_file) as file:
        lines = file.readlines()
        devices = [line.rstrip() for line in lines]

    wiki_table = "||Device||Date||" 

    for device in devices:
        device_bkp = Backup(device, parser['backups']['path'])
        print(f"Latest backup for {device_bkp.name()} is {device_bkp.latest()}")
        (date, my_device) = device_bkp.latest().split('/')
        wiki_table += "\n" + f"|{my_device}|{date}|"

    print("Wiki text for table is:")
    print(wiki_table)
    
    result = confluence.update_page(
                                    page_id=page_ID,
                                    title='Config Retrievals',
                                    representation="wiki",
                                    body=wiki_table)

    #pprint(result)
    print(f"Title of page set to '{result['title']}'")
    print(f"Confluence revision for page is now {result['version']['confRev']}") 
    
if __name__ == "__main__":
    main()
        