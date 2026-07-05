class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        openToClose={
            '}':'{',
            ')':'(',
            ']':'['
        }

        for i in range(len(s)):
            if s[i] not in openToClose:
                #means its an open bracket
                stack.append(s[i])
            
            else:
                if stack and stack.pop()!=openToClose[s[i]]:
                    return False
        
        if stack:
            return False
        
        return True

        