def totalFruit(fruits):
    i = 0
    max_length = 0
    fruit_counts = {} # Tracks {fruit_type: count_in_window}

    for j in range(len(fruits)):
        fruit_counts[fruits[j]] = fruit_counts.get(fruits[j], 0) + 1

        while len(fruit_counts) > 2:
            fruit_counts[fruits[i]] -= 1

            if fruit_counts[fruits[i]] == 0:
                del fruit_counts[fruits[i]]

            i += 1

        max_length = max(max_length, j - i + 1)

    return max_length
