# #-----Remove duplicate header lines from the file----------
totalcount=20
#
# #----------

#---------------------Edge cloud combines 1,2,3 files---------------------
with open("queue"+str(totalcount)+'-mix-one-label.csv','r') as r:
    lines=r.readlines()
with open("queue"+str(totalcount)+'-mix-one-label.csv','w') as w:
    for l in lines:
           if 'totalLatency' not in l:
                w.write(l)


# with open("queue"+str(totalcount)+'-mix-two-label.csv','r') as r:
#     lines=r.readlines()
# with open("queue"+str(totalcount)+'-mix-two-label.csv','w') as w:
#     for l in lines:
#            if 'totalLatency' not in l:
#                 w.write(l)
#
# with open("queue"+str(totalcount)+'-mix-three-label.csv','r') as r:
#     lines=r.readlines()
# with open("queue"+str(totalcount)+'-mix-three-label.csv','w') as w:
#     for l in lines:
#            if 'totalLatency' not in l:
#                 w.write(l)
