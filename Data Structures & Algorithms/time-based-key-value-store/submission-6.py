class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        value_ts_pairs = self.hashmap.get(key, [])
        res = ''
        left = 0
        right = len(value_ts_pairs) - 1
        while left <= right:
            mid = left+(right-left) // 2 
            if value_ts_pairs[mid][1] <= timestamp: # at 1st index will be our timestamp
                res = value_ts_pairs[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return res

        
