def trap(height):
    max_left = height[0]
    max_right = height[-1]
    area = 0

    left_max = [0] * len(height)
    right_max = [0] * len(height)

    for i in range(len(height)):
        if height[i] >= max_left:
            max_left = height[i]
        left_max[i] = max_left

    for i in range(len(height) - 1, -1, -1):
        if height[i] >= max_right:
            max_right = height[i]
        right_max[i] = max_right

    for i in range(len(height)):
        area += min(left_max[i], right_max[i]) - height[i]

    return area
