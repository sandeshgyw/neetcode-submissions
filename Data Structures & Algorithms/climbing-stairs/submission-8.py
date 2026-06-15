class Solution:
    def climbStairs(self, n: int) -> int:
        cache={}

        def climb(i):
            #i is the stair the person is at
            #i means starting from me consider all stair options

            #good case

            if i==n:
                # top of the stairs means one valid way found
                return 1
            if i>n:
                #xceeded top means this was not a valid way
                return 0

            if i not in cache:
                one_step=climb(i+1) # one step from i
            # when this ends it gives us 1 if the one step path was valid

                two_step=climb(i+2) # 2 step from i
            # when this ends it means we have checked all paths with 2 steps from this stair
                cache[i]=one_step+two_step



            return cache[i]

        return climb(0)

        