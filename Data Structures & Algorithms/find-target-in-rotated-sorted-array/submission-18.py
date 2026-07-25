class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r=0,len(nums)-1

        while l<r:
            m=l+(r-l)//2

            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        
        if target==nums[l]:
            return l
        
        if target>nums[l]:
            r=len(nums)-1
            l=0
        else:
            r=l
            l=0
        print(l,r)
        
        while l<=r:
            m=l+(r-l)//2

            if nums[m]==target:
                return m

            if nums[m]<target:
                l=m+1
            else:
                r=m-1
        
        return -1