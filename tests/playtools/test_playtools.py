from gorqflow.playtools import update_dict


def test_update_dict_non_recursive():
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 4}
    expected = {'a': 1, 'b': 3, 'c': 4}
    assert update_dict(d1, d2) == expected


def test_update_dict_recursive():
    d1 = {'a': 1, 'b': {'c': 2, 'd': 3}}
    d2 = {'b': {'c': 3, 'e': 5}}
    expected = {'a': 1, 'b': {'c': 3, 'd': 3, 'e': 5}}
    assert update_dict(d1, d2) == expected