#!/bin/bash
# Allowed requests
curl -siLI $1 | grep -i Allow | awk '{print $2}'
