class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashset_s=defaultdict(int)
        hashset_t=defaultdict(int)

        for char in s:
            hashset_s[char]+=1
        
        for char in t:
            hashset_t[char]+=1
        
        return hashset_s==hashset_t
        

        