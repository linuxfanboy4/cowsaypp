#!/bin/bash 
wget https://github.com/linuxfanboy4/cowsaypp.git 
cd cowsaypp 
cd src 
pip install -r requirements.txt
sudo mv cowsaypp.py /usr/local/bin/cowsaypp
echo "cowsay++ is successfully installed, Installed version is 10.5.3"
