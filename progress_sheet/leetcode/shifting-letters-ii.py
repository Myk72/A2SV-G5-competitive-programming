class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        array=[0]*(n+1)
        x=0
        for a,b,c in shifts:
            if c==1:
                array[a]+=c
                array[b+1]-=c
            else:
                array[a]-=1
                array[b+1]+=1
        res = ""
        for i, c in enumerate(s):
            x += array[i]
            letter = chr((ord(c) - 97 + x) % 26 +97)
            res += letter

        return res