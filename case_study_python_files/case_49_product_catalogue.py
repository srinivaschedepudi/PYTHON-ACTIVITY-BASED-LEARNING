"""Case 49: Tuple-based product catalogue audit."""

# Each immutable tuple is (product_id, name, unit_price, stock_quantity).
PRODUCTS = [
    ("P101", "Notebook", 45.00, 12),
    ("P102", "Pen", 10.00, 3),
    ("P103", "Folder", 0.00, 8),
    ("P104", "Marker", 35.00, 0),
]
REORDER_LEVEL = 5


def audit_catalogue(products, reorder_level):
    total_inventory_value = 0.0
    reorder_items = []
    invalid_records = []
    print("PRODUCT CATALOGUE AUDIT")
    for product in products:
        product_id, name, price, stock = product
        if price <= 0 or stock < 0 or name == "" or product_id == "":
            invalid_records.append(product_id)
            print(f"{product_id}: INVALID record")
            continue
        value = price * stock
        total_inventory_value += value
        status = "REORDER" if stock <= reorder_level else "OK"
        if stock <= reorder_level:
            reorder_items.append(product_id)
        print(f"{product_id} {name}: value=${value:.2f}, stock={stock} ({status})")
    print(f"Total valid inventory value: ${total_inventory_value:.2f}")
    print(f"Items to reorder: {reorder_items}")
    print(f"Invalid records: {invalid_records}")
    return total_inventory_value, reorder_items, invalid_records


if __name__ == "__main__":
    audit_catalogue(PRODUCTS, REORDER_LEVEL)
