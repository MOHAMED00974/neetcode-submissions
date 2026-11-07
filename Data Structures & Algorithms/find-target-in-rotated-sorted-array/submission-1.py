class Solution:
    def BinarySearch(self, nums: List[int], l: int, r: int, target: int)-> int: 
        while l<= r: 
            mid= (l+r)//2
            if nums[mid]== target:
                return mid
            elif nums[mid]> target: 
                r= mid-1
            else: 
                l= mid+1
        return -1
        

    def search(self, nums: List[int], target: int) -> int:
        start= 0
        l, r= 1, len(nums)-1
        
        while l<= r: 
            mid= (l+r)//2
            if nums[mid]< nums[start]: 
                start= mid
                r= mid-1
            else: 
                l= mid+1
        
        ans= self.BinarySearch(nums, 0, start-1, target)
        if ans != -1: 
            return ans
        ans= self.BinarySearch(nums, start, len(nums)-1, target)
        return ans