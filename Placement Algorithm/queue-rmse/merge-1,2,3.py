totalcount=20
#---------------------Merge edge cloud combined 1,2,3 files---------------------
# with open(str(totalcount)+'-mix-one-data.csv','ab') as f:#generate one-data
#     f.write(open(str(totalcount)+'-cloud-fault-one-data.csv','rb').read())
#     f.write(open(str(totalcount)+'-edge-fault-one-data.csv', 'rb').read())
#     f.write(open(str(totalcount)+'-cloud-wafer-one-data.csv','rb').read())
#     f.write(open(str(totalcount)+'-edge-wafer-one-data.csv', 'rb').read())
#generate one- label
with open("queue"+str(totalcount)+'-mix-one-label.csv','ab') as f:
    f.write(open("queue"+str(totalcount)+'-cloud-fault-one-label.csv','rb').read())
    f.write(open("queue"+str(totalcount)+'-edge-fault-one-label.csv', 'rb').read())
    f.write(open("queue"+str(totalcount)+'-cloud-wafer-one-label.csv','rb').read())
    f.write(open("queue"+str(totalcount)+'-edge-wafer-one-label.csv', 'rb').read())

# #generate two-data
# with open(str(totalcount)+'-mix-two-data.csv','ab') as f:
#     f.write(open(str(totalcount)+'-cloud-two-data.csv','rb').read())
#     f.write(open(str(totalcount)+'-edge-two-data.csv', 'rb').read())
#generate two- label
# with open("queue"+str(totalcount)+'-mix-two-label.csv','ab') as f:#
#     f.write(open("queue"+str(totalcount)+'-cloud-two-label.csv','rb').read())
#     f.write(open("queue"+str(totalcount)+'-edge-two-label.csv', 'rb').read())
# # #generate three-data
# # with open(str(totalcount)+'-mix-three-data.csv','ab') as f:
# #     f.write(open(str(totalcount)+'-cloud-three-data.csv','rb').read())
# #     f.write(open(str(totalcount)+'-edge-three-data.csv', 'rb').read())
#
# #generate three- label
# with open("queue"+str(totalcount)+'-mix-three-label.csv','ab') as f:#
#     f.write(open("queue"+str(totalcount)+'-cloud-three-label.csv','rb').read())
#     f.write(open("queue"+str(totalcount)+'-edge-three-label.csv', 'rb').read())


# #---------------------Merge edge 1,2,3 files---------------------
# with open(str(totalcount)+'-edge-one-data.csv','ab') as f:#generate one-data
#     f.write(open(str(totalcount)+'-edge-fault-one-data.csv', 'rb').read())
#     f.write(open(str(totalcount)+'-edge-wafer-one-data.csv', 'rb').read())
# # #generate one- label
# with open(str(totalcount)+'-edge-one-label.csv','ab') as f:
#     f.write(open(str(totalcount)+'-edge-fault-one-label.csv', 'rb').read())
#     f.write(open(str(totalcount)+'-edge-wafer-one-label.csv', 'rb').read())
# #

# # #---------------------Merge cloud 1,2,3 files---------------------
# with open(str(totalcount)+'-cloud-one-data.csv','ab') as f:#生成one-data
#     f.write(open(str(totalcount)+'-cloud-fault-one-data.csv','rb').read())
#     f.write(open(str(totalcount)+'-cloud-wafer-one-data.csv','rb').read())
# #generate one- label
# with open(str(totalcount)+'-cloud-one-label.csv','ab') as f:
#     f.write(open(str(totalcount)+'-cloud-fault-one-label.csv','rb').read())
#     f.write(open(str(totalcount)+'-cloud-wafer-one-label.csv','rb').read())


