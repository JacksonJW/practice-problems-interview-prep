"""
Leetcode #1678 Goal Parser Interpretation

You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

Example 1:
Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".

Example 2:
Input: command = "G()()()()(al)"
Output: "Gooooal"

Example 3:
Input: command = "(al)G(al)()()G"
Output: "alGalooG"
 

Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.

Algorithm/DS used: string building and iteration

O(N) worst case time where N is the size of the input string 'command'

O(M) worst case space where M is the size of the input string 'command'

"""


class Solution:
    def interpret(self, command: str) -> str:
        result = ''
        i = 0
        while i < len(command):
            if command[i] == 'G':
                result += 'G'
                i += 1
            elif command[i] + command[i+1] == '()':
                result += 'o'
                i += 2
            else:
                result += 'al'
                i += 4
        return result


def test_solution():
    s = Solution()
    print("Expected result from input G()(al) is Goal and the Actual result is: " +
          str(s.interpret('G()(al)')))
    assert s.interpret('G()(al)') == 'Goal'
    assert s.interpret('G()()()()(al)') == 'Gooooal'
    assert s.interpret('(al)G(al)()()G') == 'alGalooG'


if __name__ == "__main__":
    test_solution()
