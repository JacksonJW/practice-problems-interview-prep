"""
Leetcode #1704 Determine if String Halves Are Alike

You are given a string s of even length. Split this string into
two halves of equal lengths, and let a be the first half and b 
be the second half.

Two strings are alike if they have the same number of vowels 
('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that 
s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

Example 1:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 
vowel. Therefore, they are alike.

Example 2:
Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b 
has 2. Therefore, they are not alike.

Notice that the vowel o is counted twice.

Example 3:
Input: s = "MerryChristmas"
Output: false

Example 4:
Input: s = "AbCdEfGh"
Output: true

Constraints:
2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.

Algorithm/DS used: iteration through list to check if in hash set

O(N) worst case time where N is the length of the string input s

O(1) worst case space

"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        left = 0
        right = 0
        vowels = set('aeiou')
        for c in s[:len(s)//2]:
            if c.lower() in vowels:
                left += 1
        for c in s[:len(s)//2-1:-1]:
            if c.lower() in vowels:
                right += 1
        return left == right


def test_solution():
    s = Solution()
    print("Expected result from input s = \"book\" is True and the Actual result is: " +
          str(s.halvesAreAlike('book')))
    assert s.halvesAreAlike('book') == True
    assert s.halvesAreAlike('textbook') == False
    assert s.halvesAreAlike('MerryChristmas') == False
    assert s.halvesAreAlike('AbCdEfGh') == True


if __name__ == "__main__":
    test_solution()
