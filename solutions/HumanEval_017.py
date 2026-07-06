def parse_music(ascii_music):
    """
    Parse ASCII music notation and return a list of note durations.

    The input is a string where each note is represented by a character
    followed by its duration in beats (e.g., 'A4', 'B2', 'C1'). Notes
    without an explicit duration default to 1 beat.

    Args:
        ascii_music (str): A string of ASCII music notation.

    Returns:
        list: A list of integers representing the durations of the notes.
    """
    durations = []
    i = 0
    while i < len(ascii_music):
        if ascii_music[i].isalpha():  # Check for a note character
            i += 1
            duration = 1  # Default duration
            num_start = i
            while i < len(ascii_music) and ascii_music[i].isdigit():
                i += 1
            if num_start != i:  # If a number follows the note
                duration = int(ascii_music[num_start:i])
            durations.append(duration)
        else:
            i += 1
    return durations
