#!/bin/sh

# python3 -m pip install termgraph

if [ -z "$VIRTUAL_ENV" ]; then
    echo "Virtual environment is not activated"
else
    termgraph data.csv --color {green,red} --delim ','
fi
