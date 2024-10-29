"""Classes for all dessert items"""
from abc import ABC, abstractmethod


class DessertItem(ABC):
    """Base class for all dessert items
    Arguments:
    - name
    """

    def __init__(self, name: str):
        self.name = name
        self.tax_percent = 7.25

    def __str__(self):
        return self.name

    @abstractmethod
    def calculate_cost(self) -> float:
        """
        Calculate the cost of the dessert item
        """
        pass


    def calculate_tax(self) -> float:
        return round(self.calculate_cost() * self.tax_percent / 100, 2)


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

    def calculate_cost(self) -> float:
        return round(self.candy_weight * self.price_per_pound, 2)


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

    def calculate_cost(self) -> float:
        return round(self.cookie_quantity * self.price_per_dozen / 12, 2)


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

    def calculate_cost(self) -> float:
        return round(self.scoop_count * self.price_per_scoop, 2)


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

    def calculate_cost(self) -> float:
        return round(super().calculate_cost() + self.topping_price, 2)
