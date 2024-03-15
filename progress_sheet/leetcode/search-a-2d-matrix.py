class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums,target):
            l,r=0,len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    return True
            return False
        row=col=0
        l,r=0,len(matrix)-1
        while l<=r:
            mid=(l+r)//2
            # print(matrix[mid])
            if matrix[mid][0]>target:
                r=mid-1
            elif matrix[mid][0]<target:
                if matrix[mid][-1]<target:
                    l=mid+1
                elif matrix[mid][-1]>target:
                    if search(matrix[mid],target):
                        return True
                    return False
                else:
                    return True
            elif matrix[mid][0]==target:
                return True
        
        return False
