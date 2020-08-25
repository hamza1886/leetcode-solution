# see: https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = ''

        for i in range(len(s)):
            for j in range(len(s)):
                temp_s = s[i:j + 1]
                if temp_s == '':
                    continue

                rev_str = temp_s[::-1]
                if temp_s == rev_str and len(temp_s) > len(p):
                    p = temp_s

        return p


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome('a'))  # a
    print(solution.longestPalindrome('aa'))  # aa
    print(solution.longestPalindrome('cbbd'))  # bb
    print(solution.longestPalindrome('babad'))  # bab
