class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n= len(nums)
        memo= {}
        for x in range(n):
            if memo.get(target-nums[x]) != None:
                return [memo[target-nums[x]], x]
            
            memo[nums[x]]= x
        