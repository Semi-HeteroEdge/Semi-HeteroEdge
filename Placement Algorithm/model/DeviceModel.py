class Device(object):
    def __init__(self, deviceName):
        self.deviceName = deviceName
    # The total resources
    def setCPUTotal(self, CPUTotal):
        self.CPUTotal = CPUTotal

    def getCPUTotal(self):
        return self.CPUTotal

    def setMemTotal(self, MemTotal):
        self.MemTotal = MemTotal

    def getMemTotal(self):
        return self.MemTotal

    # Resource surplus
    def setCPURemain(self, CPURemain):
        self.CPURemain = CPURemain

    # Number of sent topics
    def setPubTopic(self, pubTopic):
        self.pubTopic = pubTopic

    # Sending data volume
    def setPubVolum(self, pubVolum):
        self.pubVolum = pubVolum

    # Number of received topics
    def setSubTopic(self, subTopic):
        self.subTopic = subTopic

    # Received data volume
    def setSubVolum(self, subVolum):
        self.subVolum = subVolum

    # According to the total amount
    def setVolums(self, volums):
        self.volums = volums

    def setCompute(self, compute):
        self.compute = compute

    def getCompute(self):
        return self.compute

    def getCPURemain(self):
        return self.CPURemain

    def setMemRemain(self, MemRemain):
        self.MemRemain = MemRemain

    def setFrequency(self, frequency):
        self.frequency = frequency

    def getMemRemain(self):
        return self.MemRemain
    #Device name
    def getDeviceName(self):
        return self.deviceName

    # The total resources
    def getResourceTotal(self):
        return self.resourceTotal

    # Resource surplus
    def getResourceRemain(self):
        return self.resourceRemain

    # Number of sent topics
    def getPubTopic(self):
        return self.pubTopic
    # Sending data volume
    def getPubVolum(self):
        return self.pubVolum
    # Number of received topics
    def getSubTopic(self):
        return self.subTopic
    # Received data volume
    def getSubVolum(self):
        return self.subVolum
    # According to the total amount
    def getVolums(self):
        return self.volums

    def getFrequency(self):
        return self.frequency

