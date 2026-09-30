def generate(numRows):
    res = []

    for i in range(numRows):
        current = [1]

        if res:
            previous = res[-1]

            for j in range(len(previous) - 1):
                num = previous[j] + previous[j + 1]
                current.append(num)

            current.append(1)

        res.append(current)

    return res
