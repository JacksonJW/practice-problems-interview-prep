# Given a string, find the length of the longest substring without
# repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


def lengthOfLongestSubstring(s: str) -> int:
    i = 0
    j = 0
    letters = set()
    result = 0
    n = len(s)
    while i < n and j < n:
        if s[j] not in letters:
            letters.add(s[j])
            j += 1
            result = max(result, j-i)
        else:
            letters.remove(s[i])
            i += 1
    return result


print("outcome: " + str(lengthOfLongestSubstring("abcabcdef")))
print("expected: " + str(3))
assert(lengthOfLongestSubstring("abcabcdef") == 3)
