# Algorithms and Data Structures Practice in Python

## Favorite Problems
- **Mushroom Picker**
  - Technique: Prefix Sums, Two Pointers | [Code Link](https://github.com/soroush-04/Algorithms-DS/commit/30a49e17b09a87c77d69216f6834c818f520a6ca)
- **Genomic Range Query**
  - Technique: Prefix Sums, Two Pointers, Sliding Window | [Code Link](https://github.com/soroush-04/Algorithms-DS/commit/a0d98aaf3dd05eae152d93a32d31836036871d7c)
- **Graph Valid Tree**
  - Technique: DFS, Cycle Checking, Connectivity Check | [Code Link](https://github.com/soroush-04/Algorithms-DS/commit/ea384f78d6560cc8b4b2e4e3a89144e57ce9c166)
- **N-Queens**
  - Technique: Backtracking | [Code Link](https://github.com/soroush-04/Algorithms-DS/blob/main/favorites/n_queens.py)
- **Top K Frequent Elements**
  - Technique: Bucket Sort | [Code Link](https://github.com/soroush-04/Algorithms-DS/blob/main/favorites/top_k_frequency.py)
- **Counting Bits**
  - Technique: Bit Manipulation, Dynamic Programming | [Code Link](https://github.com/soroush-04/Algorithms-DS/blob/main/favorites/counting_bits.py)
- **Subtree of Another Tree**
  - Technique: Tree Traversal, Recursion | [Code Link](https://github.com/soroush-04/Algorithms-DS/blob/main/favorites/subtree.py)
- **Balanced Binary Tree**
  - Technique: DFS, Height Calculation | [Code Link](https://github.com/soroush-04/Algorithms-DS/blob/main/favorites/balanced_binary_tree.py)
- **Letter Combinations of a Phone Number**
  - Technique: backtracking, string join | [Code Link](https://github.com/soroush-04/Algorithms-DS/blob/main/favorites/letters_phone_numer.py)
- **Permutations**
  - Technique: backtracking | [Code Link](https://github.com/soroush-04/Algorithms-DS/blob/main/favorites/permutations.py)




## Common mistakes
### Slicing 
- A[-K:]: This slice retrieves the last K elements from the list, starting from the K-th element from the end.
- A[:-K]: This slice retrieves all elements from the beginning of the list up to (but not including) the last K elements.
  - Sample problem: cyclic rotation

### Set()
- Whenever we only care about uniqueness and a single occurence, consider using sets.
- Converting the list to a set allows O(1) average time complexity for membership checks.

### Sliding Window
- Consider using this technique when searching for specific subarrays or contiguous sequences.

### Stack
- You need to perform on current and previous index? Consider using stack for optimized performance. 

### Sorting
- Merge Sort has guaranteed O(n log n) time complexity, which can be preferable when the worst case is a concern.

### Bucket Sort
- Optimize the time complexity to O(N).
- It is a 2D array,
- We kinda try to swap and redesign the key-values of frequency hashmap.

### Trees
- In BST do not traverse the wrong subtree!
- Don't forget to propagate the state of unbalanced subtrees up the tree.

### BFS
- Consider using it for shortest path in unweighted graphs.

### DFS
- Consider using it for backtracking scenarios.

### Nested Data
- **Hashmaps**: Use `.items()` to iterate through key-value pairs and use the value to move one layer inward. 
- **Lists**: Use `item in items` to move one layer inward.

### Backtracking
- Don’t forget to undo (backtrack) changes after recursive calls.
- Recursion base case must be created accuractely.
- Don't forget to call the backtracking function at the end!
- Each for loop in a recursive callback function has its separate own state.

### Dynamic Programming
- Check for fibonnaci patterns

### Bit Manipulation
- Logical and returns the first falsy value or the last value if all are truthy.
- Logical or returns the first truthy value.
- XOR: like a toggle switch to add/remove features. Also keep in mind XOR of two same numbers is zero.
- Check LSB (least significant bit) with 'i & 1'  or 'i % 2'