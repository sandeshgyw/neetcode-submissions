class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet=set()
        checkedNum=set()
        maxLen=1

        if not nums:
            return 0

        for num in nums:
            numsSet.add(num)
        
        for num in numsSet:
            length=1
            if num in checkedNum:
                continue
            checkedNum.add(num)
            while num+length in numsSet:
                checkedNum.add(num+length)
                length+=1
            
            maxLen=max(length,maxLen)
        
        return maxLen

        