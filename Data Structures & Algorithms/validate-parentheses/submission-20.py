class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closedToOpen={
            ')':'(',
            '}':'{',
            ']':'['
        }

        for bracket in s:
            if not stack:
                stack.append(bracket)
            else:
                if bracket not in closedToOpen:#means its a open bracket
                    stack.append(bracket)
                else:
                    #means a closed bracket
                    if stack.pop()!=closedToOpen[bracket]:
                        return False
        return True if not stack else False


        