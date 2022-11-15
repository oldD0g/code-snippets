#!/bin/env python
"""
Load a JSON file
"""

import json

filename = "somefile.json"

with open(filename, encoding='utf-8') as data_file:
   data = json.load(data_file)
