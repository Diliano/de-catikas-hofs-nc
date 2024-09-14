from src.reduce_right import reduce_right

def test_calls_reducer_correct_num_times():
    # Arrange
    calls = 0

    def concatenate_string(str1, str2):
        nonlocal calls
        calls += 1
        return f'{str1} {str2}'

    test_lst = ["hi", "there", "friend"]
    # Act
    reduce_right(test_lst, concatenate_string)
    # Assert
    assert calls == 2

def test_returns_correct_result_calling_reducer_from_last_item_first():
    # Arrange
    def concatenate_string(str1, str2):
        return f"{str1} {str2}"
    
    test_lst = ["students", "morning", "good"]
    expected = "good morning students"
    # Act
    result = reduce_right(test_lst, concatenate_string)
    # Assert 
    assert result == expected