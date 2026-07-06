class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxHeight=0
        for i in range(len(piles)):
            maxHeight=max(maxHeight,piles[i])
            #o(n)
        results=[0]*maxHeight
        minSpeed=maxHeight
        

  
        
        l,r=1,max(piles)
       

        while l<=r:
            m=l+(r-l)//2

            
            totalHours=0

            for i in range(len(piles)):
                totalHours+=math.ceil((piles[i]/m))             
        
            if totalHours>h:
                l=m+1
            
            if totalHours<=h:
                minSpeed=min(minSpeed,m)
                r=m-1
        
        return minSpeed


            





        