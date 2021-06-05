#!/bin/bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"author": "Anonymous", "comment": "is that cover at least used as a heatsink?", "imageurl": "https://dcdn.org/g/1622865285989.png"}' \
  http://localhost:5000/g/thread/81931054