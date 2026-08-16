class Solution:
    def climbStairs(self, n: int) -> int:
        cache={}

        def climb(i):
            #contract: number of ways to reach top from ith stair onward

            if i>n:
                return 0
            if i==n:
                return 1
            
            if i not in cache:
                cache[i]=climb(i+1)+climb(i+2)

            
            return cache[i]

        return climb(0)

        
        