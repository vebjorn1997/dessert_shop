from dessert import DessertItem, Candy, Cookie, IceCream, Sundae


class Order:
    """Order class for the dessert shop, holds a list of DessertItems"""
    def __init__(self):
        self.order: list[DessertItem] = []

    def add(self, item: DessertItem):
        self.order.append(item)

    def __len__(self):
        return len(self.order)

    def __iter__(self):
        return iter(self.order)

    def __next__(self):
        return next(self.order)


def main():
    order = Order()
    order.add(Candy("Candy Corn", 1.5, 0.25))
    order.add(Candy("Gummy Bears", 0.25, 0.35))
    order.add(Cookie("Chocolate Chip", 6, 3.99))
    order.add(IceCream("Pistachio", 2, 0.79))
    order.add(Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))
    order.add(Cookie("Oatmeal Raisin", 2, 3.45))
    for item in order:
        print(item)
    print(len(order))


if __name__ == "__main__":
    main()
