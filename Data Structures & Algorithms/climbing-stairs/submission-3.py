class Solution:
    cache={}
    def climbStairs(self, n: int) -> int:
    #if n reaches 0 it means we found one way to reach across all stairs
    # if n reaches less than 0 means that path was not viable
       


        if n==0:
            return 1
        if n<0:
            return 0
        
        if n not in cache:
            cache[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        
        return cache[n]
        


        