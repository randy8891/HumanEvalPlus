def max_fill(wells, bucket_capacity):
    """
    Calculate the minimum number of bucket trips needed to empty all wells.

    Args:
        wells (list of int): A list where each element represents the amount of water in a well.
        bucket_capacity (int): The capacity of the bucket.

    Returns:
        int: The minimum number of bucket trips required.
    """
    if bucket_capacity <= 0:
        raise ValueError("Bucket capacity must be greater than zero.")
    
    trips = 0
    for water in wells:
        trips += -(-water // bucket_capacity)  # Ceiling division to calculate trips per well
    return trips
