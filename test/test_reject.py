from src.reject import reject

def test_only_accepts_lists_sets_tuples():
    # Arrange
    def is_even(num):
        return num % 2 == 0
    test_collection = 2
    expected = "This function only accepts lists, sets or tuples"
    # Act
    result = reject(test_collection, is_even)
    # Assert
    assert result == expected

def test_calls_given_func_correct_num_of_times():
    # Arrange
    calls = 0

    def is_even(num):
        nonlocal calls
        calls += 1
        return num % 2 == 0
    
    test_collection = [1, 2]
    expected = "This function only accepts lists, sets or tuples"
    # Act
    reject(test_collection, is_even)
    # Assert
    assert calls == 2

def test_calls_given_func_with_correct_arg():
    # Arrange
    args = []

    def is_even(num):
        args.append(num)
        return num % 2 == 0
    
    test_collection = [1, 2]
    # Act
    reject(test_collection, is_even)
    # Assert
    assert args == test_collection

def test_returns_list_of_elements_that_given_func_returns_false_for():
    # Arrange
    def is_even(num):
        return num % 2 == 0
    
    test_collection = [1, 2, 3]
    expected = [1, 3]
    # Act
    result = reject(test_collection, is_even)
    # Assert
    assert result == expected

def test_returns_empty_list_given_no_false_returns_from_func():
    # Arrange
    def is_even(num):
        return num % 2 == 0
    
    test_collection = [2, 4, 6]
    expected = []
    # Act
    result = reject(test_collection, is_even)
    # Assert
    assert result == expected

def test_returns_empty_list_given_empty_collection():
    # Arrange
    def is_even(num):
        return num % 2 == 0
    
    test_collection = []
    expected = []
    # Act
    result = reject(test_collection, is_even)
    # Assert
    assert result == expected

def test_returns_list_regardless_of_input_type():
     # Arrange
    def is_even(num):
        return num % 2 == 0
    
    test_collection = {1, 2, 3}
    expected = [1, 3]
    # Act
    result = reject(test_collection, is_even)
    # Assert
    assert result == expected

    # Arrange
    def is_even(num):
        return num % 2 == 0
    
    test_collection = (1, 2, 3)
    expected = [1, 3]
    # Act
    result = reject(test_collection, is_even)
    # Assert
    assert result == expected