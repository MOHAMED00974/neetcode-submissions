import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo= {}
        
        for x in nums:
            memo[x]= memo.get(x, 0)+1
        
        que= []

        for key, val in memo.items():
            heapq.heappush(que, (-1* val, key))
        
        ans= []
        for _ in range(k):
            ans.append(heapq.heappop(que)[1])
        
        return ans
