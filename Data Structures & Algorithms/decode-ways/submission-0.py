class Solution:
    def numDecodings(self, s: str) -> int:

        def dfs(i):
            #number of ways this digit can be decoded
            if i==len(s):
                return 1
            if s[i]=='0':
                return 0


            result=dfs(i+1)

            if i+1<len(s) and (s[i]=="1" or (s[i]=='2' and s[i+1] in "123456")):
                result+=dfs(i+2)
            return result

        return dfs(0)