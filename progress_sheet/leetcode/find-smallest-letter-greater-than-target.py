class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l,r=0,len(letters)-1
        order=ord(target)
        while l<r:
            mid=(l+r)//2
            if ord(letters[mid])>order:
                r=mid
            else:
                l=mid+1
        # print(l,r)
        return letters[r] if ord(letters[r])>order else letters[0]
