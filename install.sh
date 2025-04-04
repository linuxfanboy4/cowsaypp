#!/bin/bash 
wget https://github.com/linuxfanboy4/cowsaypp.git 
cd cowsaypp 
cd src 
pip install -r requirements.txt
python3 cowsaypp.py
