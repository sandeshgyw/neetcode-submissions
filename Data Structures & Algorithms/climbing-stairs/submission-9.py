class Solution:
    def climbStairs(self, n: int) -> int:
        #number of ways hence number of times the valid case is reached
        def climb(i):

            if i==n:
                #valid case
                return 1

            if i>n:
                #invalid case
                return 0
            
            one_step=climb(i+1)

            two_step=climb(i+2)

            return one_step+two_step
        
        return climb(0)

        