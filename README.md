# Algorithms and Data Structures Practice in Python

## Favorite Problems
- **Mushroom Picker**
  - Technique: Prefix Sums, Two Pointers | [Code Link](https://github.com/soroush-04/Algorithms-DS/commit/30a49e17b09a87c77d69216f6834c818f520a6ca)
- **Genomic Range Query**
  - Technique: Prefix Sums, Two Pointers, Sliding Window | [Code Link](https://github.com/soroush-04/Algorithms-DS/commit/a0d98aaf3dd05eae152d93a32d31836036871d7c)
- **Graph Valid Tree**
  - Technique: DFS, Cycle Checking, Connectivity Check | [Code Link](https://github.com/soroush-04/Algorithms-DS/commit/ea384f78d6560cc8b4b2e4e3a89144e57ce9c166)


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