def parse(user_input):
    """Extract the values split by a comma in a string
    and return the two values via a dictionary.
    """
    # Get the two values in a list
    parts = user_input.split(" ")

    # Store the two values in variables
    feet = int(parts[0])
    inches = int(parts[1])

    # Inject the values in a dictionary
    return {"feet": feet, "inches": inches}


