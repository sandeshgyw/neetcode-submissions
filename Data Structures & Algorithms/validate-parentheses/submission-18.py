class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen={
            '}':'{',
            ')':'(',
            ']':'['
        }
        stack=[]
        if len(s)%2!=0:
            return False

        for bracket in s:
            if bracket not in closedToOpen:
                stack.append(bracket)
            else:
                if not stack:
                    return False
            
                if stack.pop()!=closedToOpen[bracket]:
                    return False
        
        return stack==[]


        