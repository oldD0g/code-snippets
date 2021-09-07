#!/usr/bin/env python 

from yaml.loader import SafeLoader
from atlassian import Confluence
import yaml
from pprint import pprint

CONFIG_FILE = 'api-key.yml'

with open(CONFIG_FILE, 'r') as config_file:
    config = yaml.load(config_file, Loader=SafeLoader)

apikey = config['confluence']['apikey']
username = config['confluence']['username']
url = config['confluence']['url']

#print(f"Fetched {apikey} to authenticate...")

confluence = Confluence(
    url=url,
    username=username,
    password=apikey)

# Get all pages from Space
# content_type can be 'page' or 'blogpost'. Defaults to 'page'
# expand is a comma separated list of properties to expand on the content.
# max limit is 100. For more you have to loop over start values.
space_name = "MYSTUFF"
pages = confluence.get_all_pages_from_space(space_name, start=0, limit=100, status=None, expand=None, content_type='page')

print(f"Pages in space {space_name}:")
for item in pages:
    print(item['title'])

#pprint(pages)