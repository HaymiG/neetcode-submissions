class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        least = n // 2
        count = Counter(nums)
        cou = 0
        for key , value in count.items():
            if value > least :
                return key
              


        