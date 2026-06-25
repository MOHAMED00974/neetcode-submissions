class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n= len(nums)
        res= set()
        for trgt in range(n):
            l, r= 0, n-1
            while l<r:
                if  l == trgt:
                    l+= 1
                    continue
                if r == trgt:
                    r-= 1
                    continue

                cur= nums[l]+ nums[r]
                if cur+ nums[trgt]> 0:
                    r-= 1
                elif cur+ nums[trgt]< 0:
                    l+= 1
                else:
                    ans= [nums[l], nums[r], nums[trgt]]
                    ans.sort()
                    res.add(tuple(ans))
                    l+= 1
                    
        
        final= []
        for x in res:
            final.append(list(x))
        
        return final