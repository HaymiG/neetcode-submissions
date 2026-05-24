class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
       
        # r = n - 1
        for l in range(n):
            r = l + 1

            while r < n :
                if nums[l] + nums[r] == target:
                    return [l , r]
                r += 1
        return []
            
        















        # left = 0 
        # for left in range(len(nums)):
        #     right = left + 1
        #     while right < len(nums):
        #         if nums[left] + nums[right] == target :
        #            return [left , right]
        #         right += 1
        # #         

        # right = n-1
        # while left < n :
        #     return [left , right]
        #     else:
        #         left += 1
        # return []     