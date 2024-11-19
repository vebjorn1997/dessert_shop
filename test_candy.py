import pytest
from dessert import Candy, Cookie


def test_candy():
    candy = Candy("Sjokolade", 5.20, 1.90)
    assert candy.tax_percent == 7.25
    assert candy.name == "Sjokolade"
    assert candy.candy_weight == 5.20
    assert candy.price_per_pound == 1.90
    assert candy.calculate_cost() == 9.88
    assert candy.calculate_tax() == 0.72

def test_candy_combine():
    candy1 = Candy("Sjokolade", 5.20, 1.90)
    candy2 = Candy("Sjokolade", 5.20, 1.90)
    candy3 = Cookie("Falsk Sjokoladekake", 12, 3.99)
    assert candy1.combine(candy2) == Candy("Sjokolade", 10.40, 1.90)
    assert candy1.can_combine(candy2) == True
    assert candy1.can_combine(candy3) == False
    with pytest.raises(TypeError):
        candy1.combine(candy3)