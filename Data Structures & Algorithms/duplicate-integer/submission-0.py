class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for val , fre in count.items():
            if fre > 1 :
                return True 
        return False
        