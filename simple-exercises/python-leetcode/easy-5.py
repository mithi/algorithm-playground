"""
Roman to Integer

Roman numerals are represented by seven different symbols:
I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
"""

class Solution1:
    def romanToInt(self, s: str) -> int:

        if s == "": return 0

        table = {
            'I': [1, "XV"],
            'V': [5, ""],
            'X': [10, "LC"],
            'L': [50, ""],
            'C': [100, "DM"],
            'D': [500, ""],
            'M': [1000, ""],
        }

        x = 0
        i = 0
        while i < len(s):
            n, checkset = table[s[i]]

            if i + 1 < len(s) and s[i + 1] in checkset:
                m, _ = table[s[i + 1]]
                x += (m - n)
                i += 2
            else:
                x += n
                i += 1

        return x


class Solution2:
    def romanToInt(self, s: str) -> int:

        if s == "": return 0

        table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        x = 0
        i = 0
        while i < len(s):
            n = table[s[i]]

            if i + 1 < len(s) and table[s[i + 1]] > n:
                m = table[s[i + 1]]
                x += (m - n)
                i += 2
            else:
                x += n
                i += 1

        return x
