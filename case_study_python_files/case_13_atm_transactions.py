"""Case 13: ATM transaction sequence simulation."""

INITIAL_BALANCE = 5000.00
MAX_WITHDRAWAL = 4000.00
TRANSACTIONS = [
    ("deposit", 1000.00),
    ("withdraw", 1500.00),
    ("withdraw", 6000.00),
    ("deposit", -200.00),
    ("withdraw", 500.00),
]


def process_transactions(initial_balance, transactions, withdrawal_limit):
    balance = initial_balance
    accepted = 0
    rejected = 0

    print("ATM TRANSACTION SUMMARY")
    print(f"Opening balance: ${balance:.2f}")
    for number, transaction in enumerate(transactions, start=1):
        transaction_type, amount = transaction
        if amount <= 0:
            print(f"{number}. REJECTED: amount must be positive (${amount:.2f})")
            rejected += 1
        elif transaction_type == "deposit":
            balance += amount
            accepted += 1
            print(f"{number}. Deposit ${amount:.2f} -> balance ${balance:.2f}")
        elif transaction_type == "withdraw":
            if amount > withdrawal_limit:
                print(f"{number}. REJECTED: exceeds withdrawal limit (${amount:.2f})")
                rejected += 1
            elif amount > balance:
                print(f"{number}. REJECTED: insufficient funds (${amount:.2f})")
                rejected += 1
            else:
                balance -= amount
                accepted += 1
                print(f"{number}. Withdrawal ${amount:.2f} -> balance ${balance:.2f}")
        else:
            print(f"{number}. REJECTED: unknown transaction type '{transaction_type}'")
            rejected += 1

    print(f"Accepted transactions: {accepted}")
    print(f"Rejected transactions: {rejected}")
    print(f"Closing balance: ${balance:.2f}")
    return balance, accepted, rejected


if __name__ == "__main__":
    process_transactions(INITIAL_BALANCE, TRANSACTIONS, MAX_WITHDRAWAL)
