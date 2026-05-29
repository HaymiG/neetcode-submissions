class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = cur =  0 
        count = { 0 : 1}
        
        for num in nums:
            cur += num
            diff = cur - k
            result += count.get(diff , 0)
            count[cur] = 1 + count.get(cur , 0)
        return result
            
        