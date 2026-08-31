import heapq

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n= len(nums)
        curWindow= []
        ans= []

        for x in range(k):
            heapq.heappush_max(curWindow, (nums[x], x))

        for x in range(k-1, n):
            val, idx= heapq.heappop_max(curWindow)
            while len(curWindow) and x -idx >= k:
                val, idx= heapq.heappop_max(curWindow)
            if x- idx< k:
                heapq.heappush_max(curWindow, (val, idx))
            heapq.heappush_max(curWindow, (nums[x], x))
            ans.append(curWindow[0][0])

        return ans