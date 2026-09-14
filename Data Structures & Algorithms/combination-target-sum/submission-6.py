class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        res=[]

        def backtrack(i,total):
            #contract: what number moving forward including me sum to target
            #invalid
            if total>target:
                return
            if i>len(nums)-1:
                return
            #valid
            if target==total:
                result.append(res.copy())
                
                return

            #backtrack

            res.append(nums[i])
            backtrack(i,total+nums[i])
            res.pop()
            backtrack(i+1,total)
        
        backtrack(0,0)
        return result
        