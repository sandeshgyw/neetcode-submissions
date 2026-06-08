class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        result=0
        cache={}

        def climb(i):
            # this function takes in the stair I am at
            # this step is the best step there is to take
            # there are n-1 indices
            # base case is when i exceed end of stairs
            
            if i>=n:
                # if stair is at i==n it should still work
                return 0

            if i not in cache:
                       #from each stair it can take either 1 step or two step
            # 1 step
                one=climb(i+1)
            #2 step
                two=climb(i+2)
                minCost=min(one,two)
                cache[i]=minCost

     
            return cost[i]+cache[i]

        result=min(climb(0),climb(1))
        return result



            

        