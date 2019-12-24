import pandas as pd
from sklearn.externals import joblib
import xgboost as xgb
from model.DeviceModel import Device
from model.Application import App
#Resource requirements for the container    source、losso、knn、svm、xgboost、ensemble
faultDetectionCPU=[2,2,2,2,2]

##Container resources demand CPU, memory    source、auto、statis、cnn、svm、ensemble
waferInspectionCPU=[3,3,3,1,2]

#Resource requirements for the container   source propress predict
rulPredictionCPU=[1,3]
serviceCpuDemand=[3,2,3,2,2,3,2,2,3]

services=[
    "wafer-auto","fault-losso" ,"wafer-statis", "fault-knn",
    "fault-svm","wafer-cnn","fault-ensemble", "wafer-ensemble", "rul-prediction"]
newService=[]
serviceDeviceMap = {"fault-source": 0,"wafer-source":0,"rul-source":0,
     "rul-preprocess":3,"fault-xgboost":2,"wafer-svm":0}
#serviceDeviceMap["fault-losso"]
#------------------------------------------------------Part2  Initializing device-------------------------------------------------
#---------------------------------------------------1.Equipment name 2. Equipment resources--------------------------------------
#---------Initialize the device themes and data volumes -------- including the SVM fixed to nano and the xgboost to miniserver---------------

devicesCPU=[3,12,6,24]

#------------------------------------------------------Part3 Initialization mode-------------------------------------------------

i=0
j=0
for service in services:#

    deviceId=j%4
    if(serviceCpuDemand[i]<=devicesCPU[deviceId]):
        devicesCPU[deviceId]=devicesCPU[deviceId]-serviceCpuDemand[i]
        serviceDeviceMap[service]=deviceId
    else:
        flag=0
        while(flag==0):
            j=j+1
            deviceId = j % 4
            if (serviceCpuDemand[i] <= devicesCPU[deviceId]):
                devicesCPU[deviceId] = devicesCPU[deviceId] - serviceCpuDemand[i]
                serviceDeviceMap[service] = deviceId
                flag=1
            else:
                flag=0

    i=i+1
    j=j+1

print(len(serviceDeviceMap),serviceDeviceMap)





