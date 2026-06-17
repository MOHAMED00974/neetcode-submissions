class Solution:
    def isValid(self, s: str) -> bool:
        start= { 
            '{':0, 
            '[':1, 
            '(':2
        }

        end= { 
            '}':0, 
            ']':1, 
            ')':2
        }

        stack= []
        
        for x in s:
            if x in start.keys():
                stack.append(x)
                continue
            
            if len(stack) == 0 or end[x]!= start[stack[-1]]:
                return False
            stack.pop()
        
        return len(stack)== 0 








