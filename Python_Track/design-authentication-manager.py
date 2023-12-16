class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timetoLive=timeToLive
        self.generator=defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.generator[tokenId]=self.timetoLive+currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.generator[tokenId]>currentTime: # this implies the tokenId is expired,so we can renew it
            self.generator[tokenId]=currentTime+self.timetoLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count=0 # used for counting the unexpired tokens
        for exTime in self.generator.values():
            if currentTime < exTime:count+=1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)