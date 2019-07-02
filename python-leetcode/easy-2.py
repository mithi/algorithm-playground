"""
Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.
We can build up the reverse integer one digit at a time. While doing so, we can check beforehand whether or not appending another digit would cause overflow.
"""
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1;

        if x < 0:
            sign = -1
            x = -x

        x_reversed = 0

        while x != 0:
            pop = x % 10
            x = x // 10

            if x_reversed == 214_748_364:
                cond1 = sign == -1 and pop > 8
                cond2 = sign == 1 and pop > 7
                if cond1 or cond2:
                    return 0

            if x_reversed > 214_748_364:
                return 0

            x_reversed = 10 * x_reversed + pop

            if x == 0:
                break

        return sign * x_reversed
