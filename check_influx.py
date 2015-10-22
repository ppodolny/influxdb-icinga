#!/usr/bin/env python

# Icinga/Nagios plugin for InfluxDB polling
# paul.podolny@gmail.com

import argparse
from influxdb import client as influxdb
import sys


#static cfg
time_window='10s'
domainname='nrgene.local'

#match graphite syntax 
domainname=domainname.replace(".","_")

parser = argparse.ArgumentParser(description='Simple, Influxdb plugin for Icinga/Nagios')
parser.add_argument('-c','--critical', help='critical threshold', required=True)
parser.add_argument('-w','--warning', help='warning threshold', required=True)
parser.add_argument('-m','--metric', help='metric name', required=True)
parser.add_argument('-I','--influxhost', help='host or ip of influxdb', required=True)
parser.add_argument('-H','--host', help='host or ip to fetch data for', required=True)
parser.add_argument('-P','--port', help='port of influxdb api', required=False)
parser.add_argument('-u','--username', help='influxdb db username', required=False)
parser.add_argument('-p','--password', help='influxdb db password', required=False)
parser.add_argument('-d','--database', help='influxdb db name', required=True)
parser.add_argument('-n','--negate', action='store_true')
parser.set_defaults(negate=False)
parser.set_defaults(port=8086)
parser.set_defaults(username="root")
parser.set_defaults(password="root")

args = parser.parse_args()
crit_threshold=args.critical
warn_threshold=args.warning
metric=args.metric
username=args.username
password=args.password
database=args.database
port=args.port
influx_host=args.influxhost
host=args.host
negate=args.negate

value=''
query="select mean(value) from /"+host+"_"+domainname+"."+metric+"/ where time < now() - "+time_window

try:
  db = influxdb.InfluxDBClient(influx_host, port, username, password, database)
  result = db.query(query)
  value = list(result)[0][0]["mean"]
except Exception as e:
      sys.exit("[error] Could not connect to Influxdb")

if not value:
  sys.exit("[error] Received empty value from Influxdb")

if negate == True:
        if value <= crit_threshold:
                print "CRITICAL|%s=%f" % (metric, value)
                sys.exit(2)
        elif value > crit_threshold and value <= warn_threshold:
                print "WARNING|%s=%f" % (metric, value)
                sys.exit(1)
        elif value > warn_threshold:
                print "OK|%s=%f" % (metric, value)
                sys.exit(0)
        else:
                print "UNKNOWN"
                sys.exit(3)
else:
        if value >= crit_threshold:
                print "CRITICAL|%s=%f" % (metric, value)
                sys.exit(2)
        elif value < crit_threshold and value >= warn_threshold:
                print "WARNING|%s=%f" % (metric, value)
                sys.exit(1)
        elif value < warn_threshold:
                print "OK|%s=%f" % (metric, value)
                sys.exit(0)
        else:
                print "UNKNOWN"
                sys.exit(3)
