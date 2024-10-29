from dessert import Candy, Cookie
from dessertshop import Order

def test_order():
    order = Order()
    order.add(Candy("Candy Corn", 1.5, 0.25))
    order.add(Cookie("Chocolate Chip", 24, 10))
    assert order.order_cost() == 20.38
    assert order.order_tax() == 1.48
    assert len(order) == 2
    for item in order:
        assert item.name == "Candy Corn" or item.name == "Chocolate Chip"