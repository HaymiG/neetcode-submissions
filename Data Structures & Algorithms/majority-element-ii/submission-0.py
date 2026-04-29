class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        n = len(nums)
        limit = n // 3
        result= []

        for key , fre in frequency.items():
            if fre > limit:
                result.append(key)
        return result

        