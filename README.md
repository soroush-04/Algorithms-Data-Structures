# Algorithms and Data Structures Practice in Python

## Favorite Problems
- **Mushroom Picker**
  - Technique: Prefix Sums, Two Pointers | [Code Link](https://github.com/soroush-04/Algorithms-DS/commit/30a49e17b09a87c77d69216f6834c818f520a6ca)


## Common mistakes
### Slicing 
- A[-K:]: This slice retrieves the last K elements from the list, starting from the K-th element from the end.
- A[:-K]: This slice retrieves all elements from the beginning of the list up to (but not including) the last K elements.
  - Sample problem: cyclic rotation

### Set()
- Whenever we only care about uniqueness and a single occurence, consider using sets.
- Converting the list to a set allows O(1) average time complexity for membership checks.