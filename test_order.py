import pytest
from dessert import Order, PayType, Candy


def test_order():
    order = Order()
    assert order.order_cost() == 0
    assert order.order_tax() == 0
    assert order.get_pay_type() == PayType.CASH.value
    order.set_pay_type(PayType.CARD)
    assert order.get_pay_type() == PayType.CARD.value
    order.set_pay_type(PayType.PHONE)
    assert order.get_pay_type() == PayType.PHONE.value

    # Raise error when setting wrong pay_type
    with pytest.raises(ValueError):
        order.set_pay_type("1")
    # Raise error when pay_type is wrong
    order.pay_type = "1"
    with pytest.raises(ValueError):
        order.get_pay_type()


def test_sort():
    order = Order()
    order.add(Candy("Candy Corn", 1.5, 0.25))
    order.add(Candy("Fake Candy", 1.1, 0.1))
    order.add(Candy("Alt Candy", 5, 1.0))
    order.sort()
    assert order.orders[0].name == "Fake Candy"
    assert order.orders[-1].name == "Alt Candy"
