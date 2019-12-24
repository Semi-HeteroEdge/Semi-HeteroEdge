import pandas as pd
from sklearn.externals import joblib
import xgboost as xgb
from model.DeviceModel import Device
from model.Application import App
#Resource requirements for the container    source、losso、knn、svm、xgboost、ensemble
faultDetectionCPU=[2,2,2,2,2]

#Container resources demand CPU, memory    source、auto、statis、cnn、svm、ensemble
waferInspectionCPU=[3,3,3,1,2]

#Resource requirements for the container   source propress predict
rulPredictionCPU=[1,3]
serviceCpuDemand=[3,2,3,2,2,3,2,2,3]

services=[
    "wafer-auto", "fault-losso","wafer-statis", "fault-knn",
    "fault-svm","wafer-cnn","fault-ensemble", "wafer-ensemble", "rul-prediction"]
newService=[]
serviceDeviceMap = {"fault-source": 0,"wafer-source":0,"rul-source":0,
     "rul-preprocess":3,"fault-xgboost":2,"wafer-svm":0}

#------------------------------------------------------Part2  Initializing device-------------------------------------------------
#---------------------------------------------------1.Equipment name 2. Equipment resources--------------------------------------
#---------Initialize the device themes and data volumes -------- including the SVM fixed to nano and the xgboost to miniserver---------------

devicesCPU={"device0":3,
            "device1":12,
            "device2":6,
            "device3":24}

def sortedDictValues1(adict):
    items = adict.items()
   # print(items)
    backitems = [[v[1], v[0]] for v in items]
    #print(backitems)
    backitems.sort()
    return [backitems[i][1] for i in range(0, len(backitems))]

#------------------------------------------------------Part3 Initialization mode-------------------------------------------------


i=0
j=0
for service in services:
    deviceIDAs = sortedDictValues1(devicesCPU)
    print(devicesCPU,deviceIDAs)
    for deviceId in deviceIDAs:
        if(serviceCpuDemand[i]<=devicesCPU[deviceId]  ):
            # print(serviceCpuDemand[i])
            devicesCPU[deviceId]=devicesCPU[deviceId]-serviceCpuDemand[i]

            serviceDeviceMap[service]=deviceId

            # print(serviceDeviceMap[service])
            break;
    i=i+1
print(len(serviceDeviceMap),serviceDeviceMap)





