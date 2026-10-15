class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
    
        map_s={}
        map_t={}

        for ch in s:
            if ch not in map_s:
                map_s[ch]=1
            else:
                map_s[ch]+=1
    
        for ch in t:
            if ch not in map_t:
                map_t[ch]=1
            else:
                map_t[ch]+=1
    
        return map_s==map_t
    

        
    



    


      








        
        

        