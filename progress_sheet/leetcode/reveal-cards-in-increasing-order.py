class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n=len(deck)
        deck.sort()
        if n<3:return deck
        que=deque([deck[-1]])
        for i in range(n-2,-1,-1):
            que.appendleft(que.pop())
            que.appendleft(deck[i])
        return [que[i] for i in range(n)]







        # if n<3:return deck
        # l,r=1,n-2
        # res=[deck[0]]
        # while l<r:
        #     res.append(deck[r])
        #     res.append(deck[l])
        #     l+=1
        #     r-=1
        # res.append(deck[-1])
        # res.append(deck[l])
        # return res