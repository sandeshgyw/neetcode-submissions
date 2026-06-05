class Solution:
    store={}
    def climbStairs(self, n: int) -> int:
        if n==1:
            if n not in self.store:
                self.store[n]=1
            return self.store[n]
        if n==2:
            if n not in self.store:
                self.store[n]=2
            return self.store[n]
        if n<0:
            return 0

        if n not in self.store:
            self.store[n]= self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.store[n]
        


        