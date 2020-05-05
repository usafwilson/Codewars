def high_and_low(numbers):
    num_list = [int(x) for x in numbers.split(' ')]
    max_n = str(max(num_list))
    min_n = str(min(num_list))

    return max_n + ' ' + min_n
