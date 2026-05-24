class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 
        
        count = Counter(s)
        for ch in t :
            if ch in count and count[ch] > 0:
                if count[ch] > 1:

                    count[ch] -= 1
                else:
                    del count[ch]
            else :
                return False
        return True
        
            
        
            

















        # if len(s) != len(t):
        #     return False 
       
        # count = Counter(s)

        # for ch in t :
        #     if ch not in count or count[ch] == 0 :
        #         return False
        #     count[ch] -= 1

        # return True



        