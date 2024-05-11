#!/bin/bash
# Get status code
data=$(cat "$2") && curl -X POST -s "$1" -d "'$data'"