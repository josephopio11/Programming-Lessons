total_cost = 0.00
sugar_tax = 0.50
print("Sandwich or Wrap?")
bread_type = input().lower()
# TOTAL COST FOR SANDWICH IS 2
print("Meat, Vegetarian or Vegan?")
filling_type = input().lower()
#  TOTAL COST WILL BE 2 + 1.5 = 3.5
print("Cookie, Crisps, Fruit or None")
pudding = input().lower()
# TOTAL COST WILL BE 3.5 + 0.5 = 4
print("Fizzy drink, Water, Juice or None")
drink = input().lower()
print("Would you like an extra sauce? (y/n)")
extra_sauce = input().lower()
print("Would you like an extra salad? (y/n)")
extra_salad = input().lower()
if bread_type != "sandwich":
    total_cost = 2.00
else:
    total_cost = 3.00
if filling_type == "vegetarian" or filling_type == "vegan":
    total_cost = total_cost + 1.00
else:
    total_cost = total_cost + 1.50
if pudding == "cookie" and drink == "fizzy drink":
    total_cost = total_cost + sugar_tax
if pudding == "none" and drink == "none":
    total_cost = total_cost - 0.50
if (extra_salad == "y" or extra_salad == "yes") and (extra_sauce == "y" or extra_sauce == "yes"):
    total_cost = total_cost + 1.00
print(f"Your total cost is: £{total_cost}")
