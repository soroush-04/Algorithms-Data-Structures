"""Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise."""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        checklist = {}

        for i in s:
            if i in checklist:
                checklist[i] += 1
            else:
                checklist[i] = 1
        
        for i in t:
            if i in checklist:
                if checklist[i] == 0:
                    return False
                else:
                    checklist[i] -= 1
            else:
                return False
        
        return True