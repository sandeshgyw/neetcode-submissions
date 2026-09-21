class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_s=defaultdict(int)
        group=defaultdict(list)
        
        for string in strs:
            sorted_string=sorted(string)
            group[tuple(sorted_string)].append(string)

        return list(group.values())




        