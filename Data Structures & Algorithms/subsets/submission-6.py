class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        res=[]


        def backtrack(i):
            #contract: subsets from this index onward
         

            if i>len(nums)-1:
                result.append(res.copy())
                return
            
            res.append(nums[i])
            backtrack(i+1)
            res.pop()
            backtrack(i+1)
            
        
        backtrack(0)
        return result

        