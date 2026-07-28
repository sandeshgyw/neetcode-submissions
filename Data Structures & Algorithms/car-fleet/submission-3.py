class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]


        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        cars.sort(reverse=True)
        print(cars)
        stack=[]

        for pos,sp in cars:
            timeTaken=(target-pos)/sp
            if stack and stack[-1]>=timeTaken:
                continue
            stack.append(timeTaken)
        
        return len(stack)


        