import os


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


def create_receipt_folder():
    if not os.path.exists("receipts"):
        try:
            os.makedirs("receipts", exist_ok=True)
        except Exception as e:
            print(e)
