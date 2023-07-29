"""
Leetcode #1732 Find the Highest Altitude

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
 

Constraints:
n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100


Algorithm/DS used: looping and tabulation/dynamic programming

O(N) worst case time where N is the length of the gain list

O(M) worst case space where M is the length of the altitudes

"""


from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for each_gain in gain:
            altitudes.append(altitudes[-1] + each_gain)
        return max(altitudes)


def test_solution():
    s = Solution()
    print("Expected result from input <{INPUT_ARG(S)}> is <EXPECTED_RESULT> and the Actual result is: " + str(
        s.largestAltitude([-5, 1, 5, 0, -7])))
    assert s.largestAltitude([-5, 1, 5, 0, -7]) == 1
    assert s.largestAltitude([-4, -3, -2, -1, 4, 3, 2]) == 1


if __name__ == "__main__":
    test_solution()
