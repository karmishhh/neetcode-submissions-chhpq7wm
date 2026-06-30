class StockSpanner:

    def __init__(self):
        self.stack = []  

    def next(self, price: int) -> int:
        i = 1
        counter = 1
        while i <= len(self.stack) and price >= self.stack[-i]:
            counter += 1
            i += 1
        self.stack.append(price)
        
        return counter