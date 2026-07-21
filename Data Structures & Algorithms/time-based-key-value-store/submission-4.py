class TimeMap:

    def __init__(self):
        self.hashmap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = {}

        if timestamp not in self.hashmap[key]:
            self.hashmap[key][timestamp] = []
            self.hashmap[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        maxxx = 0
        for time in self.hashmap[key].keys(): 
            if timestamp >= time:
                maxxx = max(maxxx, time)
        return "" if maxxx==0 else self.hashmap[key][maxxx][0]
                
        
