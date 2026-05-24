class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counting = Counter(nums)
        for freq, val in counting.items():
            if val > 1:
                return True
        return False

        