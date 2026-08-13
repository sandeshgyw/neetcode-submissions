class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subsets=[]


        def backtrack(i):
            #contract: find all subsets starting from this i onward

            if i==len(nums):
                subsets.append(res.copy())
                return
            
            res.append(nums[i])
            backtrack(i+1)#this finds and adds all subsets starting from i+1
            #here it is done finding all subsets of i+1 with i included
            res.pop()
            #now we remove i and find subsets of all with i not not included
            backtrack(i+1)
            #this finds all subset from i+1 with iitial i not included
        backtrack(0)
        return subsets
        