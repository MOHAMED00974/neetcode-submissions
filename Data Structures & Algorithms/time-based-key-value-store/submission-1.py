class TimeMap:

    def __init__(self):
        self.current= dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.current[key]= self.current.get(key, [])
        self.current[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.current.get(key) or not len(self.current[key]): 
            return ''
        l, r= 0, len(self.current[key])-1
        ans= ''
        while l<= r: 
            mid= (l+r)//2
            if self.current[key][mid][0]<= timestamp: 
                ans= self.current[key][mid][1]
                l= mid+1
            else: 
                r= mid-1
        return ans
