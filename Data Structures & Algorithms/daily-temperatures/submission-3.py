class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)


        

        for i in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[i],i))
          
            
            while stack and temperatures[i]>stack[-1][0]:
                temp,index=stack.pop()
                days=i-index
                res[index]=days
            
            stack.append((temperatures[i],i))
        
        return res


