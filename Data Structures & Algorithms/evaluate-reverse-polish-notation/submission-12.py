class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators="+-/*"

        stack=[]


        for val in tokens:
            if val not in operators:
                stack.append(val)
            else:
                operand=val
                b=int(stack.pop())
                a=int(stack.pop())
                if operand=='+':
                    stack.append(a+b)
                if operand=='-':
                    stack.append(a-b)
                if operand=='*':
                    stack.append(a*b)
                if operand=='/':
                    stack.append(int(a/b))

        return int(stack[-1])




        