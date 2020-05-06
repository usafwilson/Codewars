def persistence(n):
    str_n = str(n)
    cnt = 0
    while len(str_n) > 1:
        total = 1
        for d in str_n:
            total *= int(d)
        cnt += 1
        str_n = str(total)
    return cnt

