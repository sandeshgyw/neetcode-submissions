class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        cache={}

        def dfs(i):
            # i am at ith house

            if i>=n:
                return 0
            if i not in cache:
                robbing_this_house=nums[i]+dfs(i+2)
                skipping_this_house=dfs(i+1)
                cache[i]=max(robbing_this_house,skipping_this_house)
            

            return cache[i]

        return dfs(0)
        