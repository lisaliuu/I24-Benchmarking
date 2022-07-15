#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:40:08 2022

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
import random


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

total = 0
elapse = 0
with open('random1.five.T.txt','w') as wf:
    for i in range(20000):
        randEX=random.randint(-14,32800)
        randSX=random.uniform(0,32800)
        randFT=random.uniform(0,643)
        randLT=random.uniform(0,643)
        randConf=random.uniform(1,100000)
        trajDict['test']=1
        trajDict['starting_x']=randSX
        trajDict['ending_x']=randEX
        trajDict['first_timestamp']=randFT
        trajDict['last_timestamp']=randLT
        trajDict['configuration_id']=randConf
        trajDict['_id']=i

        st=time.time()
        colwrite.insert_one(trajDict)
        et=time.time()
        elapse=et-st
        total=total+elapse

        if (i%50==0):
            total=total/50.
            doccount=colwrite.count_documents({})
            wf.write(str(doccount)+' '+str(total)+'\n')
            total=0
        
    wf.close()            