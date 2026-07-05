class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operands='+*-/'
        stack=[]
 
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
        
        return int(stack[-1])
                
                


