from dessert import DessertItem, Candy, Cookie, IceCream, Sundae
import receipt


class Order:
    """Order class for the dessert shop, holds a list of DessertItems"""

    def __init__(self):
        self.order: list[DessertItem] = []

    def __len__(self):
        return len(self.order)

    def __iter__(self):
        return iter(self.order)

    def __next__(self):
        return next(self.order)

    def add(self, item: DessertItem):
        self.order.append(item)

    def order_cost(self) -> float:
        return round(sum(item.calculate_cost() for item in self.order), 2)

    def order_tax(self) -> float:
        return round(sum(item.calculate_tax() for item in self.order), 2)


def main():
    order = Order()
    order.add(Candy("Candy Corn", 1.5, 0.25))
    order.add(Candy("Gummy Bears", 0.25, 0.35))
    order.add(Cookie("Chocolate Chip", 6, 3.99))
    order.add(IceCream("Pistachio", 2, 0.79))
    order.add(Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))
    order.add(Cookie("Oatmeal Raisin", 2, 3.45))

    data = [["Name", "Item Cost", "Tax"]]

    for item in order:
        data.append([item.name, item.calculate_cost(), item.calculate_tax()])

    data.append([""])
    data.append(["Subtotal", order.order_cost(), order.order_tax()])
    data.append(["Order Total", "", order.order_cost() + order.order_tax()])
    data.append(["Total items in order", "", len(order)])

    receipt.make_receipt(data, "receipt.pdf")


if __name__ == "__main__":
    main()
