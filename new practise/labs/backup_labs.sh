#!/bin/bash

#SRC_DIR="/opt/unetlab/labs/"

#DST_DIR="/root/git_doc/Network-automation-using-Python-using-David-Bomabal-Udemy-Course/new practise/labs/"
cp -a /opt/unetlab/labs/ /root/git_doc/Network-automation-using-Python-using-David-Bomabal-Udemy-Course/new\ practise/labs/

cd /git_doc/
git add .

git status

git commit -m "EVE lab file"

git remote  add origin https://github.com/Omkar-surve/Network-automation-using-Python-using-David-Bomabal-Udemy-Course.git

git push -u origin master
