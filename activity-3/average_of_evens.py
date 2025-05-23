def average_of_evens(arr):
    total = 0  # L1 d1: total
    count = 0  # L2 d2: count
    for num in arr:  # L3 p-use: arr | loop var: num
        if num % 2 == 0:  # L4 p-use: num
            total += num  # L5 c-use: total,num | d3: total updated
            count += 1  # L6 c-use: count | d4: count updated
    if count == 0:  # L7 p-use: count
        return 0
    return total / count  # L9 c-use: total, count
