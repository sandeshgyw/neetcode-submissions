class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies=[]

        for i in range(len(nums)+1):
            frequencies.append([])

        freq_count=defaultdict(int)
        result=[]

        for num in nums:
            freq_count[num]+=1
        
        for key in freq_count:
            frequencies[freq_count[key]].append(key)
        
  
        
        for i in range(len(nums),-1,-1):
            if len(frequencies[i])!=0:
                for num in frequencies[i]:
                    result.append(num)
                    if len(result)==k:
                        return result
        
        return result
        
       









        

        
        



        