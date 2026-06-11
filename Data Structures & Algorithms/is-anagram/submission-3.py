class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        memo= {}
        for c in s:
            try:
                memo[c] += 1
            except:
                memo[c] = 0
                memo[c]+= 1
        
        for c in t:
            try:
                memo[c] -= 1
            except:
                return False
        
        for x in memo.values():
            if x != 0:
                return False
        
        return True
            