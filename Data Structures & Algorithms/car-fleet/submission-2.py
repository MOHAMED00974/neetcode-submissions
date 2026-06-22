class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n= len(speed)
        
        for x in range(n):
            position[x]= (position[x], speed[x])
        
        position.sort()

        time= [0 for _ in range(n)]
        for x in range(n):
            time[x]= (target-position[x][0])/position[x][1]
        
        stack= []

        for t in time:
            while len(stack) and t>= stack[-1]:
                stack.pop()
            stack.append(t)
        
        return len(stack)
