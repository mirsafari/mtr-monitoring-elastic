#!/usr/bin/env bash

PING_COUNT=$1
TARGET_IP=$2
MONITOR_NAME=$3
LOGSTASH_IP=$4
LOGSTASH_PORT=$5
MONITORING_INTERVAL=$6

if [ -z "$1" ] ; then
        echo "USAGE:"
        echo "$0 <PING_COUNT> <TARGET_IP>"
        exit
fi

while true ; do
        mtr -r -w -j -n -z -c $PING_COUNT $TARGET_IP | ./trap.py --monitor-name $MONITOR_NAME | nc -w $LOGSTASH_IP $LOGSTASH_PORT;
        sleep $MONITORING_INTERVAL;
done
