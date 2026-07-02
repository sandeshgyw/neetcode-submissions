class Solution:
    def climbStairs(self, n: int) -> int:
        #number of ways hence number of times the valid case is reached
        cache={}
        def climb(i):

            if i==n:
                #valid case
                return 1

            if i>n:
                #invalid case
                return 0
            
            if i not in cache:
                cache[i]=climb(i+1)+climb(i+2)

            
        

            return cache[i]
        
        return climb(0)

        