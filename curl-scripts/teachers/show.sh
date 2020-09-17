#!/bin/bash

curl "http://localhost:8000/teachers/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
