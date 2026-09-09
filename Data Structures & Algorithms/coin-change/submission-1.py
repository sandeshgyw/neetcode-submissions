class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res=[]
        result=[]
    
        def backtrack(i,total):
            #this function checks if the coin makes the sum to amount or not
            # and return -1 if invalid

           
            if total>amount:
                return
            if amount==total:
                result.append(res.copy())
            if i==len(coins):
                return
            
            res.append(coins[i])
            backtrack(i,total+coins[i])
            res.pop()
            backtrack(i+1,total)
        
        backtrack(0,0)
        minLength=float('+inf')
        
        for i in range(len(result)):
            minLength=min(minLength,len(result[i]))

        return minLength if result else -1
                
            

            



        