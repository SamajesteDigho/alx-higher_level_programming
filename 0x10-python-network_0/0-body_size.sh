#!/bin/bash
# Collect the size of an http response
curl -sI $1 | grep -i Content-Length | awk '{print $2}'
