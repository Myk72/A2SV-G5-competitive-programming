class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        prefix,suffix = defaultdict(list),defaultdict(list)
        prefixSum = [0]*len(nums)
        suffixSum = [0]*len(nums)
        for idx, num in enumerate(nums):
            if num in prefix:
                prev_idx, count= prefix[num]
                dis = (idx - prev_idx)*(count+1)
                newDistance = dis + prefixSum[prev_idx]
                prefix[num] = [idx, count+1]
            else:
                prefix[num] = [idx, 0]
                newDistance=0
            prefixSum[idx] = newDistance
            
        for idx in range(len(nums)-1,-1,-1):
            if nums[idx] in suffix:
                prev_idx, count = suffix[nums[idx]]
                dis = (prev_idx - idx)*(count+1)
                newDistance = dis + suffixSum[prev_idx]
                suffix[nums[idx]] = [idx, count+1]
            else:
                suffix[nums[idx]] = [idx,0]
                newDistance=0
            suffixSum[idx] = newDistance
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] += prefixSum[i] + suffixSum[i]
            
        return res