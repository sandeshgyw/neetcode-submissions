class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        numsSet=set(nums)
        maxLen=1
        consecutive_set=defaultdict(list)

        for num in range(len(numsSet)):
            if num-1 not in numsSet:
                length=0
                consecutive_set[num].append(num)

                while num+length in numsSet:
                    consecutive_set[num].append(num+length)
                    length+=1
                    maxLen=max(maxLen,length)


        return maxLen
                


        