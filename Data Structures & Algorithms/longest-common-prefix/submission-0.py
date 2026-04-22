class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        for i in range(1 , len(strs)):
            ch = strs[i]
            while word and word != ch[:len(word)] :
                word = word[:-1]
        return word
        