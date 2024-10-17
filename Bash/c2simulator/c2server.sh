#!/bin/bash

## hello world

C2IP="0.0.0.0"
C2PORT=8080

if ! command -v nc &> /dev/null; then
    echo "Error: netcat (nc) not found."
    exit 1
fi

function cleanup {
    echo "C2 Stopped."
    exit 0
}

trap cleanup SIGINT SIGTERM

echo -e "C2 Starting: $(hostname -I):$C2PORT"
while true; do
    {
	    echo -e "HTTP/1.1 200 OK"
        echo -e "Content-Type: text/plain"
        echo -e ""
        echo -e "Hello from Bash Server!"
    } | nc -l -p $C2PORT -s $C2IP -q 1
done
