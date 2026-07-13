class Solution:
    def climbStairs(self, n: int) -> int:
        cache={}


        def climb(i):
            #this function returns 1 if valid branch and 0 if invalid
            #my job is to cumulate them
            if i==n:
                return 1
            
            if i>n:
                return 0

            if i not in cache:
                cache[i]=climb(i+1)+climb(i+2)

            

            return cache[i]
        return climb(0)
            

        