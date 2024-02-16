class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n=len(palindrome)
        if n==1:return ""
        res=""
        flag=False
        for i in range(n//2):
            if palindrome[i]!="a":
                res+="a"
                flag=True
                break
            res+=palindrome[i]
        if flag:
            return res+"".join(palindrome[i+1:])
        else:
            return palindrome[:-1]+"b"
