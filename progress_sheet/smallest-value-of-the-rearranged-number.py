class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:return 0
        lst=[item for item in str(num) if item!='-']
        res=""
        if num>0:
            lst.sort()
            for idx,item in enumerate(lst):
                if item!='0':
                    res+=item+"".join(lst[:idx])+''.join(lst[idx+1:])
                    return int(res)
        else:
            lst.sort(reverse=True)
            return int('-'+''.join(lst))

