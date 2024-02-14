class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic={5:0,10:0,20:0}
        for num in bills:
            dic[num]+=1
            if num==10:
                if dic[5]>0:
                    dic[5]-=1
                else:
                    return False
            if num==20:
                if dic[10]>0 and dic[5]>0:
                    dic[10]-=1
                    dic[5]-=1
                elif dic[5]>2:
                    dic[5]-=3
                else:
                    return False
        return True