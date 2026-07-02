class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #all combo = backtrack

        result=[]
        res=[]


        def backtrack(i):
            #valid
            if i==len(nums):
                result.append(res.copy())
                return

            res.append(nums[i])
            backtrack(i+1)
            res.pop()
            backtrack(i+1)
        backtrack(0)

        return result


        