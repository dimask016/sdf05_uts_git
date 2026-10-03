TAX_MULTIPLIER = 1.11

def calculate_subtotal(quantity: float, unit_price: float) -> float:
    """Calculates the base price prior to taxes."""
    return quantity * unit_price

def apply_tax(amount: float) -> float:
    """Applies an 11% tax to the final amount."""
    return amount * TAX_MULTIPLIER

def calculate_order_total(quantity: float, unit_price: float) -> float:
    subtotal = calculate_subtotal(quantity, unit_price)
    return apply_tax(subtotal)
