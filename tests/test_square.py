import pytest
import source.shapes as shapes

@pytest.mark.parametrize("side_length , expected_area", [(3, 9), (4, 16), (5, 25), (9, 81)])
def test_mutilple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length , expected_perimeter", [(3, 12), (4, 16), (5, 20), (6,24)])
def test_mutilple_square_perimeter(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter