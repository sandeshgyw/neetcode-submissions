class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #take just first element and assign sum as that
        # if adding next num makes it -ve then move to start from next
        #if adding it does not make it negative then keep adding it to subrray

        totalSum=nums[0]
        subArray=[]
        largest=nums[0]

        for i in range(1,len(nums)):
            if totalSum+nums[i] >= 0:
                totalSum+=nums[i]
                subArray.append(nums[i])
                largest=max(largest,totalSum)
            else:
                totalSum=0
                subArray=[]
        
        return largest


        
        