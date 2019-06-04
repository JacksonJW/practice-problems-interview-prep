# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from
# 1 to 3999.


def romanToInt(s) -> int:
    roman_lookup = {"I": 1, "V": 5, "X": 10,
                    "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    i = 0
    while i < len(s):
        if i == len(s)-1:
            sum += roman_lookup[s[i]]
            i += 1
        elif roman_lookup[s[i]] < roman_lookup[s[i+1]]:
            sum += roman_lookup[s[i+1]] - roman_lookup[s[i]]
            i += 2
        else:
            sum += roman_lookup[s[i]]
            i += 1
    return sum


print(romanToInt("XLIV"))
