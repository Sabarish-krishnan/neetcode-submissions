class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = 0
        ans = []
        while 1 >= n:
            for i in nums:
                ans.append(i)
            n += 1
        return ans