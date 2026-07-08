class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l,r=0,0
        window={}
        max_freq=1
        longest=0

        for r in range(len(s)):
            
            window[s[r]]=window.get(s[r],0)+1

            max_freq=max(max_freq,window[s[r]])
            
            while (r-l+1) - max_freq >k:
                #invalid
                window[s[l]]-=1
                if window[s[l]]==0:
                    del window[s[l]]
                l+=1
            #now its valid


            longest=max(longest,r-l+1)
        return longest

            

        