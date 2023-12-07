class Solution:
    def largestOddNumber(self, num: str) -> str:
      l,r=0,len(num)-1
      while r>=0:
          if int(num[r]) % 2 == 0:
              r-=1
          else:
              return num[:r+1]
      return ""