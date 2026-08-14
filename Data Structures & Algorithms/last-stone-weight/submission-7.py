class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for num in stones:
            heapq.heappush(heap,-num)

        if not stones:
            return 0

        if len(heap)<2:
            return heap[0]

        while len(heap)>1:
            x=-heapq.heappop(heap)#largest
            y=-heapq.heappop(heap)#secondlargest
            

            if x==y:
                continue
            else:
                heapq.heappush(heap,x-y)
            
        
        return 0 if not len(heap) else heap[0]


        