class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result=[]


        for i in range(len(nums)):
            if nums[i]>0:
                break
        
            if i>0 and nums[i-1]==nums[i]:
                continue
            
            l,r=i+1,len(nums)-1

            while l<r:
                if nums[l]+nums[r] + nums[i]==0:
                    result.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                else:
                    if nums[l]+nums[r]< -1*nums[i]:
                        l+=1
                    else:
                        r-=1
        return result


        