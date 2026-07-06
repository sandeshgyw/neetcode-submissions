class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list)
        result=[]



        for string in strs:
            key=[0]*26
            for i in range(len(string)):
                key[ord('a')-ord(string[i])]+=1
            
            groups[tuple(key)].append(string)
        
        for key in groups:
            result.append(groups[key])

        return result

            


        