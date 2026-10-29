"""Case 28: Repeated transaction detection."""

TRANSACTIONS = [
    ("TX101", 2500.00),
    ("TX102", 12000.00),
    ("TX101", 2500.00),
    ("TX103", 1800.00),
    ("TX104", 15000.00),
]
HIGH_VALUE_LIMIT = 10000.00


def audit_transactions(transactions, high_value_limit):
    seen_ids = []
    duplicates = []
    high_value = []
    print("TRANSACTION AUDIT")
    for transaction_id, amount in transactions:
        if transaction_id in seen_ids:
            duplicates.append(transaction_id)
            print(f"Duplicate ID: {transaction_id} (${amount:.2f})")
        else:
            seen_ids.append(transaction_id)
        if amount < 0:
            print(f"Invalid negative amount: {transaction_id} (${amount:.2f})")
        elif amount >= high_value_limit:
            high_value.append(transaction_id)
            print(f"High-value transaction: {transaction_id} (${amount:.2f})")
    print(f"Duplicate transaction IDs: {duplicates}")
    print(f"High-value transaction IDs: {high_value}")
    return duplicates, high_value


if __name__ == "__main__":
    audit_transactions(TRANSACTIONS, HIGH_VALUE_LIMIT)
