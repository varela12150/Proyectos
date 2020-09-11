#! /usr/bin/env python3
import os
import requests

def corpwebdict(path,url):
    list_of_files = os.listdir(path)
    for file in list_of_files:
            fp = open('/data/feedback/'+file)
            data = fp.read()
            data = data.split('\n')
            dic = {"title":data[0], "name":data[1], "date":data[2], "feedback":data[3]}
            response = requests.post(url, json=dic)
            print(response.status_code)

corpwebdict('/data/feedback','http://104.154.182.119/feedback/')