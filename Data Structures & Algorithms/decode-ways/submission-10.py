class Solution:
    def numDecodings(self, s: str) -> int:
        


        def decode(i):
            if i==len(s):
                return 1
            
            if s[i]==0:
                return 0
            #if it reaches here means it does not start with 0
            #max one digit is 9 so any is valid
            ways=decode(i+1)#onedigit ways

            #now if it does not start with 0
            #it could still be invalid if its two digit
            #so before choosing to go two digit we need to make sure
            # starting digit is not more than 2 and if it is 2 then next digit 
            #is not other than 0,1,2,3,4,5,6
            #if all these meet then only we can call two_digit
            if s[i]=='0':
                return 0

            if s[i] =='1' or (i+1 < len(s) and (s[i] =='2' and s[i+1] in '0123456')):
                ways+=decode(i+2)
            
            return ways
        
        return decode(0)
            
        