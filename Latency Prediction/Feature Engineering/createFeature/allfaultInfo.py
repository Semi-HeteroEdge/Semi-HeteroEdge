import os
import pymongo
import pandas as pd
import numpy as np
d=[]
dlable=["totalCount","fault-db_name","wafer-decision","fault-decision","lossoDevice","knnDevice","svmDevice","ensembleDevice","fault-ensemble-latency"]
for i in range(0,69):
    decisions=[]
    decisionscloud=[]
    address=pd.read_csv("wafer-fault-decision/fault-edge-address-mix"+str(i)+".csv").values
    db_name="wafer"+str(i)+"fault"
    for j in range(len(address)):  
        if (address[j][4]!=3):
            decisions.append(j)
    myclient = pymongo.MongoClient("mongodb://192.168.0.135:27017/")
    mydb = myclient[db_name]
    for decision in decisions:
        mycol = mydb["decision"+str(decision)]
        mydoc = mycol.find()[1:]
        num=0
        for x in mydoc:
            knnTime = x["knnTime"]
            svmTime = x["svmTime"]
            exgboostTime = x["xgboostTime"]
            ensembleTime = x["ensembleTime"]
            lat5=lat5+max(ensembleTime[1]-knnTime[0],ensembleTime[1]-svmTime[0],ensembleTime[1]-exgboostTime[0])
            num=num+1
        if (num==0 ):
            continue
        else:
            totalCount=num
            d.append([totalCount,db_name,i,decision,address[decision][1],address[decision][2],address[decision][3],address[decision][4],lat5/totalCount])
labelPD=pd.DataFrame(columns=dlable,data=d)
labelPD.to_csv("allfaultInfo.csv")
