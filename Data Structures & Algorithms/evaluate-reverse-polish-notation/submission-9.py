import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a, b):
            return a+b
        def sub(a, b):
            return a-(b)
        def mul(a, b):
            return a*b
        def div(a, b):
            tmp = a/b
            if tmp<0:
                return math.ceil(tmp)
            return int(tmp)
        
        ops= {'+':add, '-':sub, '*':mul, '/':div}
        stack= []
        
        for x in tokens:
            if x in ops.keys():
                b= stack.pop()
                a= stack.pop()
                tmp= ops[x](a, b)
                stack.append(tmp)
                continue
            stack.append(int(x))
        
        return stack[0]