class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet=set()
        starters=set()
        maxLen=1
        for num in nums:
            numsSet.add(num)
        
        for num in numsSet:
            if num-1 not in numsSet:
                starters.add(num)
        print(starters)

        
        for num in starters:
            length=1
            while num+length in numsSet:
                length+=1
            
            maxLen=max(length,maxLen)
        
        return maxLen


        