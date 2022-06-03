#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 11:37:56 2022

@author: liuc36
"""

from pymongo import MongoClient
from threading import Thread


# Derive from Threading.thread to create a specialised insert thread

class DataInsertThread(Thread):
    database        = None
    threadNumber    = None
    docsInserts = None
   

    def __init__(self, database_in, threadNumber, docs):

        self.database       = database_in

        self.threadNumber   = threadNumber

        self.docsInserts = docs
        
        Thread.__init__(self)

       

    def run(self):

        self.database.testinserts.insert_one(self.docsInserts[self.threadNumber])