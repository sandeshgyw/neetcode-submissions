class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        numsSet=set(nums)#O(n)
        maxLen=0

        for num in numsSet:
            #o(n)
            if num-1 not in numsSet:
                #o(1)
                length=0
                while num+length in numsSet:
                    #O(1) 
                    length+=1
                maxLen=max(maxLen,length)
        return maxLen
                


        