def num_islands(grid):
    number_of_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                number_of_islands += 1
                part_of_island(grid, i, j)
    return number_of_islands


def part_of_island(grid, i, j):
    if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == '0':
        return
    else:
        grid[i][j] = '0'
        part_of_island(grid, i+1, j)
        part_of_island(grid, i, j+1)
        part_of_island(grid, i-1, j)
        part_of_island(grid, i, j-1)


g = [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'],
     ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
print("The expected result for the values is 3 and the actual result is: " +
      str(num_islands(g)))
