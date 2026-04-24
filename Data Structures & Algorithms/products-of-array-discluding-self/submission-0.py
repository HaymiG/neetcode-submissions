class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n 
        suff = [0] * n
        result = [0] * n
        pref[0] = suff[n-1] = 1
 
        for i in range(1 , len(nums)):
            pref[i] = nums[i-1] * pref[i-1]

        for i in range(n-2 , -1 , -1):
            suff[i] = nums[i+1] * suff[i+1]
        for i in range(len(nums)):
            result[i] = suff[i] * pref[i]
        return result
        













        # zeros = 0
        # product  = 1
        # result = []
        # for i in range(len(nums)):
        #     if nums[i] == 0 :
        #         zeros += 1
        #     product *= nums[i]
        # if zeros >= 2:
        #     return [0] * len(nums)
        # for index , value in enumerate(nums):
        #     if zeros:
        #         result[index].append(0)
        #     result.append(product // nums[index])
        # return result








        # result = []

        # for i in range(len(nums)):
        #     pro = 1
        #     for j in range(len(nums)):
        #         if j == i :
        #             continue
        #         pro *= nums[j]
        #     result.append(pro)
        # return result

        