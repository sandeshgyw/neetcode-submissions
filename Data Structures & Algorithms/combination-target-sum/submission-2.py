class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        result=[]

        def backtrack(i,total):
            if i>len(nums)-1:
                return
            if total==target:
                result.append(res.copy())
                return
            
            if total>target:
                return

            res.append(nums[i])
            backtrack(i,total+nums[i]) #can repeat the same number
            res.pop()
            backtrack(i+1,total)

        backtrack(0,0)

        return result

        