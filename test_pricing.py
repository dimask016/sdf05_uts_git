from pricing import calculate_order_total

def test_calculate_order_total():
    assert calculate_order_total(10, 50) == 555.0
