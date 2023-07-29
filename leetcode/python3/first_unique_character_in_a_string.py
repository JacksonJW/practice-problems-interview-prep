def firstUniqChar(s):
    hash_table_of_unique = {}
    for char in s:
        if char not in hash_table_of_unique:
            hash_table_of_unique[char] = 1
        else:
            hash_table_of_unique[char] += 1

    for i in range(len(s)):
        if hash_table_of_unique[s[i]] == 1:
            return i

    return -1


print(firstUniqChar("leetcode"))
assert firstUniqChar("leetcode") == 0
