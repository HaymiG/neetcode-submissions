class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        result = []
        for word in strs:
            keys = ''.join(sorted(word))
            count[keys].append(word)
        return list(count.values())

            
        
        