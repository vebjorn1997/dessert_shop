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


def test_relational_operators():
    order = Order()
    order.add(Candy("Candy Corn", 1.5, 0.25))
    order.add(Candy("Fake Candy", 1.5, 0.25))
    order.add(Candy("Alt Candy", 5, 1.0))
    assert order.orders[0] == order.orders[1]
    assert order.orders[0] != order.orders[2]

    order2 = Order()
    order2.add(Candy("Expensive Candy", 5, 1.0))
    order2.add(Candy("Cheap Candy", 1, 1.0))
    order2.add(Candy("Similar Candy", 1, 1.0))
    assert order2.orders[0] > order2.orders[1]
    assert order2.orders[2] >= order2.orders[1]

    order3 = Order()
    order3.add(Candy("Similar Candy", 0.5, 0.8))
    order3.add(Candy("Alt Similar Candy", 1, 1.0))
    order3.add(Candy("Almost Candy", 1, 1.0))
    assert order3.orders[0] < order3.orders[1]
    assert order3.orders[2] <= order3.orders[1]
