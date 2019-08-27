from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        if len(nums1_set) > len(nums2_set):
            for nums2 in nums2_set:
                if nums2 in nums1_set:
                    result.append(nums1)
        else:
            for nums1 in nums1_set:
                if nums1 in nums2_set:
                    result.append(nums1)

        return result


def main():
    s = Solution()
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print("Expected result is [9, 4] or [4, 9] (in no particular order) and the Actual result is: " +
          str(s.intersection(nums1, nums2)))


if __name__ == "__main__":
    main()
