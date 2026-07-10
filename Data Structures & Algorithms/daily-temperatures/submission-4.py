class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack=[]
        result=[0]*len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[i]>stack[-1][0]:
                #this temp is greaetr
                oldTemp,day=stack.pop()
                result[day]=i-day
            stack.append((temperatures[i],i))

        return result

        





        