#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 11:26:56 2022

@author: liuc36
"""
import time 
import numpy as np
from pymongo import MongoClient
import urllib.parse
import thread as th
import bson
import random

username = urllib.parse.quote_plus('i24-data')
password = urllib.parse.quote_plus('mongodb@i24')
client = MongoClient('mongodb://%s:%s@10.2.218.56' % (username, password))
dbwrite=client["lisatest"]
colwrite=dbwrite["testinserts"]

dbread=client['trajectories']
colread=dbread['ground_truth_two']

n=50
n_trials=10




def busywork(size):
    a = np.random.rand(size,size)
    b = np.random.rand(size,size)
    c=np.matmul(a,b)



def generateDocs(size):
    docstart=colread.find_one()
    while(len(bson.BSON.encode(docstart))<size):
        for i in range(1000):
            docstart['y_position'].append(i+random.random())
            docstart['x_position'].append(i+random.random())
            docstart['raw_timestamp'].append(i+random.random())
            docstart['timestamp'].append(i+random.random())
            docstart['road_segment_id'].append(i+random.random()+random.random())
    #print('length: '+str(len(bson.BSON.encode(docstart))))
    del docstart['_id']
    return docstart  

    

#case 3
def threadedInserts():
    insertThreads=[]
    for threadNum in range(n):
        insertThread=th.DataInsertThread(dbwrite, threadNum, docs)
        insertThreads.append(insertThread)
        insertThread.start()
    for insertThread in insertThreads:
        insertThread.join()



#case 2
def batchInserts():
    colwrite.insert_many(docs)



totElapsedTime=0
totElapsedThreadTime=0

docs=[]
print('generating docs')
for j in range(n):
    doc=generateDocs(2000000)
    docs.append(doc)
    if (j%100==0):
        print('100 done')
    
for i in range(n_trials):

    
    colwrite.drop()
    threadst=time.thread_time()
    st=time.time()
    
    print('starting insert')
    threadedInserts()
    print('ending insert')
    
    busywork(4300)
    threadet=time.thread_time()
    et=time.time()
    
    totElapsedTime=totElapsedTime+et-st
    totElapsedThreadTime=totElapsedThreadTime+threadet-threadst


elapsedTime=totElapsedTime/n_trials
elapsedThreadTime=totElapsedThreadTime/n_trials


print('\ntime: '+str(elapsedTime)+'\nthread time: '+str(elapsedThreadTime))
    

    
