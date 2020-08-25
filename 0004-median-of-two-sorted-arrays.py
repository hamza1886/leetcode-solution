# see: https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        i = j = 0
        nums1_size = len(nums1)
        nums2_size = len(nums2)
        nums3 = []

        while i < nums1_size and j < nums2_size:
            if (nums1[i] < nums2[j]):
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1

        if i != nums1_size:
            nums3 += nums1[i:]
        if j != nums2_size:
            nums3 += nums2[j:]

        nums3_size = len(nums3)

        if nums3_size % 2 == 0:
            mid = int(nums3_size / 2)
            return (nums3[mid - 1] + nums3[mid]) / 2
        else:
            mid = int((nums3_size - 1) / 2)
            return nums3[mid] / 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 3], [2]))  # 2.0
    print(solution.findMedianSortedArrays([1, 2], [3, 4]))  # 2.5
    print(solution.findMedianSortedArrays([0, 0], [0, 0]))  # 0.0
