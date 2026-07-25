class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        stack.append((target-position[0])/speed[0])

        for i in range(len(position)):
            if (target-position[i])/speed[i] > stack[-1]:
                stack.append((target-position[i])/speed[i])
            
        return len(stack)

        