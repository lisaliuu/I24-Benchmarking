#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 10:16:16 2022

@author: liuc36
"""
import pymongo
from pymongo import MongoClient
import numpy as np
import urllib.parse
from datetime import datetime
import csv
import calendar
import time
import bson

username = urllib.parse.quote_plus('i24-data')
password = urllib.parse.quote_plus('mongodb@i24')
client = MongoClient('mongodb://%s:%s@10.2.218.56' % (username, password),w=1)
db=client["trajectories"]
colwrite=db["raw_trajectories_two"]
colread=client['trajectories']['raw_trajectories_two']

GTFilePath='/isis/home/teohz/Desktop/data_for_mongo/GT_sort_by_ID/'
TMFilePath='/isis/home/teohz/Desktop/data_for_mongo/pollute/'


trajDict = colread.find_one()
trajDict['test']=1

print (trajDict)

elapse = 0
with open('2.3.S.txt','w') as wf:
    for i in range(100):

        for a in range(10):
            trajDict['x_position'].append(1111.11111)
            trajDict['y_position'].append(1111.11111)
            trajDict['road_segment_id'].append(1111.11111)
            trajDict['timestamp'].append(1111.11111)
            trajDict['raw_timestamp'].append(1111.11111)
            trajDict['length'].append(1111.11111)
            trajDict['width'].append(1111.11111)
            trajDict['height'].append(1111.11111)
            
        trajDict['_id']=i
        st=time.time()
        colwrite.insert_one(trajDict)
        et=time.time()
        elapse=et-st
        doc=colwrite.find_one({'_id':i})
        docsize=len(bson.BSON.encode(doc))
        wf.write(str(docsize)+' '+str(elapse)+'\n')
        
    wf.close()            