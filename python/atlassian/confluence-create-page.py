#!/usr/bin/env python

from yaml.loader import SafeLoader
from atlassian import Confluence
import yaml

CONFIG_FILE = 'api-key.yml'

with open(CONFIG_FILE, 'r') as config_file:
    config = yaml.load(config_file, Loader=SafeLoader)

apikey = config['confluence']['apikey']
username = config['confluence']['username']
url = config['confluence']['url']

confluence = Confluence(
    url=url,
    username=username,
    password=apikey)

status = confluence.create_page(
    space='MYSTUFF',
    title='This is a test page created by my Python script',
    body='This is the body. You can use <strong>HTML tags</strong>!')

print(status)