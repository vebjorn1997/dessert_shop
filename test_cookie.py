from dessert import Cookie


def test_cookie():
    cookie = Cookie("Sjokoladekake", 12, 3.99)
    assert cookie.tax_percent == 7.25
    assert cookie.name == "Sjokoladekake"
    assert cookie.cookie_quantity == 12
    assert cookie.price_per_dozen == 3.99
    assert cookie.calculate_cost() == 3.99
    assert cookie.calculate_tax() == 0.29
