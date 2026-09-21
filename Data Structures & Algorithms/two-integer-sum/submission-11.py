class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map={}# map value to index

        for i,num in enumerate(nums):
            if target-num in index_map:
                return [index_map[target-num],i]
            
            index_map[num]=i


        