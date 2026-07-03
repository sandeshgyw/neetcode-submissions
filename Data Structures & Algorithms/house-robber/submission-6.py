class Solution:
    def rob(self, nums: List[int]) -> int:
        maxRob=0
        cache={}


        def rob(i):
            nonlocal maxRob
            if i>=len(nums):
                return 0

            if i not in cache:
            
                rob_house=nums[i]+rob(i+2)
            #if i decide to rob the house 
                not_rob=rob(i+1)
                cache[i]=max(rob_house,not_rob)

            maxRob=max(maxRob,cache[i])
            return cache[i]
        rob(0)
        
        return maxRob


            
        