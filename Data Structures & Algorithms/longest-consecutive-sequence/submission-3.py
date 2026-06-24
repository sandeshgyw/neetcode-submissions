class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        length=0
        starters=set()

        for num in numSet:
            if num-1 not in numSet: # starting of a seqence
                currentLength=1
                current=num
                while current+1 in numSet:
                    currentLength+=1
                    current+=1
                length=max(length,currentLength)
                



        
        return length

            



        