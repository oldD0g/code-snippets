#!/usr/bin/env python
#
# Pretty printing dictionaries
# Super useful because you often get a blob of data, and it can be hard
#  to understand the structure without pretty printing

myd = {'key1': 'somevalue', 'a_list': [0,1,2,3,4 ],
       'another_key': { 'subkey1': 'subvalue1', 'subkey2': 'subvalue2'}}

# If you just print the dict it's just all printed in a line.
print(myd)

# A useful trick is to try to print it with the JSON formatter
import json
print(json.dumps(myd, indent=2))

# But that can break with an error, specifically:
# "TypeError: Object of type datetime is not JSON serializable"
# You can hack this a little by adding a default function of "str"
# that will cast those to string, but that can be a bit blob like too.

print("Contents of dictionary using json.dumps with 'default=str':")
print(json.dumps(myd, indent=2, default=str))

# There is also the Python module pprint, e.g.

import pprint
pp = pprint.PrettyPrinter(indent=4)
print("Contents of dictionary using pprint with 'indent=4':")
pp.pprint(myd)
"""
References:
  https://stackoverflow.com/questions/3229419/how-to-pretty-print-nested-dictionaries
"""