import sys

if len(sys.argv) != 3:
    print("Usage: python bank_balance.py <initial_balance> <deposit_amount>")
    sys.exit(1)

initial = float(sys.argv[1])
deposit = float(sys.argv[2])

updated = initial + deposit

print("Updated Balance:", updated)
