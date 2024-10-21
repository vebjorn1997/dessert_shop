"""Classes for all dessert items"""


class DessertItem:
    """Base class for all dessert items
    Arguments:
    - name
    """

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Candy(DessertItem):
    """Candy class, inherits from DessertItem
    Arguments:
    - name,
    - candy_weight,
    - price_per_pound
    """

    def __init__(self, name: str, candy_weight: float, price_per_pound: float):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound


class Cookie(DessertItem):
    """Cookie class, inherits from DessertItem
    Arguments:
    - name,
    - cookie_quantity,
    - price_per_dozen
    """

    def __init__(self, name: str, cookie_quantity: int, price_per_dozen: float):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen


class IceCream(DessertItem):
    """IceCream class, inherits from DessertItem
    Arguments:
    - name,
    - scoop_count,
    - price_per_scoop
    """

    def __init__(self, name: str, scoop_count: int, price_per_scoop: float):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop


class Sundae(IceCream):
    """Sundae class, inherits from IceCream
    Arguments:
    - name,
    - scoop_count,
    - price_per_scoop,
    - topping_name
    - topping_price
    """

    def __init__(
        self,
        name: str,
        scoop_count: int,
        price_per_scoop: float,
        topping_name: str,
        topping_price: float,
    ):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
