def reduce_right(lst, func):
    lst = lst[::-1]
    result = lst[0]

    for value in lst:
        if value == result:
            continue
        result = func(result, value)

    return result