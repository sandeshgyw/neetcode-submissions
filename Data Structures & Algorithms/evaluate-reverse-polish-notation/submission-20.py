class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operands='+-*/'

        def calculate(operator,num1,num2):
            if operator =="+":
                return num1+num2
            if operator =="-":
                return num1-num2
            if operator =="*":
                return num1*num2
            if operator =="/":
                return int(num1/num2)

        for operand in tokens:
            if operand in operands:
                num2=stack.pop()
                num1=stack.pop()

                result=calculate(operand,num1,num2)
                stack.append(result)
            else:
                stack.append(int(operand))
        
        return (stack[-1])