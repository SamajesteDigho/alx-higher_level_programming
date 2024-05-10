#!/bin/bash
# Allowed requests
curl -sI $1 | awk '/Allow:/ {print $2}'
