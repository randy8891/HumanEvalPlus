def get_max_triples(arr):
    """
    Counts the number of triples (i, j, k) in the array such that i < j < k 
    and the sum of arr[i], arr[j], and arr[k] is divisible by 3.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The count of such triples.
    """
    n = len(arr)
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (arr[i] + arr[j] + arr[k]) % 3 == 0:
                    count += 1
    return count
