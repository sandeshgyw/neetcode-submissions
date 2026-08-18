class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        time=[0]*len(position)
        for i in range(len(position)):
            time[i]=(position[i],(target-position[i])/speed[i])
        #time=(time,pos)

        time.sort(reverse=True)

        
        

        for t in time:
            if stack and t<stack[-1]:
                stack.append(t)
            else:
                stack.append(t)
     
        
        return len(stack)-1





        