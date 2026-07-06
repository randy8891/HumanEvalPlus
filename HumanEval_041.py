def car_race_collision(road: str) -> int:
    """
    Counts the number of collisions between cars going left ('L') and right ('R') on a road.

    Args:
    road (str): A string representing the road where 'L' indicates a car moving left,
                'R' indicates a car moving right, and 'S' indicates a stationary car.

    Returns:
    int: The total number of collisions between cars moving left and right.
    """
    collisions = 0
    right_moving = 0

    for char in road:
        if char == 'R':
            right_moving += 1
        elif char == 'L':
            collisions += right_moving
        elif char == 'S':
            collisions += right_moving
            right_moving = 0

    return collisions
