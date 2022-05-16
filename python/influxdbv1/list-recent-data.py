#!/usr/bin/env python
"""
  Just a simple example to start - connect to a v1.8 InfluxDB and list the
  available measurements in the Telegraf database.

  Doco for this client is at: https://github.com/influxdata/influxdb-python
"""

import argparse
from influxdb import InfluxDBClient
from datetime import datetime
import sys

my_parser = argparse.ArgumentParser(description='Influx value tester')

# Add the arguments
my_parser.add_argument('--database', '-d', type=str, help='Database name', required=True)
my_parser.add_argument('--measurement', '-m', type=str, help='Measurement', required=True)
my_parser.add_argument('--limit', '-l', type=str, help='Limit - number of measurements', required=True)

# Execute the parse_args() method
args = my_parser.parse_args()

if args.database:
  print(f"Database selected is {args.database}")

influx_host = '192.168.86.27'

client = InfluxDBClient(host=influx_host, 
      port=8086, 
      database=args.database)

if not client:
  print("Failed to connect to Influx on {}".format(influx_host))
  sys.exit("Quitting!")

databases = client.get_list_database()

if not databases:
  print("ERROR:Failed to retrieve database list!")
  sys.exit("Quitting!")

client.switch_database(args.database)

results = client.query('select ifOutOctets, ifDescr from {} where ifDescr = \'GigabitEthernet1\'limit {}'.format(
                        args.measurement, args.limit
))
last_time = 0

print("Result is: {}".format(results))

for value in results.get_points():
  print(f"Measurement: {value['time']} {value['ifOutOctets']} {value['ifDescr']}")
  if last_time == 0:
    last_time = datetime.strptime(value['time'], "%Y-%m-%dT%XZ")
  else:
    this_time = datetime.strptime(value['time'], "%Y-%m-%dT%XZ")
    interval = this_time - last_time
    print("Interval since last measurement is: {}".format(interval))
    last_time = this_time

"""
for value in results.raw['series'][0]['values']:
  print(f"Measurement: {value[0]} {value[1]} {value[2]}")
  if last_time == 0:
    last_time = datetime.strptime(value[0])
  else:
    this_time = 
    interval = datetime.strptime(value[0]) - last_time
    print("Interval since last measurement is: {}".format(interval))
    last_time = 
"""
