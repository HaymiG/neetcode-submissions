class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for ch in strs:
            res += str(len(ch)) + "#" + ch
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i : j]) 
            word = s[j + 1 : j + 1 +length]
            result.append(word)
            i = length + j + 1
        return result