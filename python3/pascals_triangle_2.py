"""
119. Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

1
1, 1
1, 2, 1
1, 3, 3, 1
1, 4, 6, 4, 1


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]

Follow up:
Could you optimize your algorithm to use only O(k) extra space?

O(n) time where n is the number of rows
O(n) space where n is the number of rows which correponds to the length of one row

<AVERAGE SPACE COMPLEXITY> space
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        result = [1, 1]
        for i in range(1, rowIndex):
            current_row = []
            current_row.append(1)
            for j in range(len(result)-1):
                current_row.append(result[j] + result[j+1])
            current_row.append(1)
            result = current_row
        return result


def main():
    s = Solution()
    print("Expected result is [1, 4, 6, 4, 1] and the Actual result is: " +
          str(s.getRow(4)))


if __name__ == "__main__":
    main()
