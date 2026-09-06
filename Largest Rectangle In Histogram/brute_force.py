def largestRectangleArea(heights):
    n = len(heights)
    area = 0

    for i in range(n):
        left = right = i

        while left > 0 and heights[left - 1] >= heights[i]:
            left -= 1
        
        while right < n - 1 and heights[i] <= heights[right + 1]:
            right += 1

        area = max(area, (right - left + 1) * heights[i])

    return area
