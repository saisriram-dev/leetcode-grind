def dailyTemperatures(temperatures):
    counts = []

    for i in range(len(temperatures)):
        for j in range(i, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                counts.append(j - i)
                break
            else:
                if j == len(temperatures) - 1:
                    counts.append(0)

    return counts

temperatures = [30,38,30,36,35,40,28]
print(dailyTemperatures(temperatures))
