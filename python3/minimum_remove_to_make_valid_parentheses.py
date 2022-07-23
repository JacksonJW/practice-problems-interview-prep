"""
Leetcode #1249 Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses 
( '(' or ')', in any positions ) so that the resulting 
parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B
are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Constraints:
1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.

Algorithm(s)/DS used: Hash set and stack. Multiple iterations over string

O(N) worst case time where N is the length of s

O(N) worst case space where N is the length of s

"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result, stack, delete_set = '', [], set()
        for i, e in enumerate(s):
            if e == '(':
                stack.append((i, e))
            elif e == ')' and not stack:
                delete_set.add(i)
            elif e == ')' and stack:
                stack.pop()

        for i, _ in stack:
            delete_set.add(i)
        for i, e in enumerate(s):
            if i not in delete_set:
                result += e
        return result


def test_solution():
    s = Solution()
    print("Expected result from input 'lee(t(c)o)de)' is 'lee(t(c)o)de' and the Actual result is: " +
          str(s.minRemoveToMakeValid('lee(t(c)o)de)')))
    assert s.minRemoveToMakeValid('lee(t(c)o)de)') == 'lee(t(c)o)de'
    assert s.minRemoveToMakeValid('a)b(c)d') == 'ab(c)d'
    assert s.minRemoveToMakeValid('))((') == ''


if __name__ == "__main__":
    test_solution()
