def findDuplicate(nums):
    # Phase 1: Find a meeting point inside the cycle
    slow = 0
    fast = 0

    while True:
        slow = nums[slow]              # move 1 step
        fast = nums[nums[fast]]        # move 2 steps

        if slow == fast:
            break

    # Phase 2: Find the entrance of the cycle
    slow = 0

    while slow != fast:
        slow = nums[slow]              # move 1 step
        fast = nums[fast]              # move 1 step

    return slow
