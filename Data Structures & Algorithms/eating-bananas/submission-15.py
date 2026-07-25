class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       
        rates=[] 

     
        
        #BS on this
        l,r=1,max(piles)
        res=r

        while l<=r:
            k=l+(r-l)//2
            total=0
            for pile in piles:
                total+=math.ceil(pile/k)
                    
            if total<=h:
                res=min(res,k)
                r=k-1
            else:
                l=k+1
        
        return res






        