"""
Procedural Banking System Mock
==============================

Key Entities
------------------------------------------
Customer   → {"id", "name", "email"}
Account    → {"id", "customer_id", "balance", "currency", "is_active"}
Transaction→ {"id", "from_account", "to_account", "amount", "timestamp"}

"""

from datetime import datetime
from typing import Dict, List, Optional

# =============================================================================
# GLOBAL "DATABASE" — simple in-memory state shared by all functions
# =============================================================================

bank_data = {
    "customers": [],
    "accounts": [],
    "transactions": [],
    "next_customer_id": 1,
    "next_account_id": 1,
    "next_transaction_id": 1,
}


# =============================================================================
# CUSTOMER FUNCTIONS
# =============================================================================

def create_customer(name: str, email: str) -> Dict:
    """Register a new customer in the bank."""
    global bank_data

    customer = {
        "id": bank_data["next_customer_id"],
        "name": name,
        "email": email,
    }
    bank_data["customers"].append(customer)
    bank_data["next_customer_id"] += 1
    print(f"[INFO] Customer created: {customer["name"]} (id={customer["id"]})")
    return customer


def find_customer(customer_id: int) -> Optional[Dict]:
    """Find a customer by ID."""
    for c in bank_data["customers"]:
        if c["id"] == customer_id:
            return c
    return None


# =============================================================================
# ACCOUNT FUNCTIONS
# =============================================================================

def create_account(customer_id: int, currency: str = "USD") -> Dict:
    """Create a new bank account for a given customer."""
    global bank_data

    customer = find_customer(customer_id)
    if not customer:
        print(f"[ERROR] Customer {customer_id} not found.")
        return {}

    account = {
        "id": bank_data["next_account_id"],
        "customer_id": customer_id,
        "balance": 0.0,
        "currency": currency,
        "is_active": True,
    }

    bank_data["accounts"].append(account)
    bank_data["next_account_id"] += 1
    print(f"[INFO] Account #{account["id"]} created for {customer["name"]}")
    return account


def find_account(account_id: int) -> Optional[Dict]:
    """Find an account by ID."""
    for acc in bank_data["accounts"]:
        if acc["id"] == account_id:
            return acc
    return None


def deposit(account_id: int, amount: float, description: str = "Deposit") -> None:
    """Add money to an account."""
    account = find_account(account_id)
    if not account:
        print(f"[ERROR] Account {account_id} not found.")
        return
    if amount <= 0:
        print("[ERROR] Deposit amount must be positive.")
        return

    account["balance"] += amount
    record_transaction(None, account_id, amount, description)
    print(f"[OK] Deposited {amount:.2f} {account["currency"]} into account #{account_id}.")


def withdraw(account_id: int, amount: float, description: str = "Withdrawal") -> None:
    """Withdraw money from an account."""
    account = find_account(account_id)
    if not account:
        print(f"[ERROR] Account {account_id} not found.")
        return
    if amount <= 0:
        print("[ERROR] Withdrawal amount must be positive.")
        return
    if account["balance"] < amount:
        print("[ERROR] Insufficient funds.")
        return

    account["balance"] -= amount
    record_transaction(account_id, None, amount, description)
    print(f"[OK] Withdrew {amount:.2f} {account["currency"]} from account #{account_id}.")


def transfer(from_id: int, to_id: int, amount: float, description: str = "Transfer") -> None:
    """Transfer funds between two accounts."""
    from_acc = find_account(from_id)
    to_acc = find_account(to_id)

    if not from_acc or not to_acc:
        print("[ERROR] Invalid account(s) in transfer.")
        return
    if from_acc["currency"] != to_acc["currency"]:
        print("[ERROR] Currency mismatch.")
        return
    if amount <= 0:
        print("[ERROR] Transfer amount must be positive.")
        return
    if from_acc["balance"] < amount:
        print("[ERROR] Insufficient funds for transfer.")
        return

    from_acc["balance"] -= amount
    to_acc["balance"] += amount
    record_transaction(from_id, to_id, amount, description)
    print(f"[OK] Transferred {amount:.2f} {from_acc["currency"]} from #{from_id} to #{to_id}.")


# =============================================================================
# TRANSACTIONS
# =============================================================================

def record_transaction(from_id: Optional[int], to_id: Optional[int],
                       amount: float, description: str) -> None:
    """Record a transaction in the global log."""
    global bank_data

    txn = {
        "id": bank_data["next_transaction_id"],
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "from_account": from_id,
        "to_account": to_id,
        "amount": amount,
        "description": description,
    }
    bank_data["transactions"].append(txn)
    bank_data["next_transaction_id"] += 1


def list_transactions(account_id: int) -> List[Dict]:
    """Return all transactions involving a given account."""
    result = []
    for t in bank_data["transactions"]:
        if t["from_account"] == account_id or t["to_account"] == account_id:
            result.append(t)
    return result


# =============================================================================
# REPORTING
# =============================================================================

def print_account_summary(account_id: int) -> None:
    """Print current balance and basic info."""
    account = find_account(account_id)
    if not account:
        print("[ERROR] Account not found.")
        return

    customer = find_customer(account["customer_id"])
    print("=" * 40)
    print(f"Account #{account["id"]} — {customer["name"]}")
    print(f"Currency: {account["currency"]}")
    print(f"Balance:  {account["balance"]:.2f}")
    print("=" * 40)
    txns = list_transactions(account_id)
    for t in txns[-5:]:
        print(f"{t["timestamp"]} | {t["description"]:<15} | {t["amount"]:.2f}")


# =============================================================================
# DRIVER CODE
# =============================================================================

if __name__ == "__main__":
    # Create customers
    alice = create_customer("Alice", "alice@example.com")
    bob = create_customer("Bob", "bob@example.com")

    # Create accounts
    acc1 = create_account(alice["id"], "USD")
    acc2 = create_account(bob["id"], "USD")

    # Run some operations
    deposit(acc1["id"], 200)
    withdraw(acc1["id"], 50)
    transfer(acc1["id"], acc2["id"], 100)

    # Print reports
    print_account_summary(acc1["id"])
    print_account_summary(acc2["id"])
    





