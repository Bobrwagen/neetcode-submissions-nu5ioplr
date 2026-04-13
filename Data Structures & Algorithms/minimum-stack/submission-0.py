class MinStack:

    def __init__(self):
        self.stack = []
        self.pref = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.pref[-1] if self.pref else val)
        self.pref.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.pref.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.pref[-1]
        
