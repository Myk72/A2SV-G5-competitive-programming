class Solution:
    def freqAlphabets(self, s: str) -> str:
        mp={'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i',
        '10#':'j', '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o',
        '16#': 'p', '17#': 'q', '18#': 'r', '19#': 's', '20#': 't', '21#': 'u',
        '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z' }
        l,r=0,2
        res=""
        while l<=r:
            temp=s[l:r+1]
            if temp in mp:
                res+=mp[temp]
                l=r+1
                r+=3
            else:
                res += mp[s[l]]
                l+=1
                r+=1
            if r>=len(s):
                r=len(s)-1
        return res