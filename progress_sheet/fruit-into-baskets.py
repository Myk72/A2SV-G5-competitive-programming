class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l= 0
        res=0
        count = defaultdict(int)
        for r, fruit in enumerate(fruits):
            count[fruit] += 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            res = max(res, r - l + 1)

        return res