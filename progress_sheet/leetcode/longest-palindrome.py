class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic=defaultdict(int)
        count=0
        for char in s:
            if dic[char]>0:
                dic[char]-=1
                count-=1
            else:
                dic[char]+=1
                count+=1
        return len(s) -count+1 if count>0 else len(s) -count
        