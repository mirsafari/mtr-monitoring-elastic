# mtr-monitoring-elastic
Inspired by: (https://github.com/svdasein/logstash-codec-mtrraw)

trap is a python script that takes input from MTR in json format, adds additional fields and than sends MTR reports to logstash via nc.  Works with mtr 0.92, ELK stack 7.8.0. 

# Installation: 
```
git clone https://github.com/mirsafari/mtr-monitoring-elastic.git
```
```
docker build . -t mtr-monitoring-elastic
```
# Usage:
Run signe container per monitored endpoint and change environment variables to suit your needs
```
docker run -dit --name mtr-monitoring-elastic-google-dns \
  -e PING_COUNT='10' \
  -e TARGET_IP='8.8.8.8' \
  -e MONITOR_NAME='GoogleDNS' \
  -e LOGSTASH_IP='10.10.10.10' \
  -e LOGSTASH_PORT='12345' \
  -e MONITORING_INTERVAL='60' \
  --network host \
  trap
```
Example of logstash setup
```
input {
  tcp {
    port => 12345
    codec => json
  }
}

output {
    elasticsearch {
      hosts => ["10.10.10.10:9200""]
      index => "mtr-monitoring-elastic-%{+YYYY.MM.dd}"
    }
}
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
