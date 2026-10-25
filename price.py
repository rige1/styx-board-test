def total_price(unit_price_cents, quantity, discount_percent=0):
    if unit_price_cents < 0 or quantity < 0:
        raise ValueError("price and quantity must be non-negative")
    subtotal = unit_price_cents * quantity
    return subtotal * (100 + discount_percent) // 100
