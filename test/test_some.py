from src.some import some

def test_calls_predicate_once():
    # Arrange
    calls = 0

    def is_even(num):
        nonlocal calls
        calls += 1
        return num % 2 == 0
    
    test_nums = [1]
    # Act
    some(test_nums, is_even)
    # Assert
    assert calls == 1

def test_calls_predicate_multiple_times():
    # Arrange
    calls = 0

    def is_even(num):
        nonlocal calls
        calls += 1
        return num % 2 == 0
    
    test_nums = [1, 3, 5]
    # Act
    some(test_nums, is_even)
    # Assert
    assert calls == 3

def test_predicate_is_being_passed_the_arg():
    # Arrange
    args = []

    def is_even(num):
        args.append(num)
        return num % 2 == 0
    
    test_nums = [1]
    # Act
    some(test_nums, is_even)
    # Assert
    assert args == test_nums

def test_returns_true_if_predicate_returns_true_once():
    # Arrange
    def is_even(num):
        return num % 2 == 0
    
    test_nums = [1, 2, 3]
    expected = True
    # Act
    result = some(test_nums, is_even)
    # Assert
    assert result == expected

def test_returns_false_if_predicate_returns_false_for_all():
    # Arrange
    def is_even(num):
        return num % 2 == 0
    
    test_nums = [1, 3, 5]
    expected = False
    # Act
    result = some(test_nums, is_even)
    # Assert
    assert result == expected