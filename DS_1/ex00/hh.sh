#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Использование: $0 <название вакансии>"
    exit 1
fi

VACANCY_NAME="${1// /%20}"

URL="https://api.hh.ru/vacancies"

PARAMS="?text=${VACANCY_NAME}&per_page=20"

TEMP_FILE=$(mktemp)
curl --silent "${URL}${PARAMS}" > "$TEMP_FILE"

jq '.' "$TEMP_FILE" > hh.json

rm "$TEMP_FILE"

