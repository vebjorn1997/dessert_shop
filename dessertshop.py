from dessert import Candy, Cookie, IceCream, Sundae, Order, PayType
from utils import validate_float, validate_int, validate_string, create_receipt_folder
import receipt
import uuid

class Customer:
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.customer_id = uuid.uuid4()
        self.order_history: list[Order] = []

    def add2history(self, order: Order) -> "Customer":
        self.order_history.append(order)
        return self


class DessertShop:
    def __init__(self):
        self.customer_db: dict[str, Customer] = {}

    def user_prompt_candy(self) -> Candy:
        name = validate_string("Enter the name of the candy: ")
        weight = validate_float("Enter the weight of the candy: ")
        price_per_pound = validate_float("Enter the price per pound of the candy: ")
        return Candy(name, weight, price_per_pound)

    def user_prompt_cookie(self) -> Cookie:
        name = validate_string("Enter the name of the cookie: ")
        quantity = validate_float("Enter the quantity of the cookie: ")
        price_per_dozen = validate_float("Enter the price per dozen of the cookie: ")
        return Cookie(name, quantity, price_per_dozen)

    def user_prompt_icecream(self) -> IceCream:
        name = validate_string("Enter the name of the ice cream: ")
        scoop_count = validate_int("Enter the number of scoops of the ice cream: ")
        price_per_scoop = validate_float("Enter the price per scoop of the ice cream: ")
        return IceCream(name, scoop_count, price_per_scoop)

    def user_prompt_sundae(self) -> Sundae:
        name = validate_string("Enter the name of the sundae: ")
        scoop_count = validate_int("Enter the number of scoops of the sundae: ")
        price_per_scoop = validate_float("Enter the price per scoop of the sundae: ")
        topping_name = validate_string("Enter the name of the topping: ")
        topping_price = validate_float("Enter the price of the topping: ")
        return Sundae(name, scoop_count, price_per_scoop, topping_name, topping_price)

    def user_prompt_pay_type(self, pay_type: str) -> PayType:
        return PayType(pay_type)


def pay_type_prompt(order: Order, shop: DessertShop):
    pay_type_prompt = "\n".join(
        [
            "\n",
            "1: Cash",
            "2: Card",
            "3: Phone",
            "\nWhat type of payment would you like to use? (1-3): ",
        ]
    )

    pay_type_done: bool = False
    while not pay_type_done:
        pay_type_choice = input(pay_type_prompt)
        match pay_type_choice:
            case "1":
                order.set_pay_type(shop.user_prompt_pay_type(PayType.CASH))
                pay_type_done = True
            case "2":
                order.set_pay_type(shop.user_prompt_pay_type(PayType.CARD))
                pay_type_done = True
            case "3":
                order.set_pay_type(shop.user_prompt_pay_type(PayType.PHONE))
                pay_type_done = True
            case _:
                print("Invalid response:  Please enter a choice from the menu (1-3)")


def register_customer(order: Order, shop: DessertShop):
    customer_name = validate_string("Enter your name: ")
    if customer_name in shop.customer_db:
        shop.customer_db[customer_name].add2history(order)
    else:
        shop.customer_db[customer_name] = Customer(customer_name)
        shop.customer_db[customer_name].add2history(order)

def item_prompt(shop: DessertShop):
    order = Order()
    prompt = "\n".join(
        [
            "\n",
            "1: Candy",
            "2: Cookie",
            "3: Ice Cream",
            "4: Sunday",
            "\nWhat would you like to add to the order? (1-4, Enter for done): ",
        ]
    )
    done: bool = False
    while not done:
        choice = input(prompt)
        match choice:
            case "":
                if len(order) > 0:
                    register_customer(order, shop)
                    pay_type_prompt(order, shop)
                    done = True
                else:
                    print("No items in order")
            case "1":
                item = shop.user_prompt_candy()
                order.add(item)
                print(item)
            case "2":
                item = shop.user_prompt_cookie()
                order.add(item)
                print(item)
            case "3":
                item = shop.user_prompt_icecream()
                order.add(item)
                print(item)
            case "4":
                item = shop.user_prompt_sundae()
                order.add(item)
                print(item)
            case _:
                print(
                    "Invalid response:  Please enter a choice from the menu (1-4) or Enter"
                )
    order.sort()

def print_order_history(customer: Customer):
    data = [["Name", "Item Cost", "Tax"]]

    data.append(["Customer Name", "", customer.customer_name])
    data.append(["Customer ID", "", customer.customer_id])

    data.append(["Total Orders", "", len(customer.order_history)])

    for order in customer.order_history:
        order_line = order.__str__().split("\n")

        data.append([""])
        data.append(["Order Start"])
        for item in order_line:
            if len(order_line) == order_line.index(item) + 1:
                data.append([""])
                data.append(["Total items in order", "", len(order)])
                data.append(["Subtotal", f"${order.order_cost()}", f"${order.order_tax()}"])
                data.append(
                    [
                        "Order Total",
                        "",
                        f"${round(order.order_cost() + order.order_tax(), 2)}",
                    ]
                )
                data.append(["Paid with ", "", order.get_pay_type()])

            else:
                splitted = item.split(",")
                data.append([splitted[0], splitted[-2], splitted[-1]])

    receipt.make_receipt(data, f"receipts/{customer.customer_name}_receipt.pdf")


def main():
    shop = DessertShop()
    orders_finished: bool = False
    prompt = "\n".join(
        [
            "\n",
            "Do you want to start a new order? (y/n): ",
        ]
    )

    item_prompt(shop)
    while not orders_finished:
        choice = input(prompt)
        match choice:
            case "y":
                item_prompt(shop)
            case _:
                orders_finished = True

    create_receipt_folder()
    for customer in shop.customer_db.values():
        print_order_history(customer)

if __name__ == "__main__":
    main()
