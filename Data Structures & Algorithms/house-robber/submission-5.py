class Solution:
    def rob(self, nums: List[int]) -> int:
        maxRob=0


        def rob(i):
            nonlocal maxRob
            if i>=len(nums):
                return 0
            
            rob_house=nums[i]+rob(i+2)
            #if i decide to rob the house 
            not_rob=rob(i+1)

            maxRob=max(maxRob,max(rob_house,not_rob))
            return max(rob_house,not_rob)
        rob(0)
        
        return maxRob


            
        