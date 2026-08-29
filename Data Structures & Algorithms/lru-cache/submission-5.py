class LRUCache:

    def __init__(self, capacity: int):
        self.k=capacity
        self.cache={}
        self.queue=[]
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

   

        index=self.queue.index(key)
        temp=self.queue.pop(index)
        self.queue.append(temp)

        return self.cache[key]
        
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            index=self.queue.index(key)
            temp=self.queue.pop(index)
            self.cache[key]=value
            self.queue.append(temp)
            
        else:
            if len(self.queue)>=self.k:
                temp=self.queue.pop(0)
                del self.cache[temp]
                self.cache[key]=value
                self.queue.append(key)
            else:
                self.cache[key]=value
                self.queue.append(key)
        
      


        
