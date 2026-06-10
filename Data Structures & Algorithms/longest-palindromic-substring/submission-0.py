class Solution:
    def longestPalindrome(self, s: str) -> str:
        resultingIndex=0
        resultingLength=0

        for i in range(len(s)):
            #assume odd length
            l,r=i,i

            while l>=0 and r<len(s) and s[l]==s[r]:
                window=r-l+1
                if window>resultingLength:
                    resultingIndex=l
                    resultingLength=window
                l-=1
                r+=1
            
            #assume even length
            l=i
            r=i+1

            while l>=0 and r<len(s) and s[l]==s[r]:
                window=r-l+1
                if window>resultingLength:
                    resultingIndex=l
                    resultingLength=window
                l-=1
                r+=1
            
        return s[resultingIndex:resultingIndex+resultingLength]




            


        
        