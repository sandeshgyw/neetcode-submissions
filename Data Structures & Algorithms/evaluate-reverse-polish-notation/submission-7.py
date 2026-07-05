class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operands='+*-/'
        stack=[]

        def add(a,b):
            return a+b
        def sub(a,b):
            return a-b
        def mul(a,b):
            return a*b
        def div(a,b):
            return a//b
        
        for i in range(len(tokens)):
            stack.append(tokens[i])
            if stack[-1] in operands:
                operand=stack.pop()
                b=int(stack.pop())
                a=int(stack.pop())

                if operand=='+':
                    stack.append(a+b)
                if operand=='-':
                    stack.append(a-b)
                if operand=='*':
                    stack.append(a*b)
                if operand=='/':
                    stack.append(a//b)
        
        return stack[-1]
                
                


