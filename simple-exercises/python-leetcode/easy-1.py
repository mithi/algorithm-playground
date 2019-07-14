"""
specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

SOLUTION 1: BRUTE FORCE
SOLUTION 2: Two-pass Hash Table
SOLUTION 3: One-pass Hash Table
"""

class Solution1:
    # BRUTE FORCE
    # time complexity = n^2
    # space complexity = 1
    # Test each pair
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # should not happen
        return [-1, -1]


class Solution2:
    # TWO PASS HASHTABLE
    # time complexity: n
    # space complexity: n
    # first pass -> map: key = target - nums[i], value: i
    # 2nd pass -> for all i's
    # check if key = target - nums[i] exists in hash table
    # if value is not equal to i return [i, value]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            c = target - nums[i]
            table[c] = i

        for j in range(len(nums)):
            if nums[j] in table:
                if j != table[nums[j]]:
                    return [j, table[nums[j]]]

        # should not happen
        return [-1, -1]


class Solution3:
    # One pass hash table
    # time complexity - n
    # space complexity - n
    # While you are making a hash table, check if
    # the complement is already in the table
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        table[target - nums[0]] = 0

        for i in range(1, len(nums)):
            if nums[i] in table:
                return [table[nums[i]], i]
            table[target - nums[i]] = i

        # should not happen
        return [-1, 1]

