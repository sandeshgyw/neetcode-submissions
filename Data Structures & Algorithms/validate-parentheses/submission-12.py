class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closedToOpen={
            ')':'(',
            '}':'{',
            ']':'['
        }

        if s[0] in closedToOpen:
            return False


        for i in range(len(s)):
            if s[i] not in closedToOpen:
                #means open bracket
                stack.append(s[i])
            elif s[i] in closedToOpen:
                #means closed bracket
                #the incoming closed bracket
                # is not euqal to the latest open bracket in stack
                if stack.pop()!=closedToOpen[s[i]]:
                    return False
        
        return stack==[]

        