# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 18:14:12 2020

@author: aarsh
"""

import pandas as pd
import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["dbdemo"]
mycol=mydb["tlbdemo"]
data=pd.read_csv("samp.csv")

for i in data.index:
   mydict={}
   x1=int(data['id'][i])
   x2=str(data['road_geom'][i])
   x3=str(data['road_id'][i])
   x4=str(data['full_name'][i])
   x5=str(data['route_type'][i])
   x6=str(data['mtfcc_feature_class_code'][i])
   mydict={"id":x1 , "road_geom":x2, "road_id":x3, "full_name": x4, "route_type":x5, "mtfcc_feature_class_code":x6 }
   print(mydict)
   print()
   mycol.insert_one(mydict)

print("Done")