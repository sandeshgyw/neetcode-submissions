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

                result=calculate(operand,int(num1),int(num2))
                stack.append(result)
            else:
                stack.append(operand)
        
        return stack[-1]