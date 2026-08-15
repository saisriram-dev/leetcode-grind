def findMaxAverage(nums, k):
    i = 0
    j = 0
    total = 0
    max_avg = []

    while j < len(nums):
        total += nums[j]

        if (j - i + 1) == k:
            max_avg.append(total/k)
            total -= nums[i]
            i += 1
        
        j += 1
    
    return max(max_avg)
