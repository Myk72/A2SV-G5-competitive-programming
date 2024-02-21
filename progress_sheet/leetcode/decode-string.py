class Solution:
    def decodeString(self, s: str) -> str:
        #recursion
        def decode(s,n):
            if s.isalpha():
                return s*n
            res=""
            ans=""
            stack=[]
            dig=""
            i=0
            while i<len(s):
                while s[i].isdigit():
                    if stack:res+=s[i]
                    else:dig+=s[i]
                    i+=1
                if s[i]=="[":
                    if stack:res+=s[i]
                    stack.append(s[i])
                elif s[i]=="]":
                    stack.pop()
                    # "3[a2[c]]"
                    if stack:res+=s[i]
                    else:
                        ans+= decode(res,int(dig))
                        dig=""
                        res=""
                else:
                    if not dig:ans+=s[i]
                    else:res+=s[i]
                i+=1
                # print(res)
            return ans*n


        return decode(s,1)