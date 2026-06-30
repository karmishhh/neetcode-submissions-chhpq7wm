class StockSpanner:

    def __init__(self):
        self.stack = []        

    def next(self, price: int) -> int:
        counter = 1
        while self.stack and self.stack[-1][1] <= price:
            prev_counter, prev_price = self.stack.pop()
            counter += prev_counter
        
        self.stack.append((counter, price))

        return counter


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)