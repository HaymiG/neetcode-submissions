class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = nums.copy()  
        result.extend(nums)
        return result