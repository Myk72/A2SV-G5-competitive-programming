class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        for item in ghosts:
            diff=[abs(item[0]-target[0]),abs(item[1]-target[1])]
            targ=[abs(target[0]),abs(target[1])]
            if sum(diff)<=sum(targ):
                return False
        return True