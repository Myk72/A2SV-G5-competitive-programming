class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = defaultdict(int)
        res=0
        l=0
        for j, item in enumerate(s):
            while char[item]>0 :
                char[s[l]]-=1
                l += 1
            char[item]+=1
            res = max(res, j - l + 1)
        return res