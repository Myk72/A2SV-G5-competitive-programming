class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for item in s:
            if item.isalnum():
                string+=item.lower()
        l,r=0,len(string)-1
        while l<r:
            if string[l]!=string[r]:
                return False
            l+=1
            r-=1
        return True