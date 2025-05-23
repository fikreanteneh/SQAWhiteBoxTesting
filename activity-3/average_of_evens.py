def average_of_evens(arr):
    total = 0  # d1: total
    count = 0  # d2: count
    for num in arr:  # p-use: arr
        if num % 2 == 0:  # p-use: num
            total += num  # c-use: total, num | d3: total updated
            count += 1  # c-use: count | d4: count updated
    if count == 0:  # p-use: count
        return 0
    return total / count  # c-use: total, count
