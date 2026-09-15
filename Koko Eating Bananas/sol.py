import math


def minEatingSpeed(piles, h):
    left = 1
    right = max(piles)
    ans = right

    while left <= right:
        mid = (left + right) // 2

        # Calculate total hours needed at speed 'mid'
        hours_needed = 0
        for pile in piles:
            hours_needed += math.ceil(pile / mid)

        if hours_needed <= h:
            ans = mid       # Speed is sufficient, try to find a smaller speed
            right = mid - 1
        else:
            left = mid + 1  # Speed is too slow, increase speed

    return ans
