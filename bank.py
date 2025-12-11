import sys

# Default values if user does not provide input
default_initial = 1000.0
default_deposit = 200.0

# Check if user provided both arguments
if len(sys.argv) == 3:
    initial = float(sys.argv[1])
    deposit = float(sys.argv[2])
    source_initial = "User Input"
    source_deposit = "User Input"
else:
    initial = default_initial
    deposit = default_deposit
    source_initial = "Self-assigned"
    source_deposit = "Self-assigned"

updated = initial + deposit

# Print details
print(f"Initial Balance: {initial} ({source_initial})")
print(f"Deposit Amount: {deposit} ({source_deposit})")

# Check deposit validity
if deposit > 0:
    print("Deposit successful!")
elif deposit == 0:
    print("No deposit made.")
else:
    print("Invalid deposit: cannot be negative.")

print("Updated Balance:", updated)
