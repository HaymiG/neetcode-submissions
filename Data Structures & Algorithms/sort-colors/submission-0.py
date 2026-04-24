class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # return nums.sort()
        # using countinf sorting 
        max_n = max(nums)
        count = [0] * (max_n + 1)
        result = [0]*(len(nums))
        for num in nums:
            count[num] += 1
        for i in range(1 ,len(count)):
            count[i] += count[i-1]
        for i in reversed(nums):
            count[i] -= 1
            result[count[i]] = i
        for i in range(len(result)):
            nums[i] = result[i]

            
        return nums
        

        
        