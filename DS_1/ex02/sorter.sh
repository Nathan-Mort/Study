#!/bin/bash

HH_CSV="../ex01/hh.csv"
SORT_HH="hh_sorted.csv"

{
    head -n 1 "$HH_CSV"

    tail -n +2 "$HH_CSV" | sort -t',' -k2,2 -k1,1n 
} > "$SORT_HH"
