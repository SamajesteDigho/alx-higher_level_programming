#!/bin/bash
# Allowed requests
curl -sI $1 | grep -i Allow | awk '{print $2}'
