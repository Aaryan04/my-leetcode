class StockPrice:

    def __init__(self):
        self.time_to_price = dict()     # stores {timestamp: current price}
        self.latest_ts = -1      # track the max timestamp that we have reached 
        self.max_heap = []              # (-price, timestamp)
        self.min_heap = []              # (price, timestamp)

        # heapq.heapify(self.max_heap)
        # heapq.heapify(self.min_heap)

    def update(self, timestamp: int, price: int) -> None:
        self.time_to_price[timestamp] = price
        self.latest_ts = max(self.latest_ts, timestamp)
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))
        
        return self.time_to_price[timestamp]

    def current(self) -> int:
        return self.time_to_price[self.latest_ts]

    def maximum(self) -> int:

        while self.max_heap:    
            price, ts = self.max_heap[0]
            price = -price        
            if price == self.time_to_price[ts]:
                return price
            else:    
                heapq.heappop(self.max_heap)

    def minimum(self) -> int:

        while self.min_heap:    
            price, ts = self.min_heap[0]    
            if price == self.time_to_price[ts]:
                return price
            else:    
                heapq.heappop(self.min_heap)
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()