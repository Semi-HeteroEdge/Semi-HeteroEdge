totalcount=90
#---------------------- merge edge cloud combined 1,2,3 files---------------------
with open(str(totalcount)+'-mix-one-data.csv','ab') as f:#Generate one - data
    f.write(open(str(totalcount)+'-cloud-fault-one-data.csv','rb').read())
    f.write(open(str(totalcount)+'-edge-fault-one-data.csv', 'rb').read())
    f.write(open(str(totalcount)+'-cloud-wafer-one-data.csv','rb').read())
    f.write(open(str(totalcount)+'-edge-wafer-one-data.csv', 'rb').read())
#Generate one - label
with open(str(totalcount)+'-mix-one-label.csv','ab') as f:
    f.write(open(str(totalcount)+'-cloud-fault-one-label.csv','rb').read())
    f.write(open(str(totalcount)+'-edge-fault-one-label.csv', 'rb').read())
    f.write(open(str(totalcount)+'-cloud-wafer-one-label.csv','rb').read())
    f.write(open(str(totalcount)+'-edge-wafer-one-label.csv', 'rb').read())

#Generate two - data
with open(str(totalcount)+'-mix-two-data.csv','ab') as f:
    f.write(open(str(totalcount)+'-cloud-two-data.csv','rb').read())
    f.write(open(str(totalcount)+'-edge-two-data.csv', 'rb').read())
#Generate two - label
with open(str(totalcount)+'-mix-two-label.csv','ab') as f:#
    f.write(open(str(totalcount)+'-cloud-two-label.csv','rb').read())
    f.write(open(str(totalcount)+'-edge-two-label.csv', 'rb').read())
#Generate three - data
with open(str(totalcount)+'-mix-three-data.csv','ab') as f:
    f.write(open(str(totalcount)+'-cloud-three-data.csv','rb').read())
    f.write(open(str(totalcount)+'-edge-three-data.csv', 'rb').read())

#Generate three - label
with open(str(totalcount)+'-mix-three-label.csv','ab') as f:#
    f.write(open(str(totalcount)+'-cloud-three-label.csv','rb').read())
    f.write(open(str(totalcount)+'-edge-three-label.csv', 'rb').read())


#---------------------Merge edge 1,2,3 files---------------------
with open(str(totalcount)+'-edge-one-data.csv','ab') as f:#Generate one - data
    f.write(open(str(totalcount)+'-edge-fault-one-data.csv', 'rb').read())
    f.write(open(str(totalcount)+'-edge-wafer-one-data.csv', 'rb').read())
# #Generate one- label
with open(str(totalcount)+'-edge-one-label.csv','ab') as f:
    f.write(open(str(totalcount)+'-edge-fault-one-label.csv', 'rb').read())
    f.write(open(str(totalcount)+'-edge-wafer-one-label.csv', 'rb').read())
#

# #---------------------Merge cloud 1,2,3 files---------------------
with open(str(totalcount)+'-cloud-one-data.csv','ab') as f:#
    f.write(open(str(totalcount)+'-cloud-fault-one-data.csv','rb').read())
    f.write(open(str(totalcount)+'-cloud-wafer-one-data.csv','rb').read())
#Generate one - lable
with open(str(totalcount)+'-cloud-one-label.csv','ab') as f:
    f.write(open(str(totalcount)+'-cloud-fault-one-label.csv','rb').read())
    f.write(open(str(totalcount)+'-cloud-wafer-one-label.csv','rb').read())


