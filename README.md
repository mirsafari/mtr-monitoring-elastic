# trap
Python script that takes input from MTR in json format, adds additional fields and than sends MTR reports to logstash via nc. Script generates two document types: mtr_report: hop and mtr_report: fullpath. Hop, as the name suggests, contains information about each hop (hop_pct_loss, hop_number, etc.), while fullpath contains information only about enpoint related metrics (as well as some other things like mtr_fullpath, mtr_packet_size etc.). Works with mtr 0.92, ELK stack 6.6.1. 

MTR accepted output:

mtr -r -w -c 1 -j -n -z IP.ADD.RE.SS | ./mtr_parser.py --monitor-name Endpoint-Name

-r -> output using report mode
-w -> output wide report
-c -> set the number of pings sent
-j -> output json
-n -> do not resove host names
-z -> display AS number
