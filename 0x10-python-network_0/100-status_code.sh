#!/bin/bash
# Get status code
curl -sI -o /dev/null -w "%{http_code}" "$1" 
