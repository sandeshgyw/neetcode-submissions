class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        window={}
        maxLen=0
        maxFreqWindow=0

        for r in range(len(s)):
            window[s[r]]=window.get(s[r],0)+1

            maxFreqWindow=max(maxFreqWindow,window[s[r]])
            windowLen=r-l+1

            while windowLen-maxFreqWindow>k:
                #invalid window
                
                window[s[l]]=window.get(s[l],0)-1
                l+=1
                windowLen-=1
            
            maxLen=max(maxLen,windowLen)
            
        
        return maxLen

            
            




            


            



            

        