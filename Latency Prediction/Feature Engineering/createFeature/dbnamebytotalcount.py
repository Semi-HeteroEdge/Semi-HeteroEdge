import pandas as pd
import csv
totalcount=90

fault = pd.read_csv("allfaultInfo.csv").values #Read the fault file
wafer = pd.read_csv("allwaferInfo.csv").values #Read the wafer file
db_namelable=["waferDecision","faultDecison"]#Define the label of the database
edgePlacement=[]
cloudPlacement=[]
#Output the wafer's components on which device, and ensemble's delayed file
for i in range(len(wafer)):#To traverse the wafer
    if wafer[i][1]>=totalcount:#Find the totalcount that satisfies this condition
        if wafer[i][10]>0 and wafer[i][10]<3000:#The preprocessing of the wafer data
            for j in range(len(fault)):#To traverse the fault
                if fault[j][1]>=totalcount:#Find the data that fault satisfies
                    if fault[j][9] > 0 and fault[j][9] < 3000:#The preprocessing of the fault data
                        if wafer[i][3]==fault[j][3]:#To judge whether the I of the wafer is the same as the I of the fault
                            if wafer[i][4]==fault[j][4]:#To judge whether the j of the wafer is the same as the j of the fault
                                if(wafer[i][9]==3):
                                    cloudPlacement.append([wafer[i][3],wafer[i][4]])
                                else:
                                    edgePlacement.append([wafer[i][3],wafer[i][4]])#Add the same to the fault file


#Output CSV file
cloud_csv = pd.DataFrame(columns=db_namelable, data=cloudPlacement)
cloud_csv.to_csv("dbname-bytotalcount/"+str(totalcount)+"-db_name-cloud.csv")
edge_csv = pd.DataFrame(columns=db_namelable, data=edgePlacement)
edge_csv.to_csv("dbname-bytotalcount/"+str(totalcount)+"-db_name-edge.csv")




