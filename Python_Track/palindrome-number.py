class Solution(object):
    def isPalindrome(self, num):
        """
        :type x: int
        :rtype: bool
        """
        temp=num
        res=0
        while temp>0:
            mod=temp%10
            res=res*10+mod
            temp=temp//10
        if res==num:
            return True
        else:
            return False
        