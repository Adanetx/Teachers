#!/bin/bash

curl "http://localhost:8000/teachers/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
