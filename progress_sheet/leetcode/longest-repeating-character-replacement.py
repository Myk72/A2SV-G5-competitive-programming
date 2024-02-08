class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int)
        mx = 0
        l,freq = 0,0
        for r, char in enumerate(s):
            count[char]+=1
            freq = max(freq,count[char])
            # current maximum occurance of the most frequent letter
            while r-l + 1 > k+freq:
                count[s[l]]-= 1
                l+= 1
            mx = max(mx, r - l + 1)
        return mx