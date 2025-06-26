#!/usr/bin/env python
"""
This example looks to find all the connection related information
from Ansible files, so that netmiko could then be used to connect
to the device.

It uses suggestions from
https://github.com/Shourai/til/blob/master/ansible/using-ansible-inventory-in-python.md

One point to note is that this is using unsuppported Ansible interfaces. But
this is probably still arguably better than writing everything from scratch.

"""

from argparse import ArgumentParser
from getpass import getpass
from pathlib import Path
import json
import re
import sys

from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.parsing.vault import VaultSecret, PromptVaultSecret
from ansible.errors import AnsibleParserError # thrown for vault decryption error

from netmiko import ConnectHandler

ANSIBLE_DIR_TOP = f'{Path.home()}/ansible-hosts'

parser = ArgumentParser(description="Device Connection Tool using Netmiko")

parser.add_argument('--host',
                    action='store',
                    help="Host to connect to")

args = parser.parse_args()

if not args.host:
    print("Host not supplied")
    parser.print_help(sys.stderr)
    sys.exit(1)
    
vault_password = getpass("Vault Password: ")
    
target_host = args.host
    
inventory_paths = Path(ANSIBLE_DIR_TOP).\
            glob('**/ansible/inventory.yml')
       
dl = DataLoader()
dl.set_vault_secrets([('default', 
                       PromptVaultSecret(bytes(vault_password, encoding='utf-8')),)])
     
for inv_path in inventory_paths:
    im = InventoryManager(loader=dl, sources=str(inv_path))
    
    hosts = im.get_hosts()
    hostname_list = [vars(host_obj)['name'] for host_obj in hosts]
    # print(f"Found hosts: {hostname_list} in inventory file {inv_path}")
    
    if target_host in hostname_list:
        print(f"Found host {target_host} in inventory file {inv_path}")
        my_host = im.get_host(target_host)
        break

vm = VariableManager(loader=dl, inventory=im)
try:
    my_vars = vm.get_vars(host=my_host)
except AnsibleParserError as e:
    print(f"ERROR: Password could not decrypt vault for host {target_host}")
    sys.exit(1)
    
print(json.dumps(my_vars, indent=2))
