class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2!=0:
            return False

        closedToOpen={
            '}':'{',
            ')':'(',
            ']':'['
        }
        
        stack=[]

        for i in range(len(s)):
            if s[i] in closedToOpen:
                #if it is a closing bracket
                if not stack:
                    return False
                if stack.pop()!=closedToOpen[s[i]]:
                    return False
            else:
                #its an opening bracket
                stack.append(s[i])
        
        return stack==[]
        