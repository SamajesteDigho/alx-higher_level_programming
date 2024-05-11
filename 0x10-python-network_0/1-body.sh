#!/bin/bash
# Display the body of a curl request
curl -sI $1 | grep -i "HTTP" | [[ $(awk '{print $2}') -eq 200 ]] && curl -s $1
