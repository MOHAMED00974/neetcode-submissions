class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n= len(temperatures)
        ans= [0 for _ in range(n)]
        stk= []

        for x in range(n):
            while len(stk) and temperatures[stk[-1]]< temperatures[x]:
                ans[stk[-1]]= x-stk[-1]
                stk.pop()
            stk.append(x)
        
        return ans


