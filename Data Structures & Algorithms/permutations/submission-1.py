class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        res=[]
        

        def backtrack(i):
            if len(res)==len(nums):
                result.append(res.copy())
                return
            
            for k in range(len(nums)):
                if nums[k] not in res:
                    res.append(nums[k])
                    backtrack(k+1)
                    res.pop()
         

                    

        backtrack(0)
        return result



        