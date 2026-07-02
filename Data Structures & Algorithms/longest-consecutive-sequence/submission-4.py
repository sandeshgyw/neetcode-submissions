class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starters=defaultdict(list)
        maxlen=0


        for num in nums:
            if num-1 not in nums:
                starters[num].append(num)
            
        for num in starters:
            length=1

            while num+1 in nums:
                length+=1
                num=num+1
            maxlen=max(length,maxlen)

        return maxlen
            
        

        
        