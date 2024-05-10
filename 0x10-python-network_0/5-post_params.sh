#!/bin/bash
# Precise header parameter in curl
curl -X POST -s $1 -H "Content-Type: application/json" -d '{"email": "test@gmail.com", "subject": "I will always be here for PLD"}'
