#!/bin/bash
# Get status code
curl -s "$1" | grep -i "you got me!"
