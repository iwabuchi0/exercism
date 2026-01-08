EXPECTED_BAKE_TIME = 40

def bake_time_remaining(minutes_in_the_oven):
    """Calculate the remain bake time.

    Args: 
        minutes_in_the_oven (int): the number of minutes the lasagna has already baked.

    Returns: 
        int: the number of minutes baking based on the EXPECTD_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - minutes_in_the_oven
print(bake_time_remaining(30))

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time bassed on number of layers.

    Args: 
        number_of_layers(int): the number of layers to prepare.
        
    Returns:
        int: Total preparation time, assuming each layer takes 2 minutes.
    """
    return number_of_layers * 2
print(preparation_time_in_minutes(2))

def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Calculatee the total elapsed cooking time.
    Args:
        number_of_layers (int): the number of layers prepared.
        elapsed_bake_time (int): the time that lasagna has been baked.
    Returns: 
        int: Total elapsed time, including preparation and baking.
    """
    return (2* number_of_layers) + elapsed_bake_time
print(elapsed_time_in_minutes(3,20))
    