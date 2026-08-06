class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        result=[]

        def backtrack(start,totalSum):
            #base : correct
            if totalSum==target:
                result.append(res.copy())
                return
            #base case: incorrect
            if totalSum>target:
                return
            if start>=len(nums):
                return

            for choice in range(start,len(nums)):
                res.append(nums[choice])
                backtrack(choice,totalSum+nums[choice])
                res.pop()
        
        backtrack(0,0)
        return result


        