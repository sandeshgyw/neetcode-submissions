class Solution:
    def numDecodings(self, s: str) -> int:
        res=[]
        result=[]


        def decode(i):#0
        #if valid way send 1 else 0
            if i==len(s):
                return 1
            
            if s[i]=='0':
                return 0

            one_digit=decode(i+1)
            two_digit=0

            if i+1<len(s) and (s[i]=='1' or (s[i]=='2' and s[i+1] in '0123456')):
                two_digit=decode(i+2)
            
            return one_digit+two_digit
        
        return decode(0)


        