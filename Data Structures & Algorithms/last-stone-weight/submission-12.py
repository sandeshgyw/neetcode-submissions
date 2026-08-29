class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]

        for stone in stones:
            heapq.heappush(heap,-1*stone)
        print(heap)
        
        while len(heap)>1:
            a,b=-1*heapq.heappop(heap),-1*heapq.heappop(heap)

            if a==b:
                continue
            if b<a:
                heapq.heappush(heap,-1*(a-b))
            
        return -1*heap[0] if heap else 0




        