class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        numsSet=set(nums)
        maxLen=0
 

        for num in numsSet:
      
            if num-1 not in numsSet:
           
                length=0
                while num+length in numsSet: 
                    length+=1
                    maxLen=max(maxLen,length)
        return maxLen
                


        