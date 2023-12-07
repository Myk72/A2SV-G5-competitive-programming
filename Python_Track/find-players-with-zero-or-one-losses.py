class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

      answer=[[],[]]
      winners=Counter()
      losers=Counter()
      for i in range(len(matches)):
        winners.update([matches[i][0]])
        losers.update([matches[i][1]])
      for a in losers.keys():
        if losers[a]==1:
            answer[1].append(a)
      for b in winners.keys():
        if b not in losers:
            answer[0].append(b)
      answer[1].sort()
      answer[0].sort()
      return answer
        