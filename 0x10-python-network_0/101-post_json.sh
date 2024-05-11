#!/bin/bash
# Get status code
data="$2" && curl -X POST -s "$1" -d "'$(cat "$2")'"
