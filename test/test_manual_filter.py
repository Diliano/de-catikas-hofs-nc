from src.manual_filter import manual_filter

# return same data type as passed in
# handles empty imput

def test_only_accepts_specified_data_types():
    # Arrange
    def test_func():
        pass
    test_collection = 1
    expected = "This function only accepts lists, sets or tuples"
    # Act
    result = manual_filter(test_func, test_collection)
    # Assert
    assert result == expected

def test_calls_given_function_correct_number_of_times():
    # Arrange
    calls = 0

    def test_func(arg):
        nonlocal calls
        calls += 1
        pass

    test_collection = [1, 2, 3]
    # Act
    manual_filter(test_func, test_collection)
    # Assert
    assert calls == 3

def test_calls_given_function_with_correct_arg():
    # Arrange
    args = []

    def test_func(arg):
        args.append(arg)
        pass

    test_collection = [1, 2, 3]
    # Act
    manual_filter(test_func, test_collection)
    # Assert
    assert args == test_collection

def test_filters_correctly():
    # Arrange
    def fun(variable):
        letters = ["a", "e", "i", "o", "u"]
        if (variable in letters):
            return True
        else:
            return False
        
    test_collection = ["g", "e", "e", "j", "k", "s", "p", "r"]
    expected = ["e", "e"]
    # Act
    result = manual_filter(fun, test_collection)
    # Assert
    assert result == expected

def test_returns_tuple_given_tuple_input():
    # Arrange
    def is_multiple_of_3(num):
        return num % 3 == 0
        
    test_collection = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    expected = (3, 6, 9)
    # Act
    result = manual_filter(is_multiple_of_3, test_collection)
    # Assert
    assert result == expected

def test_returns_set_given_set_input():
    # Arrange
    def fun(variable):
        letters = ["a", "e", "i", "o", "u"]
        if (variable in letters):
            return True
        else:
            return False
        
    test_collection = {"g", "e", "j", "k", "s", "p", "r", "a"}
    expected = {"e", "a"}
    # Act
    result = manual_filter(fun, test_collection)
    # Assert
    assert result == expected

def test_handles_empty_input_collection():
    def is_multiple_of_3(num):
        return num % 3 == 0
    
    assert manual_filter(is_multiple_of_3, []) == []
    assert manual_filter(is_multiple_of_3, ()) == ()
    assert manual_filter(is_multiple_of_3, set()) == set()