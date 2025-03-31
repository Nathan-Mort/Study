#!/bin/sh

echo "pandas" > requirements.txt
echo "numpy" >> requirements.txt
echo "ipykernel" >> requirements.txt
echo "statsmodels" >> requirements.txt
echo "seaborn" >> requirements.txt
echo "matplotlib" >> requirements.txt
echo "scikit-learn" >> requirements.txt


python3 -m venv venom

source venom/bin/activate

pip install -r requirements.txt

python3 -m ipykernel install --user --name=envi --display-name "venom"

rm requirements.txt