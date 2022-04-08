#!/usr/bin/env python
"""
  Just a simple example to start - connect to a v1.8 IUnfluxDB and list the
  available measurements in the Telegraf database.
"""

from influxdb import InfluxDBClient

influx_host = '192.168.86.27'

client = InfluxDBClient(host=influx_host, 
      port=8086, 
      database='telegraf')

if client:
  print("Connected successfully")
else:
  print("Failed to connect to Influx on {}".format(influx_host))

databases = client.get_list_database()

if databases:
  for key in databases:
    print(f"Got DB {key['name']}")
else:
  print("ERROR:Failed to retrieve database list!")

client.switch_database('telegraf')

results = client.query('SHOW MEASUREMENTS')
for measurement in results.raw['series'][0]['values']:
  print(f"Measurement: {measurement[0]}")