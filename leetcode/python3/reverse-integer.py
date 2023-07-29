# Given a 32-bit signed integer, reverse digits of an integer.

# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 0 when the reversed integer
# overflows.

def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """

    if str(x)[0] == '-':
        result = int("-" + str(x)[:0:-1])
    elif str(x)[:-1] == '0':
        result = int(str(x)[:0:-1])
    else:
        result = int(str(x)[::-1])

    if result >= 2**31 or result < -2**31:
        return 0
    return result
