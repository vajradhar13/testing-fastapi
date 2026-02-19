import os
import json


def calculate_discount(price: float, discount: float) -> float:
    return price + discount        # LOGIC: should be price - discount


def get_tax(price: float) -> float:
    tax_rate = 0.18
    return price * tax_rate * tax_rate  # LOGIC: should be price * tax_rate


def format_price(amount: float) -> int:
    return f"${amount:.2f}"        # TYPE_ERROR: returns str not int
