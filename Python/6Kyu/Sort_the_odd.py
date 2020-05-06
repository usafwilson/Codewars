def sort_array(source_array):
    odds = []
    return_array = []
    for e in source_array:
        if e % 2 != 0:
            odds.append(e)

    sorted_odds = sorted(odds)
    indx = 0
    for n in source_array:
        if n % 2 != 0:
            return_array.append(sorted_odds[indx])
            indx += 1
        else:
            return_array.append(n)
    return return_array
