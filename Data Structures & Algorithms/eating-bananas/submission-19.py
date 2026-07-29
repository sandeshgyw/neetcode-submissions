class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        highRate=max(piles)
        lowRate=1

        k=highRate


        while lowRate<=highRate:
            rate=lowRate+(highRate-lowRate)//2
            totalTime=0
            for pile in piles:
                totalTime+=math.ceil(pile/rate)

            if totalTime<=h:
                k=rate
                highRate=rate-1
            else:
                lowRate=rate+1
        
        return k



        