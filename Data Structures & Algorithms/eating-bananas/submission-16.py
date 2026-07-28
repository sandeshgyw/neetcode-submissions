class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        maxPile=max(piles)

        lowRate,highRate=1,maxPile

        while lowRate<=highRate:
            rate=lowRate+(highRate-lowRate)//2
            timeTaken=0

            for pile in piles:
                timeTaken+=math.ceil(pile/rate)
            
            if timeTaken==h:
                return rate
            
            if timeTaken<h:
                highRate=rate-1
            else:
                lowRate=rate+1
        return lowRate
            

                
        