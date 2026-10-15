class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Rewrite question
        # we have some numbers and we are given a target
        # we have to find which two numbers sum up to that target
        # we then have to return the indices of the numbers

        #Brute force Solution
        #for i in range(len(nums)):
           # for j in range(i+1,len(nums)):
               # if nums[i]+nums[j]==target:
                   # return [i,j]
        
        #Optimal Solution

        hashmap={}

        for i in range(0,len(nums)):
            #range(start_index, end_index)
            difference=target-nums[i]
            if difference in hashmap:
                return [hashmap[difference],i]
            else:
                hashmap[nums[i]]=i




        


        




            



        

        