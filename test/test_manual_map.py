from src.manual_map import manual_map

def test_returns_prompt_if_given_wrong_data_type():
    # Arrange
    def test_func():
        pass
    test_input = 1
    expected = "This function only accepts lists, sets or tuples"
    # Act
    result = manual_map(test_func, test_input) 
    # Assert
    assert result == expected

def test_invokes_given_function():
    # Arrange
    calls = 0

    def double(num):
        nonlocal calls
        calls += 1
        return num + num
    
    test_input = [1, 2, 3]
    # Act
    manual_map(double, test_input)
    # Assert
    assert calls == 3

def test_invokes_given_function_with_correct_arg():
    # Arrange
    args = []

    def double(num):
        args.append(num)
        return num + num
    
    test_input = [1, 2, 3]
    # Act
    manual_map(double, test_input)
    # Assert
    assert args == test_input

def test_returns_correct_result():
    # Arrange
    def double(num):
        return num + num
    
    test_input = [1, 2, 3]
    expected = [2, 4, 6]
    # Act 
    result = manual_map(double, test_input)
    # Assert
    assert result == expected

def test_returns_tuple_given_tuple_input():
    # Arrange
    def double(num):
        return num + num
    
    test_input = (1, 2, 3)
    expected = (2, 4, 6)
    # Act 
    result = manual_map(double, test_input)
    # Assert
    assert result == expected

def test_returns_set_given_set_input():
    # Arrange
    def double(num):
        return num + num
    
    test_input = {1, 2, 3}
    expected = {2, 4, 6}
    # Act 
    result = manual_map(double, test_input)
    # Assert
    assert result == expected

def test_handles_empty_input():
    def test_func():
        pass
    assert manual_map(test_func, []) == []
    assert manual_map(test_func, ()) == ()
    assert manual_map(test_func, set()) == set()