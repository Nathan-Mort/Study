#!/bin/sh

HH_FILE="../ex03/hh_positions.csv"

header=$(head -n 1 "$HH_FILE")

tail -n +2 "$HH_FILE" | while IFS=',' read -r id created_at name has_test alternate_url; do

    date=$(echo "$created_at" | cut -d'T' -f1)

    if [ ! -f "$date.csv" ]; then
        echo "$header" > "$date.csv"  
    fi

    echo "$id,$created_at,$name,$has_test,$alternate_url" >> "$date.csv"
done