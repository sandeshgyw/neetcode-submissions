class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]

        for i in range(len(nums)):
            a=nums[i]

            while a>0:
                return result
            #if the num is >0 then all after it are also >0
            
            if i>0 and nums[i-1]==nums[i]:
                continue
            #if the next fixed num is same as previous
            #we move forward
            #now if we reach here means we have locked a valid num as i
            #now we do normal 2sum

            l,r=i+1,len(nums)-1

            while l<r:
                total=nums[i]+nums[l]+nums[r]

                if total>0:
                    r=r-1
                elif total<0:
                    l=l+1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                 
                    while nums[l]==nums[l-1]:
                        l+=1
            
        return result


        