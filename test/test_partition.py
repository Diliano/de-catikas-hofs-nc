from src.partition import partition

def test_only_accepts_lists_sets_tuples():
    # Assert
    def test_func(arg):
        pass
    test_collection = 2
    expected = "This function only accepts lists, sets or tuples"
    # Act
    result = partition(test_collection, test_func)
    # Assert
    assert result == expected

def test_returns_empty_nested_list_given_empty_input():
    # Assert
    def test_func(arg):
        pass
    test_collection = []
    expected = [[], []]
    # Act
    result = partition(test_collection, test_func)
    # Assert
    assert result == expected

def test_calls_function_correct_num_times():
    # Assert
    calls = 0

    def test_func(arg):
        nonlocal calls
        calls += 1
        pass

    test_collection = [1, 2, 3]
    # Act
    partition(test_collection, test_func)
    # Assert
    assert calls == 3

def test_calls_function_with_correct_arg():
    # Assert
    args = []

    def test_func(arg):
        args.append(arg)
        pass

    test_collection = [1, 2, 3]
    # Act
    partition(test_collection, test_func)
    # Assert
    assert args == test_collection

def test_populates_list_of_true_evaluations():
    # Arrange
    def is_even(num):
        return num % 2 == 0
    
    test_collection = [2, 4]
    expected = [[2, 4], []]
    # Act
    result = partition(test_collection, is_even)
    # Assert
    assert result == expected

def test_populates_list_of_false_evaluations():
    # Arrange
    def is_even(num):
        return num % 2 == 0
    
    test_collection = [1, 3]
    expected = [[], [1, 3]]
    # Act
    result = partition(test_collection, is_even)
    # Assert
    assert result == expected

def test_handles_true_and_false_evaluations():
    # Arrange
    def is_even(num):
        return num % 2 == 0
    
    test_collection = [1, 2, 3, 4, 5]
    expected = [[2, 4], [1, 3, 5]]
    # Act
    result = partition(test_collection, is_even)
    # Assert
    assert result == expected

def test_returns_correct_list_given_set_input():
    # Arrange
    def is_even(num):
        return num % 2 == 0
    
    test_collection = {7, 22, 94, 111, 2, 99, 46, 73}
    expected = [[22, 94, 2, 46], [7, 111, 99, 73]]
    # Act
    result = partition(test_collection, is_even)
    # Assert
    assert sorted(result[0]) == sorted(expected[0])
    assert sorted(result[1]) == sorted(expected[1])

def test_returns_correct_list_given_tuple_input():
    # Arrange
    def is_even(num):
        return num % 2 == 0
    
    test_collection = (1, 2, 3, 4, 5)
    expected = [[2, 4], [1, 3, 5]]
    # Act
    result = partition(test_collection, is_even)
    # Assert
    assert result == expected