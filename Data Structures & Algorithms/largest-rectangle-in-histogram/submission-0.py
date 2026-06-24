class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n= len(heights)
        l, r= [0 for _ in range(n)], [(n-1) for _ in range(n)]

        stack= []

        for x in range(n):
            while len(stack) and heights[x] < heights[stack[-1]]:
                r[stack[-1]]= x-1
                stack.pop()
            stack.append(x)

        stack.clear()

        for x in range(n-1, -1, -1):        
            while len(stack) and heights[x] < heights[stack[-1]]:
                l[stack[-1]]= x+1
                stack.pop()
            stack.append(x)
        
        ans= 0
        
        for x in range(n):
            cur= heights[x]*(r[x]-l[x]+1)
            ans= max(ans, cur)
        
        return ans