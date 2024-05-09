import source.shapes as shapes


def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_paremeter(my_rectangle):
    assert my_rectangle.perimeter() == 10*2 + 20*2

def test_not_equal(my_rectangle, another_rectangle):
    assert my_rectangle != another_rectangle