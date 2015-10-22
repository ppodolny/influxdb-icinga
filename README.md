# influxdb-icinga
Influxdb plugin for Icinga (and Nagios)
----------------------------------------

Installation:
-------------
pip install -r requirements.txt

Usage:
------

Simple, Influxdb plugin for Icinga/Nagios

  -h, --help            show this help message and exit
  -c CRITICAL, --critical CRITICAL
                        critical threshold
  -w WARNING, --warning WARNING
                        warning threshold
  -m METRIC, --metric METRIC
                        metric name
  -I INFLUXHOST, --influxhost INFLUXHOST
                        host or ip of influxdb
  -H HOST, --host HOST  host or ip to fetch data for
  -P PORT, --port PORT  port of influxdb api
  -u USERNAME, --username USERNAME
                        influxdb db username
  -p PASSWORD, --password PASSWORD
                        influxdb db password
  -d DATABASE, --database DATABASE
                        influxdb db name
  -n, --negate



Example:
-------
./check_influx.py -c 90 -w 80 -m memory.memory-used -I influxdb02 -H influxdb02  -d graphite 

Output is provided as perf. data , exit status is compatible with Nagios/Icinga: 0=OK, 1=WARNING, 2=CRITICAL, 3=UNKNOWN

OK|memory.memory-used=331220519.856710
