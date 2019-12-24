# #-----去掉文件中重复的标题行----------
totalcount=10
#
# #----------

#---------------------边云结合的1，2，3文件---------------------
with open(str(totalcount)+'-edge-one-label.csv','r') as r:
    lines=r.readlines()
with open(str(totalcount)+'-edge-one-label.csv','w') as w:
    for l in lines:
           if 'totalLatency' not in l:
                w.write(l)
#data
with open(str(totalcount)+'-edge-one-data.csv','r') as r:
    lines=r.readlines()
with open(str(totalcount)+'-edge-one-data.csv','w') as w:
    for l in lines:
           if 'totalCount' not in l:
                w.write(l)
#tow

# with open(str(totalcount)+'-mix-two-label.csv','r') as r:
#     lines=r.readlines()
# with open(str(totalcount)+'-mix-two-label.csv','w') as w:
#     for l in lines:
#            if 'totalLatency' not in l:
#                 w.write(l)
# #data
# with open(str(totalcount)+'-mix-two-data.csv','r') as r:
#     lines=r.readlines()
# with open(str(totalcount)+'-mix-two-data.csv','w') as w:
#     for l in lines:
#            if 'totalCount' not in l:
#                 w.write(l)
# with open(str(totalcount)+'-mix-three-label.csv','r') as r:
#     lines=r.readlines()
# with open(str(totalcount)+'-mix-three-label.csv','w') as w:
#     for l in lines:
#            if 'totalLatency' not in l:
#                 w.write(l)
# #data
# with open(str(totalcount)+'-mix-three-data.csv','r') as r:
#     lines=r.readlines()
# with open(str(totalcount)+'-mix-three-data.csv','w') as w:
#     for l in lines:
#            if 'totalCount' not in l:
#                 w.write(l)
#
# #
# # #---------------------边的1，2，3文件---------------------
# with open(str(totalcount)+'-edge-one-label.csv','r') as r:
#     lines=r.readlines()
# with open(str(totalcount)+'-edge-one-label.csv','w') as w:
#     for l in lines:
#            if 'totalLatency' not in l:
#                 w.write(l)
# #data
# with open(str(totalcount)+'-edge-one-data.csv','r') as r:
#     lines=r.readlines()
# with open(str(totalcount)+'-edge-one-data.csv','w') as w:
#     for l in lines:
#            if 'totalCount' not in l:
#                 w.write(l)
# #tow
#
# with open(str(totalcount)+'-edge-two-label.csv','r') as r:
#     lines=r.readlines()
# with open(str(totalcount)+'-edge-two-label.csv','w') as w:
#     for l in lines:
#            if 'totalLatency' not in l:
#                 w.write(l)
# #data
# with open(str(totalcount)+'-edge-two-data.csv','r') as r:
#     lines=r.readlines()
# with open(str(totalcount)+'-edge-two-data.csv','w') as w:
#     for l in lines:
#            if 'totalCount' not in l:
#                 w.write(l)
# with open(str(totalcount)+'-edge-three-label.csv','r') as r:
#     lines=r.readlines()
# with open(str(totalcount)+'-edge-three-label.csv','w') as w:
#     for l in lines:
#            if 'totalLatency' not in l:
#                 w.write(l)
# #data
# with open(str(totalcount)+'-edge-three-data.csv','r') as r:
#     lines=r.readlines()
# with open(str(totalcount)+'-edge-three-data.csv','w') as w:
#     for l in lines:
#            if 'totalCount' not in l:
#                 w.write(l)
#
# #
# #
# # #---------------------合并云的1，2，3文件---------------------
# with open(str(totalcount)+'-cloud-one-label.csv','r') as r:
#     lines=r.readlines()
# with open(str(totalcount)+'-cloud-one-label.csv','w') as w:
#     for l in lines:
#            if 'totalLatency' not in l:
#                 w.write(l)
# #data
# with open(str(totalcount)+'-cloud-one-data.csv','r') as r:
#     lines=r.readlines()
# with open(str(totalcount)+'-cloud-one-data.csv','w') as w:
#     for l in lines:
#            if 'totalCount' not in l:
#                 w.write(l)
# #tow
#
# with open(str(totalcount)+'-cloud-two-label.csv','r') as r:
#     lines=r.readlines()
# with open(str(totalcount)+'-cloud-two-label.csv','w') as w:
#     for l in lines:
#            if 'totalLatency' not in l:
#                 w.write(l)
# #data
# with open(str(totalcount)+'-cloud-two-data.csv','r') as r:
#     lines=r.readlines()
# with open(str(totalcount)+'-cloud-two-data.csv','w') as w:
#     for l in lines:
#            if 'totalCount' not in l:
#                 w.write(l)
# with open(str(totalcount)+'-cloud-three-label.csv','r') as r:
#     lines=r.readlines()
# with open(str(totalcount)+'-cloud-three-label.csv','w') as w:
#     for l in lines:
#            if 'totalLatency' not in l:
#                 w.write(l)
# #data
# with open(str(totalcount)+'-cloud-three-data.csv','r') as r:
#     lines=r.readlines()
# with open(str(totalcount)+'-cloud-three-data.csv','w') as w:
#     for l in lines:
#            if 'totalCount' not in l:
#                 w.write(l)
#
# #
# #
