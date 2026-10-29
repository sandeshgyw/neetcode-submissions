class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group together anagrams
        res=defaultdict(list)

        for string in strs:
            # sort the string
            count=26*[0]

            for ch in string:
                count[ord(ch)-ord('a')]+=1
            
            res[tuple(count)].append(string)
        
        return list(res.values())

     
        




        
   

        