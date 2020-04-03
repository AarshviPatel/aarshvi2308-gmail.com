# aarshvi2308-gmail.com
Performance Testing of MongoDB
MongoDB is a cross-platform document-oriented database program. MongoDB has a flexible storage architecture. It supports expressive query language & secondary indexes, strong consistency and enterprise management and integrations. The cross-platform NoSQL database was complex to install in the first place. MongoDB requires a community server which is a free and open document base to be downloaded first. This community server could be used with either a command prompt or its own GUI. cmd required the path to be specified every time an operation needs to be performed. A data and dB folder had to be created to overcome the complexity. To have actual hold of the database the MongoDB compass had to be installed. Moving on, the data was in the form of a CSV file. To insert this file and to calculate times python had to be used. Pymongo was imported for insertion. The preprocessed dataset that now contains 6M rows were inserted. The large data was inserted in smaller chunks. A dictionary was created in python with the following different rows: road latitude, longitude, road_id, name of the road, route type, class code. This dictionary was inserted as a whole in the table in MongoDB.

C.	Challenges
1)	The database has more than 6 million rows with road latitude, longitude, road id, name of the road, route type and so on. Some of the rows have NaN values that have to be handled to make the data evenly distributed.
2)	 The data is distributed in a different file which was combined into a single file for simpler processing. The process is made fully automated using scripts so if future data needs to be appended it can be done very easily.
3)	While inserting data into databases using python the issue which arose was that whole data wasn’t able to fit in main memory so to resolve this issue while performing several operations like write that data was divided in chunks and then it was inserted in databases.
4)	MongoDB stock data in documents are in JSON format so our data being in a CSV file has to be converted first in JSON form and then inserted. In our performance evaluation, we excluded the conversion time.

