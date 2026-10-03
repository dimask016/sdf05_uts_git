MEMBER_DISCOUNT_FACTOR = 0.90   # Applies a 10% discount
TAX_MULTIPLIER = 1.11           # Applies an 11% tax rate


def calculate_subtotal(quantity: float, unit_price: float) -> float:
    """Calculates the base price prior to taxes and discounts."""
    return quantity * unit_price


def apply_member_discount(subtotal: float, is_member: bool) -> float:
    """Applies a 10% discount if the customer is a registered member."""
    if is_member:
        return subtotal * MEMBER_DISCOUNT_FACTOR
    return subtotal


def apply_tax(amount: float) -> float:
    """Applies an 11% tax to the final amount."""
    return amount * TAX_MULTIPLIER


def calculate_order_total(quantity: float, unit_price: float, is_member: bool = False) -> float:
    subtotal = calculate_subtotal(quantity, unit_price)
    discounted_amount = apply_member_discount(subtotal, is_member)
    return apply_tax(discounted_amount)
