class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        maxPile=max(piles)

        lowRate,highRate=1,maxPile
        k=highRate

        while lowRate<=highRate:
            rate=lowRate+(highRate-lowRate)//2
            timeTaken=0

            for pile in piles:
                timeTaken+=math.ceil(pile/rate)
            
           
            
            if timeTaken<=h:
                k=rate
                highRate=rate-1
            else:
                lowRate=rate+1

        return k
            

                
        