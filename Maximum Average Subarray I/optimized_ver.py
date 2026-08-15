def findMaxAverage(nums, k):
    i = 0
    total = sum(nums[:k])
    max_avg = total / k

    for j in range(k, len(nums)):
        total += nums[j] - nums[i]
        max_avg = max(max_avg, total / k)
        i += 1

    return max_avg