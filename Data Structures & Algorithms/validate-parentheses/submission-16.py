class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closedToOpen={
            ')':'(',
            '}':'{',
            ']':'['
        }

        for i in range(len(s)):
            if s[i] in closedToOpen:
                if not stack or stack.pop()!=closedToOpen[s[i]]:
                    return False
        
            else:
                stack.append(s[i])
            
        
        return stack==[]

        