class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result+=num
        for num in nums:
            self.result+=num
        return self
    def subtract(self, num, *nums):
        self.result-=num
        for num in nums:
            self.result-=num
        return self

md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)

md = MathDojo()
x = md.add(50).add(5,5,6).subtract(25,50).result
print(x)

md = MathDojo()
x = md.add(1).add(1,1,1,1,1).subtract(1).result
print(x)