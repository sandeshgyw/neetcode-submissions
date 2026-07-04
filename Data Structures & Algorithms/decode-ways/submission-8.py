class Solution:
    def numDecodings(self, s: str) -> int:
      
        cache={}

        def backtrack(i):
           

            if i in cache:
                return cache[i]
            if i>=len(s):
                return 1
            
            if s[i]=='0':
                return 0
            #single digit invlaid only if 0
            single_digit=backtrack(i+1)
            #now we enter 2 digit area
            #also proves that s[i]!=='0' but could have other issues

            #2 digit invalids are: s[i]>2 

            if i+1>=len(s):
                return 1
            
            if int(s[i:i+2])>26:
                return 0

            two_digit=backtrack(i+2)
            
            cache[i]=two_digit+single_digit
            
            return cache[i]
        return backtrack(0)

        
            

        