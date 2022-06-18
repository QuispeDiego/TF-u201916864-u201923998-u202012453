import enum



class Data:
    def __init__(self,distance,way):
        self.hour=6
        self.distance=distance
        self.way=way
        self.trafficInfo= way[1][self.hour]
        self.trafficFactor=self.trafficInfo*distance

    def setTrafficFactor(self,hour): 
        self.trafficInfo= self.way[1][hour]
        self.trafficFactor=self.trafficInfo*self.distance

    def getTrafficFactor(self):
        return self.trafficFactor

class Node:
    def __init__(self,id,Data):
        self.id=id
        self.Data=Data

    def changeHour(self,hour):
         self.Data.setTrafficFactor(hour)






          

