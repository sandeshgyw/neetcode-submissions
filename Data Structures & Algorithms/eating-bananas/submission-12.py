class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate=max(piles)#4
        rates=[]

        for i in range(rate):
            rates.append(i+1)
        
        #BS on this
        l,r=0,len(rates)-1

        while l<r:
            mid=l+(r-l)//2
            total=0
            for pile in piles:
                total+=math.ceil(pile/rates[mid])
            
            if total==h:
                l=mid
                continue
            
            if total>h:
                l=mid+1
            
            else:
                r=mid-1
        
        return rates[l]






        