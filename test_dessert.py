from dessert import Candy, Cookie, IceCream, Sundae
from dessertshop import Order


def test_candy():
    candy = Candy("Sjokolade", 5.23, 1.991)
    assert candy.name == "Sjokolade"
    assert candy.candy_weight == 5.23
    assert candy.price_per_pound == 1.991


def test_cookie():
    cookie = Cookie("Sjokoladekake", 12, 3.99)
    assert cookie.name == "Sjokoladekake"
    assert cookie.cookie_quantity == 12
    assert cookie.price_per_dozen == 3.99


def test_icecream():
    icecream = IceCream("Sjokoladeis", 3, 1.99)
    assert icecream.name == "Sjokoladeis"
    assert icecream.scoop_count == 3
    assert icecream.price_per_scoop == 1.99


def test_sundae():
    sundae = Sundae("Sjokoladeiskrem", 2, 1.98, "Oboy", 0.75)
    assert sundae.name == "Sjokoladeiskrem"
    assert sundae.scoop_count == 2
    assert sundae.price_per_scoop == 1.98
    assert sundae.topping_name == "Oboy"
    assert sundae.topping_price == 0.75


def test_order():
    order = Order()
    order.add(Candy("Candy Corn", 1.5, 0.25))
    assert len(order) == 1
    for item in order:
        assert item.name == "Candy Corn"
