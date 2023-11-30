class Solution(object):
    def sumOfThree(self, n):
        """
        :type num: int
        :rtype: List[int]
        """
        if (n+3)%3==0:
            i=int((n+3)/3)
            return [i-2,i-1,i]
        else:
            return []
        