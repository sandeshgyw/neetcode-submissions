class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
 
        cache={}
    
        def backtrack(i,total):
            #this function checks if the coin makes the sum to amount or not
            #here i is the coin I am taking into consideration now and total
            #is the total of the coins I have already considered
            if total>amount:
                return float('+inf')
            if amount==total: 
                return 0
            if i==len(coins):
                return float('+inf')

            if (i,total) in cache:
                return cache[(i,total)]
           
           
            take=1+backtrack(i,total+coins[i])
            skip=backtrack(i+1,total)

            cache[(i,total)]=min(take,skip)
            return cache[(i,total)]
        
        result=backtrack(0,0)
  

        return result if result !=float('+inf') else -1
                
            

            



        