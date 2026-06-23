class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result=[]#o(n)
        mapp=defaultdict(list)#o(n) if all uniwue

        for string in strs: #o(n)
            count=[0]*26
            
            for c in string:
                count[ord(c)-ord('a')]+=1

            mapp[tuple(count)].append(string)

        return list(mapp.values())

   
         






        