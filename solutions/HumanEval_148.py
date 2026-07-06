def bf(planet1, planet2):
    """
    Returns a list of planets in order from the sun that are located between two given planets.
    
    Parameters:
    planet1 (str): The name of the first planet.
    planet2 (str): The name of the second planet.
    
    Returns:
    list: A list of planet names between the two given planets in order from the sun.
    """
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    try:
        index1 = planets.index(planet1)
        index2 = planets.index(planet2)
        if index1 < index2:
            return planets[index1 + 1:index2]
        else:
            return planets[index2 + 1:index1]
    except ValueError:
        return []
