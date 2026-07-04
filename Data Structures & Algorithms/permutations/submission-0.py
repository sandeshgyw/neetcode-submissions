class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        result=[]



        def backtrack():
            if len(res)==len(nums):
                result.append(res.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in res:
                    res.append(nums[i])
                    backtrack()
                    res.pop()
        backtrack()

        return result

        