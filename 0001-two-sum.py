# see: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        nums_size = len(nums)

        complements = []

        for i in range(nums_size):
            complement = target - nums[i]

            if complement in complements:
                return [nums.index(complement), i]

            complements.append(nums[i])

        return []


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # [0, 1]
