class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands="+-*/"
        stack=[]


        for val in tokens:
            if val not in operands:
                stack.append(val)
            else:
                num1=int(stack.pop())
                num2=int(stack.pop())

                if val == '+':
                    stack.append(num1+num2)
                if val == '-':
                    stack.append(num1-num2)
                if val == '*':
                    stack.append(num1*num2)
                if val == '/':
                    stack.append(int(num1/num2))
        
        return stack[-1]

        