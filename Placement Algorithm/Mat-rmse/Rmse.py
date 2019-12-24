import pandas as pd
import csv
totalcount=20
num="one"
true=pd.read_csv(str(totalcount)+"-mix-"+num+"-label.csv").values
f=pd.read_csv("queue"+str(totalcount)+"-mix-"+num+"-label.csv").values
t=[]
for i in range(len(f)):
    t.append([f[i][1],true[i][1]])
lable=["totalLatency","totalLatency"]
labelPD = pd.DataFrame(columns=lable, data=t)
labelPD.to_csv("Aqueue"+str(totalcount)+"-mix-"+num+"-label.csv")

target = []
prediction = []

file=pd.read_csv("Aqueue"+str(totalcount)+"-mix-"+num+"-label.csv").values
#file=pd.read_csv("queue10-mix-one-label.csv").values
for i in range(len(file)):
    target.append(file[i][2])
    prediction.append((file[i][1]))
error = []
for i in range(len(target)):
    error.append(target[i] - prediction[i])

print("Errors: ", error)
print(error)

squaredError = []
absError = []
for val in error:
    squaredError.append(val * val)  # Target -prediction squared
    absError.append(abs(val))  # absolute value of error

# print("Square Error: ", squaredError)
# print("Absolute Value of Error: ", absError)

#print("MSE = ", sum(squaredError) / len(squaredError))  

from math import sqrt

print("RMSE = ", sqrt(sum(squaredError) / len(squaredError)))  


# targetDeviation = []
# targetMean = sum(target) / len(target)  # 
# for val in target:
#     targetDeviation.append((val - targetMean) * (val - targetMean))
# #print("Target Variance = ", sum(targetDeviation) / len(targetDeviation))  # 
