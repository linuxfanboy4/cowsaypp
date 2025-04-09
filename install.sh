#!/bin/bash 
wget https://github.com/linuxfanboy4/cowsaypp.git 
cd cowsaypp 
cd src 
pip install -r requirements.txt
sudo mv cowsaypp.py /usr/local/bin/cowsaypp
python3 cowsaypp.py
