#!/bin/bash
# Get status code
curl -X POST -s "$1" -d "'$(cat "$2")'"