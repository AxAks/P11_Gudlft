"""
Tests file for request info extractions
"""
from lib_request.lib_request import extract_required_places


def test_an_entered_amount_of_places_should_return_a_int():
    """
    Checks that the input can be converted into an integer
    """
    form = {'places': '2'}
    assert type(extract_required_places(form)) == int
