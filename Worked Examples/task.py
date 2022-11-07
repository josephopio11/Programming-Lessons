print("---Welcome to Split My Bill---") # Print this
print("What is the total bill?") # Print this
bill_total = float(input())
print("How many people are sharing?")
people = int(input())
print("What percentage tip would you like to leave?")
tip_percentage = int(input())

percentage_decimal = tip_percentage / 100
tip_total = bill_total * percentage_decimal
bill_total = bill_total + tip_total

cost_per_person = bill_total / people

print(f"Total bill including tip is £{bill_total}")
print(f"Total cost per person is £{cost_per_person}")
