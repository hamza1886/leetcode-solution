# see: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicts = {}
        maxlength = start = 0

        for i, value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums

            num = i - start + 1

            if num > maxlength:
                maxlength = num

            dicts[value] = i

        return maxlength


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abcabcbb'))  # 3
    print(solution.lengthOfLongestSubstring('bbbbb'))  # 1
    print(solution.lengthOfLongestSubstring('pwwkew'))  # 3
