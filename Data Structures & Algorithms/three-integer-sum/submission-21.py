class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()#o(nlogn)

        for i,num in enumerate(nums):
            fixed_num=num

            if fixed_num>0:
                break

            if i>=0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1

            while l<r:
                if nums[l]+nums[r]+nums[i]==0:
                    result.append([nums[l],nums[r],nums[i]])
                    l+=1
                elif nums[l]+nums[r]+nums[i]>0:
                    r-=1
                else:
                    l+=1
                
                while l<r and nums[l]==nums[l-1]:
                    l+=1
                
        return result


        