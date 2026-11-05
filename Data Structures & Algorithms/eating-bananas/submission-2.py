import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can(x: int)-> bool: 
            '''
                The boolean condition for our binary search.
            '''
            clock= 0
            for i in piles: 
                clock+= math.ceil(i/x)
                if clock>h:
                    return False
            return True
        
        l, r= 1, max(piles)
        
        while l<= r: 
            mid= (l+r)//2
            if can(mid):
                r= mid-1
                ans= mid
            else: 
                l= mid+1
        return ans