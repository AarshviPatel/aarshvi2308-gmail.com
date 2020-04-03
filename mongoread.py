# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 13:05:14 2020

@author: aarsh
"""

import pymongo
import time
current_milli_time = lambda: int(round(time.time() * 1000))
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbdemo"]
mynew = mydb["tlbdemo1"]
#db=myclient.dbdemo
#collection=db.tbldemo1
time_list=[]
ct=0
t1=current_milli_time()
for x in mynew.find():
  ct+=1
  if(ct%100000==0):
      print("Rows read",ct)
  if(ct%1500000==0):    
      t2=current_milli_time()
      time_list.append(float((t2-t1)/60000.00))
print ("Time ::",time_list)
print ("Done")