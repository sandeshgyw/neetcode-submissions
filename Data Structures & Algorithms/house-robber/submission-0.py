class Solution:
    def rob(self, nums: List[int]) -> int:
        #nums[i]: money in each house
        n=len(nums) #number of houses not indices
        #cant go to adjacent houses
        # maximum amount he can rob
        #if he starts with the first house:
            #he has to take i+2 steps everytime so that no adjacent house is it
        #if he starts with second house:
            #he has to take i+2 steps everytime
        cache={}
            
            

        def rob_house(house_index):
                #this returns how much money he is robbing from that house

                #base case is if he runs out of houses
            if house_index>=n:
                return 0

            if house_index not in cache:
                money_current=nums[house_index]
                next_house=rob_house(house_index+2)
                cache[house_index]=money_current+rob_house(house_index+2)

      

            return cache[house_index]

        return max(rob_house(0),rob_house(1))


        
        