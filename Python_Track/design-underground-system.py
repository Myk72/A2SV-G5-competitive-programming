class UndergroundSystem:

    def __init__(self):
        self.check_in={}
        self.total_time=defaultdict(int) # consists summation of time duration between stations
        self.freq=defaultdict(int) # frequency of travel

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id]=stationName,t
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation,time1=self.check_in.pop(id)
        # since customer can only be checked into one place at a time
        delta=t-time1
        self.total_time[(startStation,stationName)]+=delta
        self.freq[(startStation,stationName)]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.total_time[(startStation,endStation)]/ self.freq[(startStation,endStation)]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)