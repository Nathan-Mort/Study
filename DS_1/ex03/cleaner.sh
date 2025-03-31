#!/bin/sh

HH_FILE="../ex02/hh_sorted.csv"
HH_POS_FILE="hh_positions.csv"

{
    # Выводим заголовки
    head -n 1 "$HH_FILE"
    # Обрабатываем данные
    tail -n +2 "$HH_FILE" | awk -F',' '
    {
        original = $3;
        
        # gsub(r, s [, t]) Каждую подстроку в строке t удовлетворяющую выражению r заменить на строку s. 
        # Фичв awk  заменяем все запятые на пробелы
        gsub(/,/, " ", original);

        position = "\"-\"";
        if ($3 ~ /Junior/) position = "\"Junior\"";
        if ($3 ~ /Middle/) position = (position == "\"-\"" ? "" : position "/") "\"Middle\"";
        if ($3 ~ /Senior/) position = (position == "\"-\"" ? "" : position "/") "\"Senior\"";

        print $1 "," $2 "," position "," $4 "," $5;
    }'
} > "$HH_POS_FILE"
