def reject(collection, func):
    accepted_types = {list, set, tuple}
    if type(collection) not in accepted_types:
        return "This function only accepts lists, sets or tuples"
    
    return [value for value in collection if not func(value)]