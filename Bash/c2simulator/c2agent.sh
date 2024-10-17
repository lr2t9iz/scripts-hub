#!/bin/bash
## hello world

C2Server="172.31.86.238"
C2Port="8080"

beacon() {
	req=$(curl -s -XGET "http://$C2Server:$C2Port")
	echo -e "Ping to c2 $C2Server:$C2Port \
Server answer: $req"
}

while true; do
	beacon
	sleep 5 # Sleep Timers
	# Uncomment the line below to add Jitter
	# sleep $((RANDOM % 10 + 5)) # Jitter
done
