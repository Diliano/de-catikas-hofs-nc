from src.for_each import for_each

def test_returns_none():
    # Arrange
    def test_func(arg):
        pass
    test_lst = [1, 2, 3]
    expected = None
    # Act
    result = for_each(test_lst, test_func)
    # Assert
    assert result == expected
        
def test_calls_given_function_correct_number_of_times():
    # Arrange
    calls = 0

    def say_hello(arg):
        nonlocal calls
        calls += 1
        print(f"Hey there {arg}")

    test_lst = ["Cat"]
    # Act
    for_each(test_lst, say_hello)
    # Assert
    assert calls == 1

    # Arrange
    calls = 0

    def say_hello(arg):
        nonlocal calls
        calls += 1
        print(f"Hey there {arg}")

    test_lst = ["Cat", "Dog", "Fox"]
    # Act
    for_each(test_lst, say_hello)
    # Assert
    assert calls == 3

def test_calls_given_function_with_correct_arg():
    # Arrange
    args = []

    def say_hello(arg):
        args.append(arg)
        print(f"Hey there {arg}")

    test_lst = ["Cat", "Dog", "Fox"]
    # Act
    for_each(test_lst, say_hello)
    # Assert
    assert args == test_lst