class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring=set()#window_state
        l=0
        maxlen=0


        for r in range(len(s)):
            while s[r] in substring:
                #invalid window
                substring.remove(s[l])
                l+=1

            substring.add(s[r])    
            maxlen=max(maxlen,r-l+1)
        return maxlen



        