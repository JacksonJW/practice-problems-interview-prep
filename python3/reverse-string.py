# Write a function that reverses a string.
# The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do
# this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.

# Solution is O(1) space and O(n) runtime


def reverse_string(s):
    i = 0
    j = len(s)-1

    while i < j:
        swap = s[i]
        s[i] = s[j]
        s[j] = swap
        i += 1
        j -= 1

    return s


print(reverse_string(["h", "e", "l", "l", "o"]))
