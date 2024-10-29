from dessert import Sundae

def test_sundae():
    sundae = Sundae("Sjokoladeiskrem", 3, 1.99, "Oboy", 0.75)
    assert sundae.tax_percent == 7.25
    assert sundae.name == "Sjokoladeiskrem"
    assert sundae.scoop_count == 3
    assert sundae.price_per_scoop == 1.99
    assert sundae.topping_name == "Oboy"
    assert sundae.topping_price == 0.75
    assert sundae.calculate_cost() == 6.72
    assert sundae.calculate_tax() == 0.49