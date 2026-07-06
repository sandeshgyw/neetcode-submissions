class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

 
        numSet=set(nums)
        maxlen=0
        length=1


        for num in numSet:
            current=num
            if num-1 not in numSet:
                
                length=1
                
                while current+1 in numSet:
                    length+=1
                    current=current+1
            
            maxlen=max(length,maxlen)
        
        return maxlen
                    


                #starters
        

        