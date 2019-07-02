"""
Write a function to find the longest common prefix string 
amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        shortest = min(strs, key=len)
        
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return other[:i]
        
        return shortest
