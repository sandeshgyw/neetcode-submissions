class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        result=[]


        def backtrack(i):

            if len(res)==len(nums):
                result.append(res.copy())
                return
            
            for i,choice in enumerate(nums):
                if choice not in res:
                    res.append(choice)
                    backtrack(i)
                    res.pop()

        backtrack(0)
        return result