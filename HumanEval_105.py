def by_length():
    """
    Sorts integers from 1 to 9 in reverse order and returns their names spelled out.
    
    Returns:
        list: A list of strings representing the names of the integers in reverse order.
    """
    num_to_word = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
                   6: "six", 7: "seven", 8: "eight", 9: "nine"}
    return [num_to_word[num] for num in sorted(num_to_word.keys(), reverse=True)]
