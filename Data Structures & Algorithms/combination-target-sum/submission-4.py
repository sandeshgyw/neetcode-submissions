class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        result=[]

        def backtrack(i,totalSum):
            #base : correct
            if totalSum==target:
                result.append(res.copy())
                return
            
            #base case: incorrect
            if totalSum>target:
                return
            
            if i>=len(nums):
                return
            
            res.append(nums[i])
            backtrack(i,totalSum+nums[i])#can repeat same number
            res.pop()
            backtrack(i+1,totalSum)#using next index number
        
        backtrack(0,0)
        return result


        