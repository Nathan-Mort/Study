#!/bin/sh

HH_FILE="../ex03/hh_positions.csv"
UNIQ_POS_FILE="hh_uniq_positions.csv"

{
    echo "\"name\",\"count\"" 
    tail -n +2 "$HH_FILE" | awk -F',' '{print $3}' | sort | uniq -c | sort -nr | awk '{print $2 "," $1}'
} > "$UNIQ_POS_FILE"
