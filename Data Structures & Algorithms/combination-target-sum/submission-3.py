class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        result=[]


        def backtrack(i,total):

            if total==target:
                result.append(res.copy())
                return

            if total>target:
                return
            if i==len(nums):
                return
            
            res.append(nums[i])
            backtrack(i,total+nums[i])#can choose same again
            res.pop()
            backtrack(i+1,total)

        backtrack(0,0)
        return result

