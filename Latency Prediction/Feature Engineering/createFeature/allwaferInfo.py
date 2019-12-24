# import os
# import pymongo
# import pandas as pd
# import numpy as np
# import csv
# d=[]
# dlable=["totalCount","fault-db_name","wafer-decision","fault-decision","wafer-decision","autoDevice","staticDevice","cnnDevice","ensembleDevice","wafer-ensemble-latency"]
# for i in range(0,69):
#     decisionfault=[]
#     address=pd.read_csv("wafer-fault-decision/wafer-edge-address.csv").values
#     address1=pd.read_csv("wafer-fault-decision/fault-edge-address-mix"+str(i)+".csv").values
#     if (address[i][4]!=3):#edge
#     #if (address[i][4]==3)
#         for j in range(len(address1)):
#             db_name="wafer"+str(i)+"fault"+str(j)
#             myclient = pymongo.MongoClient("mongodb://192.168.0.135:27017/")#edge
#             #myclient = pymongo.MongoClient("mongodb://39.100.79.76:27019/")#cloud
#             mydb = myclient[db_name]
#             mycol = mydb["decision"+str(i)]
#             mydoc = mycol.find()[1:]
#             num=0
#             lat5=0
#             for x in mydoc:
#                 frame = x["cnnframe"]
#                 cnnTime = x["cnnTime"]
#                 svmTime = x["svmTime"]
#                 ensembleTime = x["ensembleTime"]
#                 lat5=lat5+max(ensembleTime[1] - cnnTime[0], ensembleTime[1] - svmTime[0])
#                 num=num+1
#             totalCount=num
#             if (totalCount==0 ):
#                 continue
#             else:  
#                 d.append([totalCount,db_name,i,j,i,address[i][1],address[i][2],address[i][3],address[i][4],lat5/totalCount])
# labelPD=pd.DataFrame(columns=dlable,data=d)
# labelPD.to_csv("allwaferInfo.csv")

import os
import pymongo
import pandas as pd
import numpy as np
import csv
address=pd.read_csv("wafer-fault-decision/wafer-edge-address.csv").values
address1=pd.read_csv("wafer-fault-decision/fault-edge-address-mix44"+".csv").values

db_name="wafer38fault44"
myclient = pymongo.MongoClient("mongodb://192.168.0.135:27017/")#edge
#myclient = pymongo.MongoClient("mongodb://39.100.79.76:27019/")#cloud
mydb = myclient[db_name]
mycol = mydb["decision38"]
mydoc = mycol.find()[1:]
num=0
lat5=0
for x in mydoc:
    frame = x["cnnframe"]
    cnnTime = x["cnnTime"]
    svmTime = x["svmTime"]
    ensembleTime = x["ensembleTime"]
    lat5=lat5+max(ensembleTime[1] - cnnTime[0], ensembleTime[1] - svmTime[0])
    num=num+1
totalCount=num
print(lat5/num)






