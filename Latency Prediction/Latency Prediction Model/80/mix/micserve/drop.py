import pandas as pd
totalcount=80
df=pd.read_csv(str(totalcount)+'-mix-one-data.csv')
df=df.drop(columns=['microPubTopic','pubDevicefre','upComponent','upPubVolum','upSubVolum','upPubTopic'])
df.to_csv(str(totalcount)+'-mix-one-data-1.csv')
#2

df=pd.read_csv(str(totalcount)+'-mix-two-data.csv')
df=df.drop(columns=['pubDevicevolums2','subDeviceSubVolum'])
df.to_csv(str(totalcount)+'-mix-two-data-1.csv')
# #3
# df=pd.read_csv(str(totalcount)+'-mix-three-data.csv')
# df=df.drop(columns=['pubDevicefre1','pubDevicefre2','subDeviceFrequency'])
# df.to_csv(str(totalcount)+'-mix-three-data-1.csv')
