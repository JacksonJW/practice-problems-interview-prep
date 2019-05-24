# Given n non-negative integers a1, a2, ..., an, where each represents a
# point at coordinate(i, ai). n vertical lines are drawn such that the
# two endpoints of line i is at(i, ai) and (i, 0). Find two lines, which
# together with x-axis forms a container, such that the container contains
# the most water.

# Note: You may not slant the container and n is at least 2.


def maxArea(height) -> int:
    max_area = 0
    i = 0
    j = len(height)-1
    while i != j:
        print('height[i]: is ' + str(height[i]))
        print('height[j]: is ' + str(height[j]))
        min_height = min(height[i], height[j])
        print('min_height is: ' + str(min_height))
        max_area = max(max_area, min_height*(j-i))
        print("max_area is: "+str(max_area))
        if min_height == height[i]:
            i += 1
        else:
            j -= 1
    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
