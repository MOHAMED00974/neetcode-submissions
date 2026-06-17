class Solution:
    
    def longestConsecutive(self, nums: List[int]) -> int:
        hashh= set(nums)

        def check(cur, step):
            tmp= 0
            while cur in hashh:
                cur += step
                tmp+= 1
            return tmp

        ans= 0
        for num in nums:
            ans= max(check(num, 1), ans)
            ans= max(check(num, -1), ans)
        
        return ans