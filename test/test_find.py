from src.find import find

def test_calls_predicate_once():
    # Arrange
    calls = 0

    def is_multiple_of_five(num):
        nonlocal calls
        calls += 1
        return num % 5 == 0
    
    test_nums = [1]
    # Act
    find(test_nums, is_multiple_of_five)
    # Assert
    assert calls == 1
    
def test_calls_predicate_multiple_times():
    # Arrange
    calls = 0

    def is_multiple_of_five(num):
        nonlocal calls
        calls += 1
        return num % 5 == 0
    
    test_nums = [1, 2, 3]
    # Act
    find(test_nums, is_multiple_of_five)
    # Assert
    assert calls == 3

def test_predicate_is_being_passed_arg():
    # Arrange
    args = []

    def is_multiple_of_five(num):
        args.append(num)
        return num % 5 == 0
    
    test_nums = [1]
    # Act
    find(test_nums, is_multiple_of_five)
    # Assert
    assert args == test_nums

def test_returns_first_element_that_satisfies_predicate():
    # Arrange
    def is_multiple_of_five(num):
        return num % 5 == 0
    
    test_nums = [2, 8, 15, 34, 40]
    expected = 15
    # Act
    result = find(test_nums, is_multiple_of_five)
    # Assert
    assert result == expected

def test_returns_message_if_predicate_not_satisfied():
    # Arrange
    def is_multiple_of_five(num):
        return num % 5 == 0
    
    test_nums = [2, 8, 16, 34, 42]
    expected = "No element satisfies the predicate function"
    # Act
    result = find(test_nums, is_multiple_of_five)
    # Assert
    assert result == expected