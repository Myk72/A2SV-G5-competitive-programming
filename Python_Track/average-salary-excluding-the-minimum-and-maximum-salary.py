class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        r=len(salary)-2
        return sum(salary[1:r+1])/r
        