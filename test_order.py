import pytest
from dessert import Order, PayType


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
