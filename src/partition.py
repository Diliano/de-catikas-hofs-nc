def partition(collection, func):
    accepted_types = {list, set, tuple}
    if type(collection) not in accepted_types:
        return "This function only accepts lists, sets or tuples"
    
    result = [[], []]

    for value in collection:
        if func(value):
            result[0].append(value)
        else:
            result[1].append(value)
    
    return result