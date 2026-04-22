class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []
        sorted_item = sorted(count.items() , key= lambda x:x[1] , reverse = True)
        for i in range(k):
            result.append(sorted_item[i][0])
        return result