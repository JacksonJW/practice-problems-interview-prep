def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    running_lookup = {}
    row = 0
    result_str = ""
    row_num = 0
    inc = True
    while row < numRows:
        running_lookup[row] = ""
        row = row+1

    for i in range(len(s)):
        if row_num == numRows-1:
            inc = False
        elif row_num == 0:
            inc = True
        running_lookup[row_num] = running_lookup[row_num] + s[i]
        if inc == True:
            row_num = row_num + 1
        else:
            row_num = row_num - 1

    for value in running_lookup.values():
        result_str = result_str + value

    return result_str


print("The function \"convert\" with input \"AB\" and rowNums of \"1\" returns: " + convert("AB", 1))
