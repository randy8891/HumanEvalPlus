def f(lst):
    """
    Given a list of integers, return a new list where:
    - Elements at even indices are replaced with their factorial.
    - Elements at odd indices are replaced with the sum of all elements in the input list.

    Args:
    lst (list): A list of integers.

    Returns:
    list: A transformed list as described above.
    """
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    total_sum = sum(lst)
    return [factorial(lst[i]) if i % 2 == 0 else total_sum for i in range(len(lst))]
