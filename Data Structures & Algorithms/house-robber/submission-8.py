class Solution:
    def rob(self, nums: List[int]) -> int:

        def dfs(i):
            #this function gives how much max I can loot from i onwards

            if i>=len(nums):
                return 0
            
            rob_house=nums[i]+dfs(i+2)
            #rob_house has money it robs from this house and we trust dfs will give it 
            #the correct from remaining houses

            dont_rob=dfs(i+1)
            #dont_rob is the total from i onwards when i is not robbed

            return max(rob_house,dont_rob)
        
        return dfs(0)