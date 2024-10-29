from dessert import IceCream

def test_icecream():
    icecream = IceCream("Sjokoladeis", 3, 1.99)
    assert icecream.tax_percent == 7.25
    assert icecream.name == "Sjokoladeis"
    assert icecream.scoop_count == 3
    assert icecream.price_per_scoop == 1.99
    assert icecream.calculate_cost() == 5.97
    assert icecream.calculate_tax() == 0.43