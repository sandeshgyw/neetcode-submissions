class Solution:
    def numDecodings(self, s: str) -> int:
        ways=0
        cache={}

        def backtrack(i):
            nonlocal ways

            if i in cache:
                return cache
            if i>=len(s):
                return 1
            
            if s[i]=='0':
                return 0
            
            #single digit invlaid only if 0

            ways+=backtrack(i+1)
            
            #now we enter 2 digit area

            if s[i]=='0':
                return 0

            if i+1>=len(s):
                return 1
    

            if s[i]=='1' or (s[i]=='2' and s[i+1] in '0123456'):
                ways+=backtrack(i+2)
            
            cache[i]=ways
            
            return cache[i]
        backtrack(0)

        return ways
            

        