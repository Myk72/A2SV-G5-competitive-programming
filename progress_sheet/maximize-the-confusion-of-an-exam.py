class Solution:
    def maxConsecutiveAnswers(self, answer: str, k: int) -> int:
        cnt=defaultdict(int)
        l=0
        maxi=0
        for i in range(len(answer)):
            cnt[answer[i]]+=1
            if cnt["F"]>k and cnt["T"]>k:
                cnt[answer[l]]-=1
                l+=1
            maxi=max(maxi,i-l+1)
        return maxi