class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res=[]
        hashmap={}

        def backtrack(index,count,prev):
            #contract: starting from this number how long is the subsequence
            if (index,prev) in hashmap:
                return hashmap[(index,prev)]
           

            if index>=len(nums):
                return 0
            
            length=0
            
            for i in range(index,len(nums)):
                if nums[i]<=prev:
                    continue
                res.append(nums[i])
                length=max(length,1+backtrack(i+1,count+1,nums[i]))
                res.pop()
            hashmap[(index,prev)]=length
            return length

        return backtrack(0,0,float('-inf'))
       



            


        