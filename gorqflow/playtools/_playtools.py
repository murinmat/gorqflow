def update_dict(d1: dict, d2: dict) -> dict:
    """Recursively update a dictionary with another dictionary

    Args:
        d1 (dict): The dictionary to be updated
        d2 (dict): The dictionary to update d1 with

    Returns:
        dict: The updated dictionary
    """
    for k, v in d2.items():
        if isinstance(v, dict):
            d1[k] = update_dict(d1.get(k, {}), v)
        else:
            d1[k] = v
    return d1