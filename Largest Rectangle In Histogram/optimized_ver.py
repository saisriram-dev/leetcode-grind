def largestRectangleArea(heights: list[int]) -> int:
    # Append a 0 at the end to flush out any remaining bars in the stack
    heights.append(0)
    stack = []
    max_area = 0
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            # Width is determined by the distance between the current index (i) 
            # and the new top of the stack (or 0 if the stack is empty)
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
        
    heights.pop()  # Clean up the extra 0
    return max_area