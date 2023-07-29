"""
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_counts = {}

        for s_letter in s:
            if s_letter in letter_counts:
                letter_counts[s_letter] += 1
            else:
                letter_counts[s_letter] = 1

        for t_letter in t:
            if t_letter in letter_counts:
                if letter_counts[t_letter] == 1:
                    del letter_counts[t_letter]
                else:
                    letter_counts[t_letter] -= 1

        return len(letter_counts) == 0


def main():
    s = Solution()
    print("Expected result is False and the Actual result is: " +
          str(s.isAnagram("rat", "car")))


if __name__ == "__main__":
    main()
