from model.DeviceModel import Device

class MicroService(object):
    #The service name
    def __init__(self, serviceName,isSource,isSink):
        self.name = serviceName
        self.isSource=isSource
        self.isSink=isSink
    #Set the depth at which the micro service is located
    def setDepth(self, depth):
        self.depth = depth
    def setCandidateDevice(self, candidateDevice):
        self.candidateDevice = candidateDevice
    def setCandidateLatency(self, candidateLatency):
        self.candidateDevice = candidateLatency
    #CPU requirements
    def setCPUDemand(self,CPUDemand):
        self.CPUDemand=CPUDemand

    def getCPUDemand(self):
        return self.CPUDemand
    #men requirements
    def setMemDemand(self,memDemand):
        self.memDemand=memDemand

    def getMemDemand(self):
        return self.memDemand
    #The node
    def setInnode(self,innode):
        self.innode=innode
    #Device (object)
    def setDevice(self,device):
        self.device=device
    #Latency requirements
    def setLatencyRe(self,latencyRe):
        self.latencyRe=latencyRe
    #The actual delay
    def setAcutalLat(self,actualLat):
        self.actualLat=actualLat
    #Jump latency
    def setOnehopLat(self,onehopLat):
        self.onehopLat = onehopLat
    # Number of sent topics
    def setPubTopic(self, pubTopic):
        self.pubTopic = pubTopic
    
    def setPubVolum(self, pubVolum):
        self.pubVolum = pubVolum
    # Number of received topics
    def setSubTopic(self, subTopic):
        self.subTopic = subTopic
    #Received data volume
    def setSubVolum(self, subVolum):
        self.subVolum = subVolum

    # component
    def setComponent(self,component):
        self.component=component
    # rate
    def setRate(self,rate):
        self.rate=rate
    #totalCount
    def setTotalCount(self,totalCount):
        self.totalCount=totalCount;

    def setComputeDemand(self,computeDemand):
        self.computeDemand=computeDemand

    def getComputeDemand(self):
        return self.computeDemand
    # Set the diffLatency
    def setDiffLatency(self, diffLatency):
        self.diffLatency = diffLatency

    def getTotalCount(self):
        return self.totalCount;
    #Set the depth at which the micro service is located
    def getDepth(self):
        return self.depth
    def getResourceDemand(self):
        return self.resourceDemand
    def getServiceName(self):
        return self.name
    def getInnode(self):
        return self.innode
    def getDevice(self):
        return self.device
        # Latency requirements
    def getLatencyRe(self):
        return self.latencyRe
        # The actual delay
    def getAcutalLat(self):
        return self.actualLat
        # Jump latency
    def getOnehopLat(self):
        return self.onehopLat

    def getIsSink(self):
        return self.isSink

    def getIsSource(self):
        return self.isSource

    # Number of sent topics
    def getPubTopic(self):
        return self.pubTopic
    # Sending data volume
    def getPubVolum(self):
        return self.pubVolum
    # Number of received topics
    def getSubTopic(self):
        return self.subTopic
    #Received data volume
    def getSubVolum(self):
        return self.subVolum

    # component
    def getComponent(self):
        return self.component
    # rate
    def getRate(self):
        return self.rate
        # 设置diffLatency

    def getDiffLatency(self):
        return self.diffLatency


if __name__ == '__main__':
    mic = MicroService("abc")
    mic.setInnode(["haha","wwww"])
    mic.setDevice("abc")
    mic.setResourceDemand([10,5])
    test=mic.getInnode()

    print(type(test))
    print(test[1].getServiceName())
    print(mic.getDevice().getDeviceName())
    print(mic.getResourceDemand())