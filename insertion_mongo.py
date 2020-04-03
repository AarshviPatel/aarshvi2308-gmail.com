# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:57:19 2020

@author: aarsh
"""

try:
    import pymongo
    from pymongo import MongoClient
    import pandas as pd
    import json
    import time
except Exception as e:
    print("Some Modules are Missing ")


class MongoDB(object):

    def __init__(self, dBName=None, collectionName=None):

        self.dBName = dBName
        self.collectionName = collectionName

        self.client = MongoClient("localhost", 27017, maxPoolSize=50)

        self.DB = self.client[self.dBName]
        self.collection = self.DB[self.collectionName]



    def InsertData(self, path=None):
        """
        :param path: Path os csv File
        :return: None
        """

        df = pd.read_csv("annual-enterprise-survey-2018-financial-year-provisional-csv.csv")
        data = df.to_dict('records')

        self.collection.insert_many(data, ordered=False)
        print("All the Data has been Exported to Mongo DB Server .... ")

if __name__ == "__main__":
    mongodb = MongoDB(dBName = 'Sample', collectionName='tablInsert')
    start=time.time()
    mongodb.InsertData(path="annual-enterprise-survey-2018-financial-year-provisional-csv.csv")
    end=time.time()
    total=(start-end)
    print (total)