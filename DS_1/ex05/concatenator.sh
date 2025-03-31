#!/bin/sh

OUTPUT_FILE="combined.csv"

first_file=$(ls *.csv | head -n 1)
header=$(head -n 1 "$first_file")

echo "$header" > "$OUTPUT_FILE"

for file in *.csv; do
    if [ "$file" != "$OUTPUT_FILE" ]; then
        tail -n +2 "$file" >> "$OUTPUT_FILE"
    fi
done
