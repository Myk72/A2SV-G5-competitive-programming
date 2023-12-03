class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        n1=0
        n2=0
        for item in num1:
            n1=n1*10+res[item]
        for item in num2:
            n2 = n2 * 10 + res[item]
        re=n1*n2
        mp = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
        result = ""
        if re==0:
            return "0"
        while re > 0:
            result += mp[re % 10]
            re //= 10
        return result[::-1]
        