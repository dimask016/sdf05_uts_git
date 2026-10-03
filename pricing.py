MEMBER_DISCOUNT_FACTOR = 0.85   # Diskon member diubah jadi 15%
TAX_MULTIPLIER = 1.11           # Pajak 11%

def calculate_subtotal(quantity: float, unit_price: float) -> float:
    return quantity * unit_price

def apply_member_discount(subtotal: float, is_member: bool) -> float:
    if is_member:
        return subtotal * MEMBER_DISCOUNT_FACTOR
    return subtotal

def apply_tax(amount: float) -> float:
    return amount * TAX_MULTIPLIER

def calculate_order_total(quantity: float, unit_price: float, is_member: bool = False) -> float:
    subtotal = calculate_subtotal(quantity, unit_price)
    discounted_amount = apply_member_discount(subtotal, is_member)
    return apply_tax(discounted_amount)
