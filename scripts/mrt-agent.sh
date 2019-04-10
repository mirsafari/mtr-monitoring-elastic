#!/usr/bin/env sh

while true; do mtr -r -w -j -n -c $PING_COUNT $TARGET_IP | /scripts/trap.py --monitor-name $MONITOR_NAME | nc -w 30 $LOGSTASH_IP $LOGSTASH_PORT; sleep $MONITORING_INTERVAL; done
