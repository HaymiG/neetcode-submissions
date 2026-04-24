class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count =[0] * 3
        for num in nums:
            count[num] += 1
        index = 0 
        for i in range(3):
            for _ in range(count[i]):
                nums[index] = i
                index += 1
        return nums

        # start = 0 
        # mid = 0 
        # end = len(nums) - 1
        # while mid <= end:
        #     if nums[mid] == 0 :
        #         nums[start] , nums[mid] = nums[mid], nums[start]
        #         start +=  1
        #         mid += 1
        #     elif nums[mid] == 1:
        #         mid += 1
                
        #     elif nums[mid] == 2 :
        #         nums[end] , nums[mid] = nums[mid], nums[end]
        #         end -= 1
                
            
        # return nums

















        # return nums.sort()
        # using counting sorting 
        # max_n = max(nums)
        # count = [0] * (max_n + 1)
        # result = [0]*(len(nums))
        # for num in nums:
        #     count[num] += 1
        # for i in range(1 ,len(count)):
        #     count[i] += count[i-1]
        # for i in reversed(nums):
        #     count[i] -= 1
        #     result[count[i]] = i
        # for i in range(len(result)):
        #     nums[i] = result[i]  
        # return nums



        

        
        