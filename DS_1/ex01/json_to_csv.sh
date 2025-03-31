#!/bin/bash

JSON_FILE="../ex00/hh.json"
CSV_FILE="hh.csv"
JQ_FILE="filter.jq"
{
    echo "\"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\""
    jq -f -r "$JQ_FILE" "$JSON_FILE" 
} >"$CSV_FILE"


