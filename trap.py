#!/usr/bin/python3

import json
import sys
import uuid
import os
import argparse

json_input = json.loads(sys.stdin.read())

traceroute_full_path = []

parser = argparse.ArgumentParser()
parser.add_argument('--monitor-name', help='Enter name of monitor. ie: Name of endpoint', required=True)

monitor_name = vars(parser.parse_args())

def jsonHopDocument(hop_number, hop_ip, hop_pct_loss, hop_ping_count, hop_ping_last_ms, hop_ping_avg_ms, hop_ping_best_ms, hop_ping_worst_ms, hop_ping_std_dev, hop_prev_hop):
	data = {}
	
	data['souce_host'] = json_input['report']['mtr']['src']
	data['destination_host'] = json_input['report']['mtr']['dst']
	
	data['current_path_id'] = traceroute_path_identifier
	
	data['monitor_name'] = monitor_name['monitor_name']
	data['mtr_report'] = "hop"


	data['hop_number'] = hop_number
	data['hop_ip'] = hop_ip
	data['hop_pct_loss'] = hop_pct_loss
	data['hop_ping_count'] = hop_ping_count
	data['hop_ping_last_ms'] = hop_ping_last_ms
	data['hop_ping_avg_ms'] = hop_ping_avg_ms
	data['hop_ping_best_ms'] = hop_ping_best_ms
	data['hop_ping_worst_ms'] = hop_ping_worst_ms
	data['hop_ping_std_dev'] = hop_ping_std_dev

	data['prev_hop'] = hop_prev_hop
	
	if hop_ip == "???":
		data['hop_masked'] = "true"
		
	json_data = json.dumps(data, separators=(',', ':'))
	print (json_data)


def jsonFullpathDocument(traceroute_full_path, endpoint_hop_number, endpoint_ip, endpoint_pct_loss, endpoint_ping_count, endpoint_ping_last_ms, endpoint_ping_avg_ms, endpoint_ping_best_ms, endpoint_ping_worst_ms, endpoint_ping_std_dev):
	data = {}
	data['souce_host'] = json_input['report']['mtr']['src']
	data['destination_host'] = json_input['report']['mtr']['dst']
	
	data['current_path_id'] = traceroute_path_identifier
	
	data['monitor_name'] = monitor_name['monitor_name']
	data['mtr_report'] = "fullpath"

	data['mtr_tos'] = json_input['report']['mtr']['tos']
	data['mtr_packet_size'] = json_input['report']['mtr']['psize']
	data['mtr_bitpattern'] = json_input['report']['mtr']['bitpattern']
	data['mtr_ping_count'] = json_input['report']['mtr']['tests']

	data['endpoint_hop_number'] = endpoint_hop_number
	data['endpoint_ip'] = endpoint_ip
	data['endpoint_pct_loss'] = endpoint_pct_loss
	data['endpoint_ping_count'] = endpoint_ping_count
	data['endpoint_ping_last_ms'] = endpoint_ping_last_ms
	data['endpoint_ping_avg_ms'] = endpoint_ping_avg_ms
	data['endpoint_ping_best_ms'] = endpoint_ping_best_ms
	data['endpoint_ping_worst_ms'] = endpoint_ping_worst_ms
	data['endpoint_ping_std_dev'] = endpoint_ping_std_dev

	data['mtr_fullpath'] = traceroute_full_path

	json_data = json.dumps(data, separators=(',', ':'))
	print (json_data)

traceroute_path_identifier = str(uuid.uuid4())

for hop in json_input['report']['hubs']:

	hop_number = hop['count']
	hop_ip = hop['host']
	hop_pct_loss = hop['Loss%']
	hop_ping_count = hop['Snt']
	hop_ping_last_ms = hop['Last']
	hop_ping_avg_ms = hop['Avg']
	hop_ping_best_ms = hop['Best']
	hop_ping_worst_ms = hop['Wrst']
	hop_ping_std_dev = hop['StDev']
	
	
	if not 'hop_prev_hop' in locals():
		hop_prev_hop = json_input['report']['mtr']['src']

	jsonHopDocument(hop_number, hop_ip, hop_pct_loss, hop_ping_count, hop_ping_last_ms, hop_ping_avg_ms, hop_ping_best_ms, hop_ping_worst_ms, hop_ping_std_dev, hop_prev_hop)
	traceroute_full_path.append(hop_ip)
	hop_prev_hop = hop['host']

	if int(hop_number) == int(len(json_input['report']['hubs'])):	
		jsonFullpathDocument(traceroute_full_path, hop_number, hop_ip, hop_pct_loss, hop_ping_count, hop_ping_last_ms, hop_ping_avg_ms, hop_ping_best_ms, hop_ping_worst_ms, hop_ping_std_dev)
		traceroute_path_identifier = str(uuid.uuid4())
