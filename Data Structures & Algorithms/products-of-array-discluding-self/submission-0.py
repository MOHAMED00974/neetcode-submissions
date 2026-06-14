class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        prefix, suffix= nums[:], nums[:]
        
        ans= [0 for _ in range(n)]
        
        for x in range(1, n):
            prefix[x]*= prefix[x-1]
        
        for x in range(n-2, -1, -1):
            suffix[x]*= suffix[x+1]
        
        ans[0]= suffix[1]
        ans[n-1]= prefix[n-2]

        for x in range(1, n-1):
            ans[x]= suffix[x+1]*prefix[x-1]
        return ans
            
            
        