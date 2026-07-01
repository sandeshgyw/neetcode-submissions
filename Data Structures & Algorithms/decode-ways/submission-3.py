class Solution:
    def numDecodings(self, s: str) -> int:
   


        def dfs(i):
           
            if i==len(s):
                return 1
            
            #invalid cases
            #for single digit only if 0 then invlaid

            if s[i]=='0':
                return 0
            
            ways=dfs(i+1)
       

            if s[i]!='0' and i+1<len(s) and (s[i]=='1' or (s[i]=='2' and s[i+1] in '0123456')):
                ways+=dfs(i+2)
            
            return ways
        
        return dfs(0)
        