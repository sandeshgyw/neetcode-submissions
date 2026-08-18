class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the pivot point
        # then I have two sections
        # then i figure which section has target then do BS on it

        #find the pivot
        l,r=0,len(nums)-1

        while l<=r:
            m=l+(r-l)//2

            if nums[m]==target:
                return m
            
            if nums[m]<nums[r]:
                r=m-1
            else:
                l=m+1
        
        pivot=l
        # if target==nums[pivot]:
        #     return pivot

        r=len(nums)-1

        if target>nums[r]:
            r=pivot
            l=0

        while l<=r:
            m=l+(r-l)//2

            if nums[m]==target:
                return m
            if nums[m]>target:
                r=m-1
            else:
                l=m+1
    
        return -1

            
        

        