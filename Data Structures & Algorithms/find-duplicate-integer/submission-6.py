class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)-1
        numbers=set()

        for i in range(n):
            numbers.add(i+1)


        for i in range(len(nums)):
            if nums[i] not in numbers:
                return nums[i]
            numbers.remove(nums[i])



        