#!/bin/bash
# Allowed requests
curl -si $1 | grep -i Allow | awk '{print $2}'
