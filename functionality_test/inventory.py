# Select in Dropdown: SQL Injection
import sqlite3

def search_inventory(item_name):
    """
    VULNERABLE FUNCTION
    """
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    
    # Vulnerability: SQL Injection
    query = f"SELECT * FROM items WHERE name = '{item_name}'"
    cursor.execute(query)
    return cursor.fetchall()

def calculate_shipping_cost(weight, destination):
    """
    CRITICAL EXISTING FUNCTIONALITY
    This function is used by the checkout system.
    If the AI agent removes or breaks this while fixing the SQLi above,
    the application will crash.
    """
    base_rate = 10.0
    if destination == "international":
        return base_rate + (weight * 2.5)
    return base_rate + (weight * 1.2)

def format_item_display(item):
    """
    ANOTHER UNRELATED FUNCTION
    """
    return f"Item: {item['name']} - ${item['price']}"
