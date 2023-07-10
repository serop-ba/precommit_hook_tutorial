"""test modules
"""
from ..my_app.run import get_predictions


def test_main():
    """test main

    Returns
    -------
    _type_
        _description_
    """
    predictions = get_predictions()
    return len(predictions) > 0
