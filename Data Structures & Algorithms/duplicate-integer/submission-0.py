class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            if freq.get(num) == None:
                freq[num] = 0
            freq[num] += 1
            if freq[num] > 1:
                return True
        return False