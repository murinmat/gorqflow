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


def print_dict(d: dict, indent: int = 2) -> None:
    """Pretty print a dictionary with indented values.

    Args:
        d (dict): The dictionary to be printed.
    """
    def _print(_d, current_indent_factor=0):
        for k, v in _d.items():
            print(' ' * current_indent_factor*indent + str(k) + ':')
            if isinstance(v, dict):
                _print(v, current_indent_factor+1)
            else:
                print(' ' * (current_indent_factor+1)*indent + str(v))
    _print(d)
