class Solution:
    def numDecodings(self, s: str) -> int:
        

        def decode(i):
            #this functions gives
            #total paths that reach the end validly
            #or how many ways can we decode moving forward from this index
            #valid path
            if i>=len(s):
                return 1
            #invalid path
            if s[i]=='0':
                return 0
            
            
            ways=decode(i+1)
            #if one digit is not 0 then we can move forward
            #but for 2 digit, there are other conditions and only
            #if that satisfies then we move forward

            if i+1<len(s) and (s[i]=='1' or (s[i]=='2' and s[i+1] in '0123456')):
                ways+=decode(i+2)
            
            return ways
        
        return decode(0)

        