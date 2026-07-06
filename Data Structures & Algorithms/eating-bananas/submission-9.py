class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
     

 
        
        

        
        
        l,r=1,max(piles)
        minSpeed=r
       

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


            





        