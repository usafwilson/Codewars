def high_and_low(numbers):
    num_list = [int(x) for x in numbers.split(' ')]
    return str(max(num_list)) + ' ' + str(min(num_list))
