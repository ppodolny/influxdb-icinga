# influxdb-icinga
Influxdb plugin for Icinga (and Nagios)
----------------------------------------

Installation:
-------------
pip install -r requirements.txt

Usage:
------

./check_influx.py -h


Example:
-------
./check_influx.py -c 90 -w 80 -m memory.memory-used -I influxdb02 -H influxdb02  -d graphite 

Output is provided as perf. data , exit status is compatible with Nagios/Icinga:

OK|memory.memory-used=331220519.856710

0=OK, 1=WARNING, 2=CRITICAL, 3=UNKNOWN


