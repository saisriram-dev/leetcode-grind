from collections import Counter


def minWindow(s, t):
    # Edge case: if either string is empty
    if not t or not s:
        return ""

    # Count characters required from t
    need = Counter(t)

    # Count characters in the current window
    window = {}

    have = 0
    required = len(need)

    left = 0
    min_len = float("inf")
    result = (-1, -1)

    # Expand the window using right pointer
    for right in range(len(s)):
        char = s[right]

        # Add current character to the window
        window[char] = window.get(char, 0) + 1

        # Check whether this character's requirement is satisfied
        if char in need and window[char] == need[char]:
            have += 1

        # If the current window contains all required characters
        while have == required:

            # Update the minimum window
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = (left, right)

            # Remove the character at the left
            left_char = s[left]
            window[left_char] -= 1

            # Check if removing it makes the window invalid
            if (
                left_char in need
                and window[left_char] < need[left_char]
            ):
                have -= 1

            # Shrink the window
            left += 1

    # Return the smallest window
    l, r = result
    return s[l:r + 1] if min_len != float("inf") else ""
