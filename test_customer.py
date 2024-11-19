from dessertshop import Customer
from dessert import Order, Candy
import uuid


def test_customer():
    customer = Customer("John")
    customer2 = Customer("John")
    assert customer.customer_name == "John"
    assert isinstance(customer.customer_id, uuid.UUID)
    assert customer.customer_id != customer2.customer_id
    assert customer.order_history == []


def test_add2history():
    customer = Customer("John")
    order = Order()
    order.add(Candy("Sjokolade", 5.20, 1.90))
    customer.add2history(order)
    assert customer.order_history == [order]
