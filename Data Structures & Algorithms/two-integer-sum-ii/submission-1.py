class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n= len(numbers)
        l, r= 0, n-1
        ans= [0, 0]
        while l< r:
            cur= numbers[l]+numbers[r]
            if cur>target:
                r-=1
            elif cur<target:
                l+= 1
            else:
                ans[0]= l+1
                ans[1]= r+1
                return ans

