def fib(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    memo = [0, 1]
    i = 2
    while i <= n:
        memo.append(memo[i-2] + memo[i-1])
        i += 1
    return memo[-1]


assert fib(7) == 13
print('fib(7) should yield an expected result of 13, the actual result is: ' + str(fib(7)))
