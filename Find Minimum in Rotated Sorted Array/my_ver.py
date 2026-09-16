def findMin(nums):
    i = 0
    j = len(nums) - 1

    if len(nums) == 1:
        return nums[0]

    if nums[i] < nums[j]:
        return nums[i]
    
    while nums[i] > nums[j]:
        j -= 1

    return nums[j + 1]
