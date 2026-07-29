class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()

        for i in range(len(nums)):
            #if starting num is >0 no chance we get >0
            if nums[i]>0:
                return result
            #is this a repitition?
            #if yes then skip the whole loop
            if i>0 and nums[i-1]==nums[i]:
                continue
            
            l,r=i+1,len(nums)-1

            while l<r:
                #only < cause we cant have duplicates

                if nums[l]+nums[r]+nums[i]==0:
                    result.append([nums[l],nums[r],nums[i]])
                    l+=1
                    r-=1
                    while  nums[l-1]==nums[l]:
                        l+=1
                    while  nums[r+1]==nums[r]:
                        r-=1
                elif nums[l]+nums[r]+nums[i]>0:
                    r-=1
                else:
                    l+=1
                
                
        return result


            

