"""You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""

# brute force solution
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         answer = [""]
#         shorter = min(len(word1), len(word2))
        
#         for i in range(shorter):
#             answer.append(word1[i])
#             answer.append(word2[i])
        
#         if len(word1) > len(word2):
#             answer.append(word1[shorter:])
#         else:
#             answer.append(word2[shorter:])
        
#         return ''.join(answer)

#optimized

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        merged = []
        
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged.append(word1[i])
                i += 1
            if j < len(word2):
                merged.append(word2[j])
                j += 1
                
        return ''.join(merged)
