class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        left = 0
        result = 0

        for r in range(len(s)):
            if s[r] in count:
                left = max(count[s[r]] + 1, left)
            count[s[r]] = r
            result = max(result, r - left + 1)
        return result