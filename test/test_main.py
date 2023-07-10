from ..my_app.run import get_predictions


def test_main():
    predictions = get_predictions()
    assert len(predictions) > 0
