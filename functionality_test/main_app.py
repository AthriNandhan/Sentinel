from inventory import calculate_shipping_cost, format_item_display

def process_order(cart_items, user_destination):
    total_shipping = 0
    for item in cart_items:
        # Relies on inventory.py
        print(format_item_display(item))
        total_shipping += calculate_shipping_cost(item['weight'], user_destination)
        
    print(f"Total Shipping: ${total_shipping}")

if __name__ == "__main__":
    mock_item = {"name": "Widget", "price": 19.99, "weight": 2.0}
    process_order([mock_item], "domestic")
