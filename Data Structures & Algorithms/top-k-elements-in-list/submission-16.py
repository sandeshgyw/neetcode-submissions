class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # return the most frequent elements in the array,
        # not all but the number of ones specified like top2, top 3, top 4...


        count={}
        freq=[[] for i in range(len(nums)+1)]
        for num in nums:
            count[num]=count.get(num,0)+1
        
        for number,frequency in count.items():
            freq[frequency].append(number)
        res=[]
        
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
            

        


        arr=[]

        for number,frequency in count.items():
            arr.append([frequency,number])

        arr.sort()

    

        res=[]

        while len(res)<k:
            res.append(arr.pop()[1])
        
        return res





    



        





        



        








        




       