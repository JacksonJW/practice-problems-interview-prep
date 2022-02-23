"""
Leetcode #1592 Rearrange Spaces Between Words

You are given a string text of words that are placed 
among some number of spaces. Each word consists of one 
or more lowercase English letters and are separated by 
at least one space. It's guaranteed that text contains 
at least one word.

Rearrange the spaces so that there is an equal number 
of spaces between every pair of adjacent words and that 
number is maximized. If you cannot redistribute all the 
spaces equally, place the extra spaces at the end, meaning 
the returned string should be the same length as text.

Return the string after rearranging the spaces.


Example 1:
Input: text = "  this   is  a sentence "
Output: "this   is   a   sentence"
Explanation: There are a total of 9 spaces and 4 words. 
We can evenly divide the 9 spaces between the words: 
9 / (4-1) = 3 spaces.

Example 2:
Input: text = " practice   makes   perfect"
Output: "practice   makes   perfect "
Explanation: There are a total of 7 spaces and 3 words. 
7 / (3-1) = 3 spaces plus 1 extra space. We place this 
extra space at the end of the string.

Constraints:
1 <= text.length <= 100
text consists of lowercase English letters and ' '.
text contains at least one word.

Algorithm/DS used: Split words and reconstruct string based on words and spaces

O(N) worst case time where N is the length of text

O(N) worst case space where N is length of text

"""


class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        result = ''
        space_count = 0
        for i in range(len(text)):
            if text[i] == ' ':
                space_count += 1
        if len(words) > 1:
            num_spaces = space_count // (len(words) - 1)
        if len(words) > 1:
            extra_spaces = space_count % (len(words)-1)
        else:
            extra_spaces = space_count
        for i in range(len(words)):
            result += words[i]
            if i == len(words) - 1:
                for j in range(extra_spaces):
                    result += ' '
            else:
                for j in range(num_spaces):
                    result += ' '
        return result


def test_solution():
    s = Solution()
    print("Expected result from input \"  this   is  a sentence \" is \"this  is   a   sentence\" and the Actual result is: " +
          str(s.reorderSpaces("  this   is  a sentence ")))
    assert s.reorderSpaces(
        "  this   is  a sentence ") == "this   is   a   sentence"
    assert s.reorderSpaces(
        " practice   makes   perfect") == "practice   makes   perfect "


if __name__ == "__main__":
    test_solution()
