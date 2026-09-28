class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        rep = {}
        for i in nums:
            if i in rep:
                rep[i] += 1
            else:
                rep[i] = 1
                
        for key, value in rep.items():
            if value > 1:
                return True
                
        return False