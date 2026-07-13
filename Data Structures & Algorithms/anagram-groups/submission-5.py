class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp=defaultdict(list)
        result=[]

        for string in strs:
            key=[0]*26

            for i in range(len(string)):
                key[ord(string[i])-ord('a')]+=1
            
            mapp[tuple(key)].append(string)
            
        for vals in mapp.values():
            result.append(vals)
        
        return result

        


            