# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:47:19 2020

@author: aarsh
"""

import pandas as pd
import pymongo
import math
import psutil
import time
current_milli_time = lambda: int(round(time.time() * 1000))
process=psutil.Process(4116)
pro_mem_list=[]
pro_cpu_list=[]
time_list=[]
no=0
ct=0

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["dbdemo"]
mycol=mydb["tlbdemo1"]
chunksize=100000
d=pd.read_csv("combined_csv3.csv", chunksize=chunksize)

t1=current_milli_time()
for data in d:
    no+=1
    for i in data.index:
        ct+=1
        mydict={}
        x1=int(data['id'][i])
        x2=str(data['road_geom'][i])
        x3=str(data['road_id'][i])
        x4=str(data['full_name'][i])
        x5=str(data['route_type'][i])
        x6=str(data['mtfcc_feature_class_code'][i])
        mydict={"id":x1 , "road_geom":x2, "road_id":x3, "full_name": x4, "route_type":x5, "mtfcc_feature_class_code":x6 }
        #print(mydict)
        #print()
        mycol.insert_one(mydict)
        if(ct%50000==0):
            print("Rows Inserted : ",ct)
    if(no%15==0):
        process_mem=process.memory_info()
        pro_mem_list.append(process_mem[1]/(1024*1024))
        pro_cpu_list.append(process.cpu_percent(interval=1.0))
        t2=current_milli_time()
        time_list.append(float((t2-t1)/60000.00))
    if(no==60):
        break

                        

print("Time :: ",time_list)
print("Average Memory Usage :: ",int(sum(pro_mem_list)/len(pro_mem_list)))
print("Average CPU Usage :: ",(max(pro_cpu_list)))
print("Done")