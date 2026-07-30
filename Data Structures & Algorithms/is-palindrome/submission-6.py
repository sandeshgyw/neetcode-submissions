class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()

        l,r=0,len(s)-1

        while l<r:
            while  not s[r].isalpha():
                r-=1
            while not s[l].isalpha():
                l+=1

            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        
        return True

       
            
        
        