def total_price(unit_price_cents, quantity):
    if unit_price_cents < 0 or quantity < 0:
        raise ValueError("price and quantity must be non-negative")
    return unit_price_cents * quantity
