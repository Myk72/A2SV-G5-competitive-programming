class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l,r=0,len(skill)-1
        tmp=skill[l]+skill[r]
        chem=0
        while l<r:
            if skill[l]+skill[r]==tmp:
                chem+=skill[l]*skill[r]
            else: return -1
            l+=1
            r-=1
        return chem