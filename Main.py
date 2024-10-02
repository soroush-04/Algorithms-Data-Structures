"""Problem: Find the longest substring without repeating characters.

"""

from typing import List

def solution(S: List[str]):
    subarray = set()
    left = 0
    overall_max = 0
    
    for right in range(len(S)):
        while S[right] in subarray:
            subarray.remove(S[left])
            left += 1
        subarray.add(S[right])
        overall_max = max(overall_max, (right - left + 1))
    
    return overall_max
            
            