totalcount=10
# #生成three-data
# with open(str(totalcount)+'-edge-three-data.csv','ab') as f:
#     f.write(open(str(totalcount)+'-cloud-three-data.csv','rb').read())
#     #f.write(open(str(totalcount)+'-edge-three-data.csv', 'rb').read())
#
# #生成three- label
# with open(str(totalcount)+'-edge-three-label.csv','ab') as f:#
#     f.write(open(str(totalcount)+'-cloud-three-label.csv','rb').read())
#    # f.write(open(str(totalcount)+'-edge-three-label.csv', 'rb').read())

#one
#one
with open(str(totalcount)+'-edge-one-data.csv','ab') as f:
    f.write(open("one-"+str(totalcount)+'-cloud-fault-one-data.csv','rb').read())
    #f.write(open(str(totalcount)+'-edge-one-data.csv', 'rb').read())

#生成three- label
with open(str(totalcount)+'-edge-one-label.csv','ab') as f:#
    f.write(open("one-"+str(totalcount)+'-cloud-fault-one-label.csv','rb').read())
    #f.write(open(str(totalcount)+'-edge-one-label.csv', 'rb').read())


