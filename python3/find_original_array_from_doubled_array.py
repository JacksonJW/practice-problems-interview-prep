"""
Leetcode #2007 Find Original Array From Doubled Array

An integer array original is transformed into a doubled array 
changed by appending twice the value of every element in 
original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a 
doubled array. If changed is not a doubled array, return an 
empty array. The elements in original may be returned in any 
order.


Example 1:
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

Example 2:
Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.

Example 3:
Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.


Constraints:
1 <= changed.length <= 105
0 <= changed[i] <= 105

Algorithm/DS used: <ALGORITHM USED/DS USED>

O(N) worst case time where N is the length of changed

O(N) worst case space where N is the length of changed

"""


import collections
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        original = []
        c = collections.Counter()
        n = 0
        for num in changed:
            c[num] += 1
            n += 1
        i = 0
        while n > 0:
            num = changed[i % len(changed)]
            if c[num] > 0:
                if num == 0 and c[num] % 2 == 0:
                    c[num] -= 2
                    n -= 2
                    original.append(num)
                    i += 1
                elif c[num * 2] > 0 and c[num / 2] > 0:
                    i += 1
                elif c[num * 2] > 0:
                    c[num] -= 1
                    c[num * 2] -= 1
                    n -= 2
                    original.append(num)
                    i += 1
                elif c[num / 2] > 0:
                    c[num] -= 1
                    c[num / 2] -= 1
                    n -= 2
                    original.append(int(num / 2))
                    i += 1
                else:
                    return []
            else:
                i += 1
        return original


def test_solution():
    s = Solution()
    print("Expected result from input [1,3,4,2,6,8] is [1,3,4] and the Actual result is: " +
          str(s.findOriginalArray([1, 3, 4, 2, 6, 8])))
    assert s.findOriginalArray([1, 3, 4, 2, 6, 8]) == [1, 3, 4]
    assert s.findOriginalArray([6, 3, 0, 1]) == []
    assert s.findOriginalArray([1]) == []


if __name__ == "__main__":
    test_solution()
