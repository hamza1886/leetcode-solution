# see: https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        is_negative = False
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        if x < 0:
            is_negative = True
            x = -x

        while x > 0:
            remainder = x % 10
            x //= 10

            if reverse > INT_MAX / 10 or (reverse == INT_MAX / 10 and remainder > 7):
                return 0
            if reverse < INT_MIN / 10 or (reverse == INT_MIN / 10 and remainder < -8):
                return 0

            reverse = reverse * 10 + remainder

        return reverse if not is_negative else -reverse


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(123))  # 321
    print(solution.reverse(-123))  # -321
    print(solution.reverse(120))  # 12
