def generate(num_rows):
    return make_row([], None, num_rows)


def make_row(triangle_list, last_row, n):
    if len(triangle_list) == n:
        return triangle_list

    if last_row is None:
        triangle_list.append([1])
        return make_row(triangle_list, [1], n)
    elif last_row == [1]:
        triangle_list.append([1, 1])
        return make_row(triangle_list, [1, 1], n)
    else:
        new_row = []
        new_row.append(1)
        i = 0
        while i < len(last_row)-1:
            new_row.append(last_row[i] + last_row[i+1])
            i += 1
        new_row.append(1)
        triangle_list.append(new_row)
        return make_row(triangle_list, new_row, n)


print("result: "+str(generate(5)))
assert generate(5) == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
