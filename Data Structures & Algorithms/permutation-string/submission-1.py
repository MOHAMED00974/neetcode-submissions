class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n= len(s1)
        ref, cur= {}, {}
        if len(s2)< n:
            return False
        for x in s1:
            ref[x]= ref.get(x, 0)+1

        for x in range(n):
            cur[s2[x]]= cur.get(s2[x], 0)+1
        
        if ref== cur:
            return True

        for x in range(n, len(s2)):
            cur[s2[x-n]]-= 1
            if not cur[s2[x-n]]:
                cur.pop(s2[x-n])
            
            cur[s2[x]]= cur.get(s2[x], 0)+1
            if cur== ref:
                return True
        
        return False