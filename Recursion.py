from typing import List

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

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

    def in_order_traversal(self, root: TreeNode):
        if root:
            self.in_order_traversal(root.left)
            print(root.value)
            self.in_order_traversal(root.right)
    
    def combine(self, nums, k):
        def backtrack(start, path):
            if len(path) == k: #base case
                result.append(path[:])
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        result = []
        backtrack(0, [])
        return result

sample = Recursion()
print(sample.factorial(4))
print(sample.fibonacci(3))
print(sample.power(3,3))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("In-Order Traversal:")
sample.in_order_traversal(root)  

combinations = sample.combine([1, 2, 3, 4], 2)
for combo in combinations:
    print(combo)