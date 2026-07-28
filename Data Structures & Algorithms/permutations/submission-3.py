class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        res=[]


        def backtrack():
            if len(res)==len(nums):
                result.append(res.copy())
                return

            for choice in nums:
                if choice not in res:
                    res.append(choice)
                    backtrack()
                    res.pop()
        backtrack()
        return result

        