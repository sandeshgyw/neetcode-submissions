class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet=set()
        maxLen=1

        if not nums:
            return 0

        for num in nums:
            numsSet.add(num)
        
        for num in numsSet:
            length=1
            while num+length in numsSet:
                length+=1
            
            maxLen=max(length,maxLen)
        
        return maxLen

        