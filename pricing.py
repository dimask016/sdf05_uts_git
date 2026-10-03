TAX_MULTIPLIER = 1.11  # PPN 11%


def calculate_subtotal(quantity: float, unit_price: float) -> float:
    return quantity * unit_price


def apply_tax(amount: float) -> float:
    return amount * TAX_MULTIPLIER


def calculate_order_total(quantity: float, unit_price: float) -> float:
    # Perhitungan langsung di branch main
    return (quantity * unit_price) * TAX_MULTIPLIER
