#!/bin/bash
# Precise header parameter in curl
curl -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" -s $1
