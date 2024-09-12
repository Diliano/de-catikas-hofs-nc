def manual_filter(func, collection):
    accepted_types = {list, set, tuple}
    if type(collection) not in accepted_types:
        return "This function only accepts lists, sets or tuples"
    
    return type(collection)([value for value in collection if func(value)])