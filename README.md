# trap
Inspired by: (https://github.com/svdasein/logstash-codec-mtrraw)

trap is a python script that takes input from MTR in json format, adds additional fields and than sends MTR reports to logstash via nc.  Works with mtr 0.92, ELK stack 6.6.1. 

# Installation: 
```
git clone https://github.com/mirsafari/trap.git
```
```
docker build . -t trap
```
# Usage:
Run signe container per monitored endpoint and change environment variables to suit your needs
```
docker run -dit --name trap-google-dns \
  -e PING_COUNT='10' \
  -e TARGET_IP='8.8.8.8' \
  -e MONITOR_NAME='GoogleDNS' \
  -e LOGSTASH_IP='10.10.10.10' \
  -e LOGSTASH_PORT='12345' \
  -e MONITORING_INTERVAL='60' \
  --network host \
  trap
```
# Details
Script generates two document types: mtr_report: hop and mtr_report: fullpath. Hop, as the name suggests, contains information about each hop (hop_pct_loss, hop_number, etc.), while fullpath contains information only about enpoint related metrics (as well as some other things like mtr_fullpath, mtr_packet_size etc.). Mtr is used with following flags:
```
mtr -r -w -j -n -c 1 IP.ADD.RE.SS 
 -r -> output using report mode
 -w -> output wide report
 -c -> set the number of pings sent (can be specified using environment variable)
 -j -> output json
 -n -> do not resove host names
```
