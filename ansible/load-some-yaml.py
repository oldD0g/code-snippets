#!/usr/bin/env python

import yaml
import json
import sys

if len(sys.argv) != 2:
    print("Usage: {} <filename.yml>".format(sys.argv[0]))
    sys.exit()

with open(sys.argv[1], "r") as stream:
    try:
        my_yaml = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

print("Loaded YAML from {} successfully".format(sys.argv[1]))

print(json.dumps(my_yaml, indent=2))
