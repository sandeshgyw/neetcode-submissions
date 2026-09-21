class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      
        result=[]
        key=[0]*(max(nums)+1)

        for i,num in enumerate(nums):
            key[num]+=1
    
        for i in range(k):
            top_value=max(key)
            index=key.index(top_value)
            result.append(index)
            key[index]=0

            

        return result




        

        
        



        