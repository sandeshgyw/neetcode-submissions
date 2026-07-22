class Solution:
    def rob(self, nums: List[int]) -> int:
    


        def robb(i):
           
            if i>=len(nums):
                return 0
            
            #choices - rob it or not rob it

            robbed_choice=nums[i]+robb(i+2)
            #if robs the current cant rob the next one 
            not_robbed_choice=robb(i+1)

            totalRob=max(robbed_choice,not_robbed_choice)

            return totalRob

            
        return robb(0)
        

            
        