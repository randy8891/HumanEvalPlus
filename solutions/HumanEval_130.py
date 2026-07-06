def tri(n):
    """
    Compute the first n elements of the Tribonacci sequence.
    
    The Tribonacci sequence is a generalization of the Fibonacci sequence where each term is 
    the sum of the three preceding ones, starting with 0, 1, 1.
    
    Parameters:
        n (int): The number of elements to compute in the sequence.
        
    Returns:
        list: A list containing the first n elements of the Tribonacci sequence.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    if n == 3:
        return [0, 1, 1]
    
    tribonacci = [0, 1, 1]
    for i in range(3, n):
        tribonacci.append(tribonacci[-1] + tribonacci[-2] + tribonacci[-3])
    return tribonacci
