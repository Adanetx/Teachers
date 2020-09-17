#!/bin/bash

curl "http://localhost:8000/teachers" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "teacher": {
      "name": "'"${NAME}"'",
      "age": "'"${AGE}"'",
      "sex": "'"${SEX}"'",
      "favorite_course": "'"${FAVORITE_COURSE}"'",
      "education": "'"${EDUCATION}"'"
    }
  }'

echo
