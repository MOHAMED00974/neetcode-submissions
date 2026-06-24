class Solution:
    def isPalindrome(self, s: str) -> bool:
        cur= ""
        for x in s:
            if x.isnumeric() or x.isalpha():
                cur= cur+ x.lower()
        
        l, r= 0, len(cur)-1
        while l<= r:
            if cur[l] != cur[r]:
                return False
            l+=1
            r-=1
        return True