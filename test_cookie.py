import pytest
from dessert import Cookie, Candy


def test_cookie():
    cookie = Cookie("Sjokoladekake", 12, 3.99)
    assert cookie.tax_percent == 7.25
    assert cookie.name == "Sjokoladekake"
    assert cookie.cookie_quantity == 12
    assert cookie.price_per_dozen == 3.99
    assert cookie.calculate_cost() == 3.99
    assert cookie.calculate_tax() == 0.29


def test_cookie_combine():
    cookie1 = Cookie("Sjokoladekake", 12, 3.99)
    cookie2 = Cookie("Sjokoladekake", 12, 3.99)
    cookie3 = Candy("Falsk Sjokolade", 5.20, 1.90)
    assert cookie1.combine(cookie2) == Cookie("Sjokoladekake", 24, 3.99)
    assert cookie1.can_combine(cookie2)
    assert not cookie1.can_combine(cookie3)
    with pytest.raises(TypeError):
        cookie1.combine(cookie3)
