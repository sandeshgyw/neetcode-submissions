class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashset_s=defaultdict(int)
        

        for char in s:
            hashset_s[char]+=1
        
        for char in t:
            if char not in hashset_s:
                return False
            if hashset_s[char]==0:
                return False

            hashset_s[char]-=1
        
        return True
        

        