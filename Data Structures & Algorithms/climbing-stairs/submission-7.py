class Solution:
    def climbStairs(self, n: int) -> int:

        def climb(i):
            #i is the stair the person is at
            #i means starting from me consider all stair options

            #good case

            if i==n:
                # top of the stairs pugesi valid way vettiyo
                return 1
            if i>n:
                #stairs ko end katch vanesi this is not valid way
                return 0

            one_step=climb(i+1) # one step from i

            two_step=climb(i+2) # 2 step from i

            return one_step + two_step

        return climb(0)

        