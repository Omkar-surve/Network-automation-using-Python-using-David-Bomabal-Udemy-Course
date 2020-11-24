#!/bin/bash

#Copying source folder to backup labs folder
cp -a /opt/unetlab/labs/ /root/git_doc/Network-automation-using-Python-using-David-Bomabal-Udemy-Course/new\ practise/labs/

#changing path to git init folder
cd /git_doc/

#staging git folders  for commit
git add .

#checking staged files
git status

#commiting files to git
git commit -m "EVE lab file"

#adding remote path to git
git remote  add origin https://github.com/Omkar-surve/Network-automation-using-Python-using-David-Bomabal-Udemy-Course.git

#pushing files to git
git push -u origin master
