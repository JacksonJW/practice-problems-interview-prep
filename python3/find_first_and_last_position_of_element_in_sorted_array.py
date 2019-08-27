from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.binary_search(nums, 0, len(nums)-1, target)

    def binary_search(self, nums, i, j, target):
        if i > j:
            return [-1, -1]

        midpt = j + (i-j) + 1 // 2
        if nums[midpt] == target:
            start = midpt
            end = midpt
            while start > i and nums[start - 1] == target:
                start -= 1
            while end < j and nums[end + 1] == target:
                end += 1
            return [start, end]
        if target < nums[midpt]:
            return self.binary_search(nums, i, midpt - 1, target)
        else:
            return self.binary_search(nums, midpt + 1, j, target)


def main():
    s = Solution()
    print("Expected result is [3, 4] and the Actual result is: " +
          str(s.searchRange([5, 7, 7, 8, 8, 10], 8)))


if __name__ == "__main__":
    main()
