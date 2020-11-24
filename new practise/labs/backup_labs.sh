#!/bin/bash

SRC_DIR="/opt/unetlab/labs"

DST_DIR="/root/git_doc/Network-automation-using-Python-using-David-Bomabal-Udem$"

cp $SRC_DIR/ $DST_DIR

cd /git_doc/

git add .

git status

DATE=($date)
echo $DATE
git commit -m "EVE lab file $DATE"

git remote  add origin https://github.com/Omkar-surve/Network-automation-using-$

git push -u origin master
