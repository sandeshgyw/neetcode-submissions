class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_s=defaultdict(int)
        group=defaultdict(list)

        
        for string in strs:
            key=[0]*26
            for ch in string:
                key[ord(ch)-ord('a')]+=1
        
            group[tuple(key)].append(string)

        return list(group.values())




        