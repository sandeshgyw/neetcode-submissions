class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closedToOpen={
            ')':'(',
            '}':'{',
            ']':'['
        }

        for bracket in s:
            if bracket in closedToOpen:#means a closed bracket
                if not stack or stack[-1]!=closedToOpen[bracket]:
                    return False
                else:
                    stack.pop()
                    continue

                
            stack.append(bracket)

        return True if not stack else False


        