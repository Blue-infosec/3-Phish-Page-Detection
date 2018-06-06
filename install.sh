#!/bin/bash

echo "check your python and pip version first"
python3 --version
pip3 --version

echo "Install dependences"

echo "Install tesseract OCR, package name:tesseract or tesseract-OCR"
#https://github.com/tesseract-ocr/tesseract/wiki
sudo apt-get update


sudo apt-get install tesseract-ocr

echo "Your installed tesseract is located at:"
which tesseract
echo "Please make sure it should be in /usr/bin/tesseract!"
echo "Did you check this?"

read -p "Continue (y/n)?" choice
case "$choice" in
  y|Y ) echo "yes, bingo! :)";;
  n|N ) echo "no -ehhh some bad thing might happen";;
  * ) echo "invalid - wow";;
esac


sleep 3

sudo apt-get install python-tk

sudo apt-get clean

echo "Clean ......"

sleep 3

echo "Install your python dependences"

sudo pip3 install -U pytesseract==0.2.0

echo "Install libraries needed for feature extraction"
sudo pip3 install -U beautifulsoup4==4.6.0
sudo pip3 install -U autocorrect==0.3.0
sudo pip3 install -U nltk==3.2.1


echo "Begin to download nltk data"
sleep 5
python3 -m nltk.downloader all


echo "Install libraries needed for machine learning"
sleep 3
sudo pip3 install -U numpy==1.14.1
sudo pip3 install -U scipy==0.19.1
sudo pip3 install -U scikit-learn==0.18.2

sudo pip3 install -U matplotlib

echo "Done!"