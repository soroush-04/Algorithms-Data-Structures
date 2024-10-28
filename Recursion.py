from typing import List

class Recursion:
    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n-1)
    
    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fibonacci(n-1) + self.fibonacci(n-2)
    
    def power(self, n, m):
        if m == 0:
            return 1
        return n * self.power(n, m-1)


sample = Recursion()
print(sample.factorial(4))
print(sample.fibonacci(3))
print(sample.power(3,3))