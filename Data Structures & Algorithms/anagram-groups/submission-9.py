class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group together anagrams
        res=defaultdict(list)

        for string in strs:
            # sort the string
            sortedS=''.join(sorted(string))
            res[sortedS].append(string)
        
        return list(res.values())
        




        
   

        