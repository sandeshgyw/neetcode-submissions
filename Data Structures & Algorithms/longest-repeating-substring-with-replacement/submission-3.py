class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        window={}#if window has max freq (a) and length of n then 
        # n-a is the num of replace,emtn available
        #if that failswindow invalid
        maxFreq=1
        res=0


        for r in range(len(s)):
            window[s[r]]=window.get(s[r],0)+1
            maxFreq=max(maxFreq,window[s[r]])

            while (r-l+1) - maxFreq >k:
                window[s[l]]-=1
                if window[s[l]]==0:
                    del window[s[l]]
                
                l+=1
            
            res=max(res,r-l+1)

        return res

            
        