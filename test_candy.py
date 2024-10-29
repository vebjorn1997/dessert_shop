from dessert import Candy


def test_candy():
    candy = Candy("Sjokolade", 5.20, 1.90)
    assert candy.tax_percent == 7.25
    assert candy.name == "Sjokolade"
    assert candy.candy_weight == 5.20
    assert candy.price_per_pound == 1.90
    assert candy.calculate_cost() == 9.88
    assert candy.calculate_tax() == 0.72