class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort(key=len)
        r=len(strs[0])-1
        mnm=float('inf')
        for i in range(1,len(strs)):
            while strs[0][:r+1]!=strs[i][:r+1]:
                r-=1
            else:
                mnm=min(r,mnm)
        return strs[0][:r+1]
        