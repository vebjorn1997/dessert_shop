"""Classes for all dessert items"""

from abc import ABC, abstractmethod
from packaging import Packaging
from payable import PayType, Payable
from combine import Combinable


class DessertItem(ABC, Packaging):
    """Base class for all dessert items
    Arguments:
    - name
    """

    def __init__(self, name: str):
        self.name = name
        self.packaging: Packaging | None = None
        self.tax_percent: float = 7.25

    def __str__(self):
        return self.name

    def __eq__(self, other) -> bool:
        if isinstance(other, DessertItem):
            return self.calculate_cost() == other.calculate_cost()
        return NotImplemented

    def __ne__(self, other) -> bool:
        if isinstance(other, DessertItem):
            return self.calculate_cost() != other.calculate_cost()
        return NotImplemented

    def __lt__(self, other) -> bool:
        if isinstance(other, DessertItem):
            return self.calculate_cost() < other.calculate_cost()
        return NotImplemented

    def __gt__(self, other) -> bool:
        if isinstance(other, DessertItem):
            return self.calculate_cost() > other.calculate_cost()
        return NotImplemented

    def __le__(self, other) -> bool:
        if isinstance(other, DessertItem):
            return self.calculate_cost() <= other.calculate_cost()
        return NotImplemented

    def __ge__(self, other) -> bool:
        if isinstance(other, DessertItem):
            return self.calculate_cost() >= other.calculate_cost()
        return NotImplemented

    @abstractmethod
    def calculate_cost(self) -> float:
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
        self.packaging = "Bag"
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def __str__(self):
        return f"{self.name}, {self.candy_weight:.2f} lbs, ${self.price_per_pound:.2f}/lb, Packaging: {self.packaging}, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}"

    def __repr__(self):
        return f"Candy('{self.name}', '{self.candy_weight}', '{self.price_per_pound}')"

    def calculate_cost(self) -> float:
        """Calculate the cost of the dessert item, rounded to two decimal places"""
        return round(self.candy_weight * self.price_per_pound, 2)

    def can_combine(self, other: Combinable) -> bool:
        return isinstance(other, Candy) and self.name == other.name

    def combine(self, other: "Candy") -> "Candy":
        if not self.can_combine(other):
            raise TypeError("Cannot combine different items")
        return Candy(
            self.name, self.candy_weight + other.candy_weight, self.price_per_pound
        )


class Cookie(DessertItem):
    """Cookie class, inherits from DessertItem
    Arguments:
    - name,
    - cookie_quantity,
    - price_per_dozen
    """

    def __init__(self, name: str, cookie_quantity: int, price_per_dozen: float):
        super().__init__(name)
        self.packaging = "Box"
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def __str__(self):
        return f"{self.name}, {self.cookie_quantity} unit(s), ${self.price_per_dozen:.2f}/dozen, Packaging: {self.packaging}, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}"

    def __repr__(self):
        return (
            f"Cookie('{self.name}', '{self.cookie_quantity}', '{self.price_per_dozen}')"
        )

    def calculate_cost(self) -> float:
        """Calculate the cost of the dessert item, rounded to two decimal places"""
        return round(self.cookie_quantity * self.price_per_dozen / 12, 2)

    def can_combine(self, other: Combinable) -> bool:
        return (
            isinstance(other, Cookie)
            and self.name == other.name
            and self.price_per_dozen == other.price_per_dozen
        )

    def combine(self, other: "Cookie") -> "Cookie":
        if not self.can_combine(other):
            raise TypeError("Cannot combine different items")
        return Cookie(
            self.name,
            self.cookie_quantity + other.cookie_quantity,
            self.price_per_dozen,
        )


class IceCream(DessertItem):
    """IceCream class, inherits from DessertItem
    Arguments:
    - name,
    - scoop_count,
    - price_per_scoop
    """

    def __init__(self, name: str, scoop_count: int, price_per_scoop: float):
        super().__init__(name)
        self.packaging = "Bowl"
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

    def __str__(self):
        return f"{self.name}, {self.scoop_count} scoop(s), ${self.price_per_scoop:.2f}/scoop, Packaging: {self.packaging}, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}"

    def __repr__(self):
        return (
            f"IceCream('{self.name}', '{self.scoop_count}', '{self.price_per_scoop}')"
        )

    def calculate_cost(self) -> float:
        """Calculate the cost of the dessert item, rounded to two decimal places"""
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
        self.packaging = "Boat"
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self) -> float:
        """Calculate the cost of the dessert item, rounded to two decimal places"""
        return round(super().calculate_cost() + self.topping_price, 2)

    def __str__(self):
        return f"{self.name}, {self.scoop_count} scoop(s), ${self.price_per_scoop:.2f}/scoop, Packaging: {self.packaging}, {self.topping_name}, ${self.topping_price:.2f}, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}"

    def __repr__(self):
        return f"Sundae('{self.name}', '{self.scoop_count}', '{self.price_per_scoop}', '{self.topping_name}', '{self.topping_price}')"


class Order(Payable):
    """Order class for the dessert shop, holds a list of DessertItems"""

    def __init__(self):
        self.orders: list[DessertItem] = []
        self.pay_type: PayType = "CASH"

    def __len__(self):
        return len(self.orders)

    def __iter__(self):
        return iter(self.orders)

    def __next__(self):
        return next(self.orders)

    def __str__(self):
        return (
            "\n".join(str(item) for item in self.orders)
            + f"\n${self.order_cost()}, ${self.order_tax()}, {self.get_pay_type()}"
        )

    def __repr__(self):
        return f"Order({', '.join(repr(item) for item in self.orders)})"

    def add(self, item: DessertItem):
        if not isinstance(item, Combinable):
            self.orders.append(item)
        elif not [
            i for i in self.orders if isinstance(i, Combinable) and i.can_combine(item)
        ]:
            self.orders.append(item)
        elif isinstance(item, Combinable):
            combinable_items = [
                i
                for i in self.orders
                if isinstance(i, type(item)) and i.can_combine(item)
            ]
            if combinable_items:
                matching_item = combinable_items[0]
                self.orders.append(matching_item.combine(item))
                self.orders.remove(matching_item)
        else:
            print("Something went wrong if you are here")
            raise ValueError("Invalid item")

    def order_cost(self) -> float:
        """
        Calculate the cost of the order, rounded to two decimal places, all items in the order
        """
        return round(sum(item.calculate_cost() for item in self.orders), 2)

    def order_tax(self) -> float:
        """
        Calculate the tax of the order, rounded to two decimal places, all items in the order
        """
        return round(sum(item.calculate_tax() for item in self.orders), 2)

    def get_pay_type(self) -> PayType:
        if self.pay_type not in PayType:
            raise ValueError("Invalid get pay type")
        return self.pay_type

    def set_pay_type(self, payment_method: PayType) -> None:
        if payment_method not in PayType:
            raise ValueError("Invalid set pay type")
        self.pay_type = payment_method.value

    def sort(self) -> None:
        self.orders.sort()
