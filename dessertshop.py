from dessert import Candy, Cookie, IceCream, Sundae, Order
import receipt


class DessertShop:
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


def validate_float(string: float | int | str) -> float:
    while True:
        try:
            return float(input(string))
        except ValueError:
            print("Invalid input detected, please enter a float.")


def validate_int(string: int | str) -> int:
    while True:
        try:
            return int(input(string))
        except ValueError:
            print("Invalid input detected, please enter an integer.")


def validate_string(string: str) -> str:
    while True:
        try:
            return str(input(string))
        except ValueError:
            print("Invalid input detected, please enter a string.")


def main():
    shop = DessertShop()
    order = Order()
    done: bool = False
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

    while not done:
        choice = input(prompt)
        match choice:
            case "":
                done = True
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
