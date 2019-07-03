"""
Write a function to find the longest common prefix string 
amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
    
class Solution1:
    # worst case: minimum_length * number_of_words = m * n
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        shortest = min(strs, key=len) # O(n)
        
        for i, ch in enumerate(shortest): # O(m*n)
            for other in strs:
                if other[i] != ch:
                    return other[:i]
        
        return shortest

class Solution:
    # worst case: m * n or n log n
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        
        words = sorted(strs) # n log n, sorts alphabetically
                    
        for i, (a, b) in enumerate(zip(words[0], words[-1])):
            if a != b:
                return words[0][:i]
                
        return words[0]
