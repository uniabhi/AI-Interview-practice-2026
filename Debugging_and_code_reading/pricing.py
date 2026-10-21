def final_price(price: float, discount_percent: float) -> float:
    if price < 0:
        raise ValueError("price cannot be negative")

    if not 0 <= discount_percent <= 100:
        raise ValueError("discount must be between 0 and 100")
    return price * (1 - discount_percent / 100)