class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        st={}
        mn=inf
        for idx,item in enumerate(cards):
            if item not in st:
                st[item]=idx
            else:
                mn=min(mn,idx-st[item]+1)
                st[item]=idx
        return mn if mn!=inf else -1

            